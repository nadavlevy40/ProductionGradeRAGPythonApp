import logging
import uuid
import os
import datetime
from fastapi import FastAPI
from pydantic import BaseModel  # Added for request bodies
from dotenv import load_dotenv

import inngest
import inngest.fast_api
from inngest.experimental import ai

# Import your custom modules (assuming these files exist in your project)
from data_loader import load_and_chunk_pdf, embed_texts
from vector_db import QdrantStorage
from custom_types import RAQQueryResult, RAGSearchResult, RAGUpsertResult, RAGChunkAndSrc

# 1. Load Environment Variables
load_dotenv()

# 2. Initialize Inngest Client
inngest_client = inngest.Inngest(
    app_id="rag_app",
    logger=logging.getLogger("uvicorn"),
    is_production=False,
    serializer=inngest.PydanticSerializer()
)

# 3. Define Inngest Functions

@inngest_client.create_function(
    fn_id="RAG: Ingest PDF",
    trigger=inngest.TriggerEvent(event="rag/ingest_pdf"),
    throttle=inngest.Throttle(
        limit=2,  # Fixed: Used 'limit' instead of 'count'
        period=datetime.timedelta(minutes=1)
    ),
    rate_limit=inngest.RateLimit(
        limit=1,
        period=datetime.timedelta(hours=4),
        key="event.data.source_id",
    ),
)
async def rag_ingest_pdf(ctx: inngest.Context):
    def _load(ctx: inngest.Context) -> RAGChunkAndSrc:
        pdf_path = ctx.event.data["pdf_path"]
        # Use provided source_id or fallback to path
        source_id = ctx.event.data.get("source_id", pdf_path)
        chunks = load_and_chunk_pdf(pdf_path)
        return RAGChunkAndSrc(chunks=chunks, source_id=source_id)

    def _upsert(chunks_and_src: RAGChunkAndSrc) -> RAGUpsertResult:
        chunks = chunks_and_src.chunks
        source_id = chunks_and_src.source_id
        vecs = embed_texts(chunks)
        # Create deterministic IDs based on source and index
        ids = [str(uuid.uuid5(uuid.NAMESPACE_URL, f"{source_id}:{i}")) for i in range(len(chunks))]
        payloads = [{"source": source_id, "text": chunks[i]} for i in range(len(chunks))]
        
        QdrantStorage().upsert(ids, vecs, payloads)
        return RAGUpsertResult(ingested=len(chunks))

    # Step 1: Load and Chunk
    chunks_and_src = await ctx.step.run("load-and-chunk", lambda: _load(ctx), output_type=RAGChunkAndSrc)
    
    # Step 2: Embed and Upsert
    ingested = await ctx.step.run("embed-and-upsert", lambda: _upsert(chunks_and_src), output_type=RAGUpsertResult)
    
    return ingested.model_dump()


@inngest_client.create_function(
    fn_id="RAG: Query PDF",
    trigger=inngest.TriggerEvent(event="rag/query_pdf_ai")
)
async def rag_query_pdf_ai(ctx: inngest.Context):
    def _search(question: str, top_k: int = 5) -> RAGSearchResult:
        query_vec = embed_texts([question])[0]
        store = QdrantStorage()
        found = store.search(query_vec, top_k)
        return RAGSearchResult(contexts=found["contexts"], sources=found["sources"])

    question = ctx.event.data["question"]
    top_k = int(ctx.event.data.get("top_k", 5))

    # Step 1: Vector Search
    found = await ctx.step.run("embed-and-search", lambda: _search(question, top_k), output_type=RAGSearchResult)

    # Prepare Prompt
    context_block = "\n\n".join(f"- {c}" for c in found.contexts)
    user_content = (
        "Use the following context to answer the question.\n\n"
        f"Context:\n{context_block}\n\n"
        f"Question: {question}\n"
        "Answer concisely using the context above."
    )

    adapter = ai.openai.Adapter(
        auth_key=os.getenv("OPENAI_API_KEY"),
        model="gpt-4o-mini"
    )

    # Step 2: LLM Inference
    res = await ctx.step.ai.infer(
        "llm-answer",
        adapter=adapter,
        body={
            "max_tokens": 1024,
            "temperature": 0.2,
            "messages": [
                {"role": "system", "content": "You answer questions using only the provided context."},
                {"role": "user", "content": user_content}
            ]
        }
    )

    answer = res["choices"][0]["message"]["content"].strip()
    return {"answer": answer, "sources": found.sources, "num_contexts": len(found.contexts)}


# 4. Initialize FastAPI
app = FastAPI()

# --- API Models ---
class IngestRequest(BaseModel):
    pdf_path: str
    source_id: str | None = None

class QueryRequest(BaseModel):
    question: str
    top_k: int = 5

# --- API Endpoints ---

@app.get("/")
async def root():
    """Root endpoint to verify server is running."""
    return {
        "message": "RAG Server is Running!",
        "endpoints": [
            "POST /trigger-ingest", 
            "POST /trigger-query", 
            "/api/inngest"
        ]
    }

@app.post("/trigger-ingest")
async def trigger_ingest(request: IngestRequest):
    """
    Triggers the background job to ingest a PDF.
    """
    # FIX: Generate a source_id from the filename automatically
    # e.g., "/path/to/transcript.pdf" -> "transcript.pdf"
    source_id = os.path.basename(request.pdf_path)

    await inngest_client.send(
        inngest.Event(
            name="rag/ingest_pdf",
            data={
                "pdf_path": request.pdf_path,
                "source_id": source_id  # <--- WE ADD THIS LINE
            }
        )
    )
    return {"status": "Ingestion event sent", "source_id": source_id}
@app.post("/trigger-query")
async def trigger_query(request: QueryRequest):
    """Manually trigger the AI Query workflow."""
    # Note: Inngest functions run asynchronously. 
    # To get the result, you'd typically check the Inngest dashboard or use `inngest.wait_for_event` logic pattern.
    await inngest_client.send(
        inngest.Event(
            name="rag/query_pdf_ai",
            data={
                "question": request.question,
                "top_k": request.top_k
            }
        )
    )
    return {"status": "Query event sent", "data": request.model_dump()}

# 5. Connect Inngest to FastAPI
inngest.fast_api.serve(app, inngest_client, [rag_ingest_pdf, rag_query_pdf_ai])
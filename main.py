import logging
from fastapi import FastAPI
import inngest
import inngest.fast_api
from pydantic import BaseModel
from dotenv import load_dotenv
import uuid
import os
import datetime
from openai import OpenAI

# Custom modules
from data_loader import load_and_chunk_pdf, embed_texts
from vector_db import QdrantStorage

load_dotenv()

# 1. Setup Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("uvicorn")

# 2. Setup Clients
openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

inngest_client = inngest.Inngest(
    app_id="rag_app",
    logger=logger,
    is_production=False,
)

# --- FUNCTION 1: INGEST PDF ---
@inngest_client.create_function(
    fn_id="RAG: Ingest PDF",
    trigger=inngest.TriggerEvent(event="rag/ingest_pdf"),
    throttle=inngest.Throttle(limit=2, period=datetime.timedelta(minutes=1))
)
async def rag_ingest_pdf(ctx: inngest.Context):
    
    def _load():
        pdf_path = ctx.event.data["pdf_path"]
        # Use filename as source_id if not provided
        source_id = ctx.event.data.get("source_id", pdf_path)
        logger.info(f"Loading PDF: {pdf_path}")
        chunks = load_and_chunk_pdf(pdf_path)
        # Return simple dict to avoid serialization errors
        return {"chunks": chunks, "source_id": source_id}

    def _upsert(data):
        chunks = data["chunks"]
        source_id = data["source_id"]
        logger.info(f"Embedding {len(chunks)} chunks for {source_id}...")
        
        vecs = embed_texts(chunks)
        
        # Create deterministic IDs
        ids = [str(uuid.uuid5(uuid.NAMESPACE_URL, f"{source_id}:{i}")) for i in range(len(chunks))]
        payloads = [{"source": source_id, "text": chunk} for chunk in chunks]
        
        QdrantStorage().upsert(ids, vecs, payloads)
        return {"ingested": len(chunks)}

    # Run steps
    data = await ctx.step.run("load-and-chunk", _load)
    result = await ctx.step.run("embed-and-upsert", lambda: _upsert(data))
    
    return result


# --- FUNCTION 2: QUERY PDF (ASYNC / BACKGROUND) ---
@inngest_client.create_function(
    fn_id="RAG: Query PDF",
    trigger=inngest.TriggerEvent(event="rag/query_pdf_ai")
)
async def rag_query_pdf_ai(ctx: inngest.Context):
    question = ctx.event.data["question"]
    
    def _search():
        query_vec = embed_texts([question])[0]
        return QdrantStorage().search(query_vec, top_k=5)

    found = await ctx.step.run("embed-and-search", _search)
    
    def _generate_answer():
        context_text = "\n\n".join(found["contexts"])
        if not context_text:
            return "No relevant context found."

        response = openai_client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Answer the user's question using the context provided."},
                {"role": "user", "content": f"Context:\n{context_text}\n\nQuestion: {question}"}
            ],
            temperature=0.2
        )
        return response.choices[0].message.content

    answer = await ctx.step.run("generate-answer", _generate_answer)
    return {"answer": answer, "sources": found["sources"]}


app = FastAPI()

# --- INSTANT CHAT ENDPOINT (FOR UI) ---
class ChatRequest(BaseModel):
    question: str

@app.post("/api/chat")
async def chat_endpoint(request: ChatRequest):
    try:
        # 1. Search Vector DB
        query_vec = embed_texts([request.question])[0]
        found = QdrantStorage().search(query_vec, top_k=5)
        
        context_text = "\n\n".join(found["contexts"])
        if not context_text:
            return {"answer": "I couldn't find any relevant information in the PDF."}

        # 2. Generate Answer
        response = openai_client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant. Answer using the context provided."},
                {"role": "user", "content": f"Context:\n{context_text}\n\nQuestion: {request.question}"}
            ],
            temperature=0.2
        )
        return {
            "answer": response.choices[0].message.content,
            "sources": found["sources"]
        }
    except Exception as e:
        logging.error(f"Chat Error: {e}")
        return {"answer": "Sorry, an error occurred."}

inngest.fast_api.serve(app, inngest_client, [rag_ingest_pdf, rag_query_pdf_ai])
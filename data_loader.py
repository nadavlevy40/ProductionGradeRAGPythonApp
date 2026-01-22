from openai import OpenAI
from llama_index.readers.file import PDFReader
from llama_index.core.node_parser import SentenceSplitter
from dotenv import load_dotenv
import pdfplumber

load_dotenv()

client = OpenAI()
EMBED_MODEL = "text-embedding-3-large"
EMBED_DIM = 3072

splitter = SentenceSplitter(chunk_size=1000, chunk_overlap=200)

def load_and_chunk_pdf(pdf_path: str, chunk_size: int = 1000, overlap: int = 200) -> list[str]:
    text_content = ""
    
    # Use pdfplumber for better Hebrew/Unicode support
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text_content += page_text + "\n"

    # If extraction failed (still empty), return empty list
    if not text_content.strip():
        print(f"WARNING: No text extracted from {pdf_path}. Is it a scanned image?")
        return []

    # Simple character-based chunking
    chunks = []
    start = 0
    text_len = len(text_content)

    while start < text_len:
        end = start + chunk_size
        chunk = text_content[start:end]
        chunks.append(chunk)
        # Move forward, subtracting overlap to keep context
        start += chunk_size - overlap
    
    return chunks


def embed_texts(texts: list[str]) -> list[list[float]]:
    response = client.embeddings.create(
        model=EMBED_MODEL,
        input=texts,
    )
    return [item.embedding for item in response.data]
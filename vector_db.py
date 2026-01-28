from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance, PointStruct

# --- CRITICAL: Global Client to keep data in memory ---
global_client = QdrantClient(":memory:")

class QdrantStorage:
    def __init__(self, collection="docs", dim=3072):
        self.client = global_client
        self.collection = collection
        
        if not self.client.collection_exists(self.collection):
            self.client.create_collection(
                collection_name=self.collection,
                vectors_config=VectorParams(size=dim, distance=Distance.COSINE),
            )

    def upsert(self, ids, vectors, payloads):
        points = [
            PointStruct(id=ids[i], vector=vectors[i], payload=payloads[i]) 
            for i in range(len(ids))
        ]
        self.client.upsert(self.collection, points=points)

    def search(self, query_vector, top_k: int = 5):
        # Using the new query_points API
        result = self.client.query_points(
            collection_name=self.collection,
            query=query_vector,
            with_payload=True,
            limit=top_k
        )
        
        # Extract text and sources cleanly
        contexts = [p.payload.get("text", "") for p in result.points]
        sources = list(set(p.payload.get("source", "") for p in result.points))

        return {"contexts": contexts, "sources": sources}
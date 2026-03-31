from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance, PointStruct
from retriva.config import settings
from retriva.domain.models import Chunk
from retriva.indexing.embeddings import get_embeddings
from typing import List

COLLECTION_NAME = "retriva_chunks"

def get_client() -> QdrantClient:
    return QdrantClient(url=settings.qdrant_url)

def init_collection(client: QdrantClient, vector_size: int = 1536):
    if not client.collection_exists(COLLECTION_NAME):
        client.create_collection(
            collection_name=COLLECTION_NAME,
            vectors_config=VectorParams(size=vector_size, distance=Distance.COSINE),
        )

def upsert_chunks(client: QdrantClient, chunks: List[Chunk]):
    if not chunks:
        return
        
    texts = [c.text for c in chunks]
    embeddings = get_embeddings(texts)
    
    points = [
        PointStruct(
            id=c.metadata.chunk_id,
            vector=embedding,
            payload={
                "text": c.text,
                **c.metadata.model_dump()
            }
        )
        for c, embedding in zip(chunks, embeddings)
    ]
    
    client.upsert(
        collection_name=COLLECTION_NAME,
        points=points
    )

def search_chunks(client: QdrantClient, query_vector: List[float], top_k: int = 5) -> List[dict]:
    results = client.search(
        collection_name=COLLECTION_NAME,
        query_vector=query_vector,
        limit=top_k
    )
    return [hit.payload for hit in results]

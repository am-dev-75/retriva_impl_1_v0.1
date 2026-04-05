from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance, PointStruct
from retriva.config import settings
from retriva.domain.models import Chunk
from retriva.indexing.embeddings import get_embeddings
from retriva.logger import get_logger
from typing import List

logger = get_logger(__name__)

COLLECTION_NAME = "retriva_chunks"

def get_client() -> QdrantClient:
    return QdrantClient(url=settings.qdrant_url)

def init_collection(client: QdrantClient, vector_size: int = None):
    if vector_size is None:
        vector_size = settings.embedding_dimension
        
    if not client.collection_exists(COLLECTION_NAME):
        logger.info(f"Creating collection '{COLLECTION_NAME}' with dimension {vector_size}...")
        client.create_collection(
            collection_name=COLLECTION_NAME,
            vectors_config=VectorParams(size=vector_size, distance=Distance.COSINE),
        )
    else:
        logger.debug(f"Collection '{COLLECTION_NAME}' already exists.")

def upsert_chunks(client: QdrantClient, chunks: List[Chunk]):
    if not chunks:
        return
        
    logger.info(f"Indexing {len(chunks)} chunks in batches of {settings.indexing_batch_size}...")
    
    for i in range(0, len(chunks), settings.indexing_batch_size):
        batch_chunks = chunks[i : i + settings.indexing_batch_size]
        texts = [c.text for c in batch_chunks]
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
            for c, embedding in zip(batch_chunks, embeddings)
        ]
        
        logger.debug(f"Upserting batch {i//settings.indexing_batch_size + 1} ({len(points)} points) to '{COLLECTION_NAME}'...")
        client.upsert(
            collection_name=COLLECTION_NAME,
            points=points
        )

def search_chunks(client: QdrantClient, query_vector: List[float], top_k: int = 5) -> List[dict]:
    logger.debug(f"Searching top_{top_k} chunks in '{COLLECTION_NAME}'...")
    results = client.search(
        collection_name=COLLECTION_NAME,
        query_vector=query_vector,
        limit=top_k
    )
    return [hit.payload for hit in results]

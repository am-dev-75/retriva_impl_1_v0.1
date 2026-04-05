from retriva.indexing.embeddings import get_embeddings
from retriva.indexing.qdrant_store import get_client, search_chunks
from retriva.logger import get_logger
from typing import List, Dict

logger = get_logger(__name__)

def retrieve_top_chunks(query: str, top_k: int = 5) -> List[Dict]:
    logger.debug(f"Retrieving top_{top_k} chunks for query...")
    embeddings = get_embeddings([query])
    query_vector = embeddings[0]
    
    client = get_client()
    results = search_chunks(client, query_vector, top_k=top_k)
    return results

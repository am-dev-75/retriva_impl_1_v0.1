from retriva.indexing.embeddings import get_embeddings
from retriva.indexing.qdrant_store import get_client, search_chunks
from typing import List, Dict

def retrieve_top_chunks(query: str, top_k: int = 5) -> List[Dict]:
    """
    Given a query, computes its embedding and retrieves the top-k chunks from Qdrant.
    """
    embeddings = get_embeddings([query])
    query_vector = embeddings[0]
    
    client = get_client()
    results = search_chunks(client, query_vector, top_k=top_k)
    return results

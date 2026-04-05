from openai import OpenAI
from retriva.config import settings
from retriva.logger import get_logger
from typing import List

logger = get_logger(__name__)

def get_embeddings(texts: List[str]) -> List[List[float]]:
    if not texts:
        return []
        
    logger.debug(f"Creating embeddings for {len(texts)} texts in batches of {settings.indexing_batch_size}...")
    client = OpenAI(
        api_key=settings.openai_api_key,
        base_url=settings.openai_base_url
    )
    
    all_embeddings = []
    for i in range(0, len(texts), settings.indexing_batch_size):
        batch = texts[i : i + settings.indexing_batch_size]
        response = client.embeddings.create(
            input=batch,
            model=settings.embedding_model
        )
        all_embeddings.extend([data.embedding for data in response.data])
    
    return all_embeddings

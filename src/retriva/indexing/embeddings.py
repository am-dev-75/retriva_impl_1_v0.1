from openai import OpenAI
from retriva.config import settings
from retriva.logger import get_logger
from typing import List

logger = get_logger(__name__)

def get_embeddings(texts: List[str]) -> List[List[float]]:
    logger.debug(f"Creating embeddings for {len(texts)} texts...")
    client = OpenAI(
        api_key=settings.openai_api_key,
        base_url=settings.openai_base_url
    )
    
    response = client.embeddings.create(
        input=texts,
        model=settings.embedding_model
    )
    
    return [data.embedding for data in response.data]

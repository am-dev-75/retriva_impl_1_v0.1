from openai import OpenAI
from retriva.config import settings
from typing import List

def get_embeddings(texts: List[str]) -> List[List[float]]:
    client = OpenAI(
        api_key=settings.openai_api_key,
        base_url=settings.openai_base_url
    )
    
    response = client.embeddings.create(
        input=texts,
        model=settings.embedding_model
    )
    
    return [data.embedding for data in response.data]

from openai import OpenAI
from retriva.config import settings
from retriva.qa.retriever import retrieve_top_chunks
from retriva.qa.prompting import build_prompt
from retriva.logger import get_logger

logger = get_logger(__name__)

def ask_question(question: str, top_k: int = 5) -> dict:
    """
    Full QA pipeline: Retrieve, Prompt, Generate Chat
    """
    logger.info(f"Processing question: {question}")
    chunks = retrieve_top_chunks(question, top_k=top_k)
    logger.info(f"Retrieved {len(chunks)} chunks for context.")
    
    system_prompt = build_prompt(question, chunks)
    
    client = OpenAI(
        api_key=settings.openai_api_key,
        base_url=settings.openai_base_url
    )
    
    response = client.chat.completions.create(
        model=settings.chat_model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": question}
        ],
        temperature=0.0
    )
    
    return {
        "answer": response.choices[0].message.content,
        "retrieved_chunks": chunks
    }

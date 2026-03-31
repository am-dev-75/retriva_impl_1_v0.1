from typing import List, Dict

def build_prompt(question: str, retrieved_chunks: List[Dict]) -> str:
    """
    Builds the grounded system prompt and user query safely formatted.
    """
    context_str = ""
    for idx, chunk in enumerate(retrieved_chunks):
        title = chunk.get("page_title", "Unknown Page")
        url = chunk.get("canonical_doc_id", "Unknown URL")
        text = chunk.get("text", "")
        # Add a clear citation block
        context_str += f"\n--- Document {idx+1} | Source: {title} ({url}) ---\n{text}\n"
        
    system_prompt = f"""You are Retriva, a grounded QA chatbot. Answer the user's question based ONLY on the provided context.
If the context does not contain sufficient evidence to answer the question, you must explicitly refuse by stating:
"I do not have sufficient evidence in my knowledge base to answer this question."

Support your factual claims with citations in the format [Document X].
Maintain language alignment: if the question is in English, reply in English. If it is in Italian, reply in Italian.

CONTEXT:
{context_str}
"""
    return system_prompt

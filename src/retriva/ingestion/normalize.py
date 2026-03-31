import re

def normalize_text(text: str) -> str:
    """
    Cleans up whitespace and standardizes newlines over parsed text.
    """
    text = re.sub(r'[ \t]+', ' ', text)
    text = re.sub(r'\n\s*\n', '\n\n', text)
    return text.strip()

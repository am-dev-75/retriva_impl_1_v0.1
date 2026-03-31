from bs4 import BeautifulSoup
from typing import Optional
from retriva.ingestion.normalize import normalize_text

def extract_main_content(html: str) -> Optional[str]:
    """
    Extracts the main content using mirror-contract selectors
    and removes boilerplate elements.
    """
    soup = BeautifulSoup(html, "html.parser")
    
    for element in soup(["nav", "footer", "script", "style", "aside", "header"]):
        element.decompose()
        
    selectors = ["#content", "#mw-content-text", "main", ".mw-parser-output"]
    target_node = None
    
    for selector in selectors:
        nodes = soup.select(selector)
        if nodes:
            target_node = nodes[0]
            break
            
    if target_node is None:
        target_node = soup.body
        if target_node is None:
            return None
            
    raw_text = target_node.get_text(separator="\n")
    return normalize_text(raw_text)

def extract_title(html: str) -> str:
    soup = BeautifulSoup(html, "html.parser")
    if soup.title and soup.title.string:
        return soup.title.string.strip()
    return ""

from bs4 import BeautifulSoup
from typing import Optional
from retriva.ingestion.normalize import normalize_text
from retriva.logger import get_logger

logger = get_logger(__name__)

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
            logger.debug(f"Content extracted using selector: {selector}")
            break
            
    if target_node is None:
        target_node = soup.body
        if target_node is None:
            logger.warning("Could not find any content or body in HTML.")
            return None
        logger.debug("Content extracted using fallback: <body>")
            
    raw_text = target_node.get_text(separator="\n")
    return normalize_text(raw_text)

def extract_title(html: str) -> str:
    soup = BeautifulSoup(html, "html.parser")
    if soup.title and soup.title.string:
        return soup.title.string.strip()
    return ""

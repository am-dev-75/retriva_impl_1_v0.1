import os
from pathlib import Path
from typing import List
from retriva.config import settings

def discover_html_files() -> List[str]:
    """
    Discovers all HTML files in the local wget mirror folder.
    """
    base = Path(settings.mirror_base_path).resolve()
    if not base.exists() or not base.is_dir():
        return []
        
    valid_exts = {".html", ".htm"}
    files = []
    
    for root, _, filenames in os.walk(base):
        for name in filenames:
            ext = os.path.splitext(name)[1].lower()
            if ext in valid_exts:
                files.append(os.path.join(root, name))
                
    return files

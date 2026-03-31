import hashlib
from typing import List
from retriva.domain.models import Chunk, ChunkMetadata, ParsedDocument

def create_chunks(document: ParsedDocument) -> List[Chunk]:
    """
    Splits the parsed document text into paragraph-level chunks.
    Assumes section details could be augmented later if needed.
    """
    paragraphs = [p.strip() for p in document.content_text.split("\n\n") if p.strip()]
    
    chunks = []
    for idx, para in enumerate(paragraphs):
        chunk_id = hashlib.md5(f"{document.doc_id}_{idx}".encode("utf-8")).hexdigest()
        
        meta = ChunkMetadata(
            doc_id=document.doc_id,
            source_path=document.source_path,
            page_title=document.page_title,
            section_path="", 
            chunk_id=chunk_id,
            chunk_index=idx,
            chunk_type="text",
            language="en"
        )
        
        chunk = Chunk(text=para, metadata=meta)
        chunks.append(chunk)
        
    document.chunks = chunks
    return chunks

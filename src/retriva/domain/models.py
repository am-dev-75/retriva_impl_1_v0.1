from pydantic import BaseModel, Field
from typing import List

class ChunkMetadata(BaseModel):
    doc_id: str
    source_path: str
    page_title: str
    section_path: str
    chunk_id: str
    chunk_index: int
    chunk_type: str = "text"
    language: str = "en"

class Chunk(BaseModel):
    text: str
    metadata: ChunkMetadata

class ParsedDocument(BaseModel):
    source_path: str
    canonical_doc_id: str
    page_title: str
    content_text: str
    chunks: List[Chunk] = Field(default_factory=list)

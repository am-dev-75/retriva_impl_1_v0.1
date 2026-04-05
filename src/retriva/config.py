# Copyright (C) 2026 Andrea Marson (am.dev.75@gmail.com)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    mirror_base_path: str = "./mirror"
    canonical_base_url: str = "https://wiki.dave.eu"
    
    qdrant_url: str = "http://192.168.1.64:6333"
    openai_api_key: str = "sk-mock-key"
    openai_base_url: str = "http://192.168.1.64:8000/v1"
    
    #embedding_model: str = "text-embedding-3-small"
    embedding_model: str = "ibm-granite/granite-embedding-english-r2"
    embedding_dimension: int = 768
    #chat_model: str = "gpt-4o-mini"
    # Chunking
    max_chunk_chars: int = 12000
    chunk_overlap: int = 500
    indexing_batch_size: int = 50
    
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

settings = Settings()

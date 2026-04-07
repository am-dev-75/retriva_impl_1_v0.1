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

from openai import OpenAI
from retriva.config import settings
from retriva.logger import get_logger
from typing import List

logger = get_logger(__name__)

def get_embeddings(texts: List[str]) -> List[List[float]]:
    if not texts:
        return []
        
    logger.debug(f"Creating embeddings for {len(texts)} texts in batches of {settings.indexing_batch_size}...")
    client = OpenAI(
        api_key=settings.embedding_openai_api_key,
        base_url=settings.embedding_base_url
    )
    
    all_embeddings = []
    for i in range(0, len(texts), settings.indexing_batch_size):
        batch = texts[i : i + settings.indexing_batch_size]
        response = client.embeddings.create(
            input=batch,
            model=settings.embedding_model
        )
        all_embeddings.extend([data.embedding for data in response.data])
    
    return all_embeddings

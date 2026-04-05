from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    mirror_base_path: str = "./mirror"
    canonical_base_url: str = "https://wiki.dave.eu"
    
    qdrant_url: str = "http://192.168.1.64:6333"
    openai_api_key: str = "sk-mock-key"
    openai_base_url: str = "http://192.168.1.64:8000/v1"
    
    #embedding_model: str = "text-embedding-3-small"
    embedding_model: str = "Qwen/Qwen3-0.6B"
    #chat_model: str = "gpt-4o-mini"
    chat_model: str = "Qwen/Qwen3-0.6B"
    
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

settings = Settings()

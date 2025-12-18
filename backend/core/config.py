# from pydantic_settings import BaseSettings, SettingsConfigDict

# class Settings(BaseSettings):
#     OPENAI_API_KEY: str
#     QDRANT_URL: str
#     QDRANT_API_KEY: str
#     COHERE_API_KEY: str

#     model_config = SettingsConfigDict(env_file=".env", extra="ignore")

# settings = Settings()
from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
ENV_FILE = BASE_DIR / ".env"

class Settings(BaseSettings):
    OPENAI_API_KEY: str
    QDRANT_URL: str
    QDRANT_API_KEY: str | None = None
    COHERE_API_KEY: str

    model_config = SettingsConfigDict(
        env_file=ENV_FILE,
        extra="ignore"
    )

settings = Settings()

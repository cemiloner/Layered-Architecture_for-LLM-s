import os
from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent

#env i dev de unutma !
app_env = os.getenv("APP_ENV", "development")
env_path = ROOT_DIR / "envs" / f".env.{app_env}"

if env_path.exists():
    load_dotenv(dotenv_path=env_path)
    print(f"Yüklenen ortam dosyası: {env_path}")
else:
    load_dotenv(ROOT_DIR / ".env")
    print("Varsayılan .env dosyası kullanılıyor.")

class Settings(BaseSettings):
    APP_ENV: str = "development"
    APP_PORT: int = 8000
    SECRET_KEY: str
    REDIS_URL: str
    OLLAMA_BASE_URL: str = "http://localhost:11434"
    DEFAULT_MODEL: str = "llama3"
    OPENAI_API_KEY: str = ""
    MODERATION_THRESHOLD: float = 0.85
    ENABLE_PROMPT_SANITIZATION: bool = True
    SANITIZER_MODEL: str = "qwen2.5:0.5b"
    model_config = SettingsConfigDict(
        env_file=str(env_path) if env_path.exists() else ".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )

settings = Settings()
from pydantic_settings import BaseSettings, SettingsConfigDict
import os


class Settings(BaseSettings):

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True
    )

    DATABASE_URL: str
    DEBUG_MODE: bool = False  # Valor por defecto si no se encuentra en .env
    API_VERSION: str = "v1"


settings = Settings()

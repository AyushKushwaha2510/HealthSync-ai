from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str = "health-sync-ai"
    ENV: str = "development"
    PORT: int = 8000

    GEMINI_API_KEY: str
    GEMINI_MODEL: str

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True,
    )

    DATABASE_URL:str


settings = Settings()
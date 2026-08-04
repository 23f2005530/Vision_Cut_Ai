from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str = "Vision Cut AI"
    APP_VERSION: str = "0.1.0"

    GEMINI_API_KEY: str = ""

    DEFAULT_LANGUAGE: str = "en"

    LOG_LEVEL: str = "INFO"

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True,
    )


settings = Settings()

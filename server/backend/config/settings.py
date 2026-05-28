from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    GEMINI_API_KEY: str

    TAVILY_API_KEY: str

    MAX_REVISIONS: int = 2

    MAX_RESEARCHERS: int = 3

    REQUEST_TIMEOUT: int = 30

    APP_USERNAME: str

    APP_PASSWORD: str

    class Config:

        env_file = ".env"
        env_file_encoding = "utf-8"
        # When running in Docker, env vars are injected directly
        # by docker-compose env_file — .env file is optional
        extra = "ignore"


settings = Settings()
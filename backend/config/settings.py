from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    GEMINI_API_KEY: str

    TAVILY_API_KEY: str

    MAX_REVISIONS: int = 2

    MAX_RESEARCHERS: int = 3

    REQUEST_TIMEOUT: int = 30

    class Config:

        env_file = ".env"


settings = Settings()
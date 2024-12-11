from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    Application Settings
    """
    # generate by using `openssl rand -hex 32`
    SECRET_KEY: str = "YOUR_SECRET_KEY"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    DATABASE_URL: str
    DATABASE_NAME: str

    BROKER_URL: str
    BACKEND_URL: str

    class Config:
        """
        Load environment variables from .env file
        """
        env_file = ".env"


settings = Settings()

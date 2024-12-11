from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # generate by using `openssl rand -hex 32`
    SECRET_KEY: str = "94c6b79390776e036f2af3bae12b10efc2687175f0df4dde4718132a1f3117dd"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30


settings = Settings()

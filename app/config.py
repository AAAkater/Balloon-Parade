from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    BALLOON_HOST: str
    BALLOON_PORT: int

    class Config:
        env_file: str = ".env"


setting = Settings()

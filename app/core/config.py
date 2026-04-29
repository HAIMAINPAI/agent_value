from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    app_name: str = "AI选品 + 利润测算 Agent"
    database_url: str = "sqlite:///./agent.db"
    debug: bool = True


settings = Settings()

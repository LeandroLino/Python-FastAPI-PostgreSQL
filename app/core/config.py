from pydantic_settings import BaseSettings
from typing import Optional
import os

class Settings(BaseSettings):
    database_url: str = "postgresql://fastapi_user:fastapi_password@db:5432/fastapi_db"
    api_version: str = "1.0.0"
    debug: bool = True
    testing: bool = False
    
    class Config:
        env_file = ".env"

    def get_database_url(self):
        """Retorna URL do banco baseada no ambiente"""
        if self.testing or os.getenv("TESTING"):
            return "sqlite:///./test.db"
        return self.database_url

settings = Settings()
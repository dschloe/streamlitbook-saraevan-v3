from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    app_name: str = "Bank Marketing Prediction API"
    model_path: str = "models/bank_marketing_model.joblib"
    api_v1_prefix: str = "/api/v1"
    
    class Config:
        env_file = ".env"

@lru_cache()
def get_settings():
    return Settings() 
from pydantic import BaseModel
from typing import Optional, List

class PredictionRequest(BaseModel):
    age: int
    job: str
    marital: str
    education: str
    default: str
    balance: int
    housing: str
    loan: str
    contact: str
    day: int
    month: str
    duration: int
    campaign: int
    pdays: int
    previous: int
    poutcome: str

class PredictionResponse(BaseModel):
    prediction: bool
    probability: float
    
class ModelInfo(BaseModel):
    version: str
    features: List[str]
    accuracy: float
    precision: float
    recall: float
    f1_score: float
    roc_auc: float 
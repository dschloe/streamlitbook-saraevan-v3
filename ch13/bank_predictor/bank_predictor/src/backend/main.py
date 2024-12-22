from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd
from src.models.model import BankMarketingModel

app = FastAPI(title="Bank Marketing Prediction API")

# Load the model at startup
try:
    model = BankMarketingModel.load(
        model_path='models/bank_marketing_model.joblib',
        preprocessor_path='models/bank_marketing_preprocessor.joblib'
    )
except Exception as e:
    print(f"Warning: Failed to load model - {str(e)}")
    model = None

class PredictionInput(BaseModel):
    age: int
    job: str
    marital: str
    education: str
    default: str
    balance: float
    housing: str
    loan: str
    contact: str
    duration: int
    campaign: int
    pdays: int
    previous: int
    poutcome: str

class PredictionOutput(BaseModel):
    prediction: bool
    probability: float

@app.post("/predict", response_model=PredictionOutput)
async def predict(input_data: PredictionInput):
    try:
        # Convert input to DataFrame
        input_df = pd.DataFrame([input_data.dict()])
        
        # Make prediction
        prediction = model.predict(input_df)[0]
        probability = model.predict_proba(input_df)[0][1]
        
        return PredictionOutput(
            prediction=bool(prediction),
            probability=float(probability)
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"} 
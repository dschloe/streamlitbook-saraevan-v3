from fastapi import APIRouter, Depends
from ..schemas import PredictionRequest, PredictionResponse, ModelInfo
from ..ml.model import BankMarketingModel
from ..config import get_settings, Settings

router = APIRouter()
model = None

def get_model(settings: Settings = Depends(get_settings)) -> BankMarketingModel:
    global model
    if model is None:
        model = BankMarketingModel(settings.model_path)
    return model

@router.post("/predict", response_model=PredictionResponse)
async def predict(request: PredictionRequest, model: BankMarketingModel = Depends(get_model)):
    prediction, probability = model.predict(request.dict())
    return PredictionResponse(prediction=prediction, probability=probability)

@router.get("/model-info", response_model=ModelInfo)
async def get_model_info(model: BankMarketingModel = Depends(get_model)):
    return ModelInfo(**model.get_model_info()) 
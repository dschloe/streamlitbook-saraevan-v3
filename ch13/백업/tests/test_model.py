import pytest
import pandas as pd
import numpy as np
from src.models.model import BankMarketingModel

@pytest.fixture
def sample_data():
    return pd.DataFrame({
        'age': [30, 40, 50],
        'job': ['admin.', 'technician', 'retired'],
        'marital': ['married', 'single', 'divorced'],
        'education': ['tertiary', 'secondary', 'primary'],
        'default': ['no', 'no', 'no'],
        'balance': [1000, 2000, 3000],
        'housing': ['yes', 'no', 'yes'],
        'loan': ['no', 'yes', 'no'],
        'contact': ['cellular', 'telephone', 'cellular'],
        'duration': [100, 200, 300],
        'campaign': [1, 2, 3],
        'pdays': [-1, 10, -1],
        'previous': [0, 1, 2],
        'poutcome': ['unknown', 'success', 'failure']
    })

def test_model_initialization():
    model = BankMarketingModel()
    assert model is not None
    assert model.preprocessor is not None
    assert model.model is not None

def test_model_fit_predict(sample_data):
    # Create synthetic target
    y = np.random.randint(0, 2, size=len(sample_data))
    
    # Initialize and fit model
    model = BankMarketingModel()
    model.fit(sample_data, y)
    
    # Make predictions
    predictions = model.predict(sample_data)
    probabilities = model.predict_proba(sample_data)
    
    # Basic assertions
    assert len(predictions) == len(sample_data)
    assert probabilities.shape == (len(sample_data), 2)
    assert all(isinstance(p, (np.int64, bool)) for p in predictions)
    assert all(0 <= p <= 1 for p in probabilities.flatten()) 
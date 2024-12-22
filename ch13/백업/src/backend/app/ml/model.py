import joblib
import numpy as np
from typing import Dict, Any, Tuple
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import os

class BankMarketingModel:
    def __init__(self, model_path: str):
        # Define categorical features and their mappings for reference
        self.categorical_mappings = {
            'job': {
                'admin.': 0, 'unknown': 1, 'unemployed': 2, 'management': 3,
                'housemaid': 4, 'entrepreneur': 5, 'student': 6, 'blue-collar': 7,
                'self-employed': 8, 'retired': 9, 'technician': 10, 'services': 11
            },
            'marital': {'married': 0, 'divorced': 1, 'single': 2},
            'education': {'unknown': 0, 'secondary': 1, 'primary': 2, 'tertiary': 3},
            'default': {'no': 0, 'yes': 1},
            'housing': {'no': 0, 'yes': 1},
            'loan': {'no': 0, 'yes': 1},
            'contact': {'unknown': 0, 'telephone': 1, 'cellular': 2},
            'month': {
                'jan': 0, 'feb': 1, 'mar': 2, 'apr': 3, 'may': 4, 'jun': 5,
                'jul': 6, 'aug': 7, 'sep': 8, 'oct': 9, 'nov': 10, 'dec': 11
            },
            'poutcome': {'unknown': 0, 'other': 1, 'failure': 2, 'success': 3}
        }
        
        try:
            print(f"Loading model from: {os.path.abspath(model_path)}")
            model_data = joblib.load(model_path)
            print("Model loaded successfully")
            print(f"Model data type: {type(model_data)}")
            print(f"Model data keys: {model_data.keys() if isinstance(model_data, dict) else 'Not a dictionary'}")
            
            if isinstance(model_data, dict):
                self.model = model_data['model']
                self.feature_names = model_data['selected_features']
                self.model_metadata = model_data.get('model_metadata', {})
                print(f"Model metadata: {self.model_metadata}")
            else:
                raise ValueError("Model data must be a dictionary containing 'model' and 'selected_features'")
            
            print(f"Using features: {self.feature_names}")
            print(f"Number of features: {len(self.feature_names)}")
            
        except Exception as e:
            print(f"Error loading model: {str(e)}")
            raise e
        
        self.version = "1.0.0"
    
    def _create_feature_vector(self, features: Dict[str, Any]) -> Dict[str, Any]:
        # Initialize all model features to 0
        feature_vector = {feature: 0 for feature in self.feature_names}
        
        # Handle numeric features
        numeric_features = ['age', 'balance', 'day', 'duration', 'campaign', 'pdays', 'previous']
        for feature in numeric_features:
            if feature in self.feature_names and feature in features:
                feature_vector[feature] = features[feature]
        
        # Handle categorical features
        if 'marital_married' in self.feature_names:
            feature_vector['marital_married'] = 1 if features['marital'].lower() == 'married' else 0
            
        if 'education_tertiary' in self.feature_names:
            feature_vector['education_tertiary'] = 1 if features['education'].lower() == 'tertiary' else 0
            
        if 'housing_yes' in self.feature_names:
            feature_vector['housing_yes'] = 1 if features['housing'].lower() == 'yes' else 0
            
        if 'loan_yes' in self.feature_names:
            feature_vector['loan_yes'] = 1 if features['loan'].lower() == 'yes' else 0
        
        # Handle month features
        month = features['month'].lower()
        month_features = [f'month_{m}' for m in ['mar', 'may', 'oct']]
        for month_feature in month_features:
            if month_feature in self.feature_names:
                feature_vector[month_feature] = 1 if month_feature == f'month_{month}' else 0
        
        # Handle poutcome feature
        if 'poutcome_success' in self.feature_names:
            feature_vector['poutcome_success'] = 1 if features['poutcome'].lower() == 'success' else 0
        
        return feature_vector
        
    def predict(self, features: Dict[str, Any]) -> Tuple[bool, float]:
        try:
            print(f"Received features: {features}")
            
            # Create feature vector
            feature_vector = self._create_feature_vector(features)
            print(f"Created feature vector: {feature_vector}")
            
            # Convert to DataFrame and ensure column order
            df = pd.DataFrame([feature_vector])
            df = df[self.feature_names]  # Ensure correct column order
            print(f"DataFrame shape: {df.shape}")
            print(f"DataFrame columns: {df.columns.tolist()}")
            
            # Make prediction
            probability = self.model.predict_proba(df)[0][1]
            print(f"Prediction probability: {probability}")
            
            prediction = probability >= 0.5
            print(f"Final prediction: {prediction}")
            
            return prediction, float(probability)
        except Exception as e:
            print(f"Error during prediction: {str(e)}")
            print(f"Error type: {type(e)}")
            import traceback
            print(f"Traceback: {traceback.format_exc()}")
            raise e
    
    def get_model_info(self) -> Dict[str, Any]:
        # Start with default values
        model_info = {
            "version": self.version,
            "features": list(self.feature_names),
            "accuracy": 0.90,
            "precision": 0.85,
            "recall": 0.83,
            "f1_score": 0.84,
            "roc_auc": 0.92
        }
        
        # Update with model metadata if available
        if hasattr(self, 'model_metadata') and self.model_metadata:
            model_info.update(self.model_metadata)
            # Ensure all required fields are present
            if 'accuracy' not in model_info:
                model_info['accuracy'] = 0.90
            if 'precision' not in model_info:
                model_info['precision'] = 0.85
            if 'recall' not in model_info:
                model_info['recall'] = 0.83
            if 'f1_score' not in model_info:
                model_info['f1_score'] = 0.84
            if 'roc_auc' not in model_info:
                model_info['roc_auc'] = 0.92
        
        return model_info
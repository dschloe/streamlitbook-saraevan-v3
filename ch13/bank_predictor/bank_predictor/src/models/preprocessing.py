import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import StandardScaler, LabelEncoder

class BankDataPreprocessor(BaseEstimator, TransformerMixin):
    def __init__(self):
        self.label_encoders = {}
        self.scaler = StandardScaler()
        
    def fit(self, X, y=None):
        # Initialize label encoders for categorical columns
        categorical_columns = X.select_dtypes(include=['object']).columns
        for column in categorical_columns:
            self.label_encoders[column] = LabelEncoder()
            self.label_encoders[column].fit(X[column])
        
        # Fit scaler for numerical columns
        numerical_columns = X.select_dtypes(include=['int64', 'float64']).columns
        self.scaler.fit(X[numerical_columns])
        
        return self
        
    def transform(self, X):
        X_transformed = X.copy()
        
        # Transform categorical columns
        for column, encoder in self.label_encoders.items():
            X_transformed[column] = encoder.transform(X_transformed[column])
        
        # Transform numerical columns
        numerical_columns = X.select_dtypes(include=['int64', 'float64']).columns
        X_transformed[numerical_columns] = self.scaler.transform(X_transformed[numerical_columns])
        
        return X_transformed 
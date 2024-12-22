import joblib
from sklearn.ensemble import RandomForestClassifier
from .preprocessing import BankDataPreprocessor

class BankMarketingModel:
    def __init__(self):
        self.preprocessor = BankDataPreprocessor()
        self.model = RandomForestClassifier(
            n_estimators=100,
            max_depth=10,
            random_state=42
        )
        
    def fit(self, X, y):
        # Preprocess the data
        X_transformed = self.preprocessor.fit_transform(X)
        
        # Train the model
        self.model.fit(X_transformed, y)
        return self
        
    def predict(self, X):
        # Preprocess the data
        X_transformed = self.preprocessor.transform(X)
        
        # Make predictions
        return self.model.predict(X_transformed)
        
    def predict_proba(self, X):
        # Preprocess the data
        X_transformed = self.preprocessor.transform(X)
        
        # Make probability predictions
        return self.model.predict_proba(X_transformed)
        
    def save(self, model_path, preprocessor_path):
        # Save the model and preprocessor
        joblib.dump(self.model, model_path)
        joblib.dump(self.preprocessor, preprocessor_path)
        
    @classmethod
    def load(cls, model_path, preprocessor_path):
        instance = cls()
        instance.model = joblib.load(model_path)
        instance.preprocessor = joblib.load(preprocessor_path)
        return instance 
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import joblib
import os
from model import BankMarketingModel

def load_data(data_path):
    """데이터를 로드하고 전처리합니다."""
    # 데이터 로드
    df = pd.read_csv(data_path, sep=';')
    
    # 목표변수 변환 (yes/no -> 1/0)
    df['y'] = (df['y'] == 'yes').astype(int)
    
    # 특성과 목표변수 분리
    X = df.drop('y', axis=1)
    y = df['y']
    
    return X, y

def evaluate_model(model, X_test, y_test):
    """모델 성능을 평가합니다."""
    # 예측
    y_pred = model.predict(X_test)
    
    # 성능 지표 계산
    metrics = {
        'accuracy': accuracy_score(y_test, y_pred),
        'precision': precision_score(y_test, y_pred),
        'recall': recall_score(y_test, y_pred),
        'f1': f1_score(y_test, y_pred)
    }
    
    return metrics

def main():
    # 데이터 로드
    data_path = 'data/bank/bank.csv'
    X, y = load_data(data_path)
    
    # 학습/테스트 데이터 분할
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    # 모델 초기화 및 학습
    model = BankMarketingModel()
    model.fit(X_train, y_train)
    
    # 모델 평가
    metrics = evaluate_model(model, X_test, y_test)
    print("\n=== 모델 성능 ===")
    for metric_name, value in metrics.items():
        print(f"{metric_name}: {value:.4f}")
    
    # 모델 저장
    os.makedirs('models', exist_ok=True)
    model.save(
        model_path='models/bank_marketing_model.joblib',
        preprocessor_path='models/bank_marketing_preprocessor.joblib'
    )
    print("\n모델이 저장되었습니다.")

if __name__ == '__main__':
    main() 
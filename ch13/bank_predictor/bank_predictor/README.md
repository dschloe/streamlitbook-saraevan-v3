# Bank Marketing Campaign Success Prediction System

## 프로젝트 개요
은행 마케팅 캠페인의 성공 여부를 예측하는 머신러닝 기반 웹 애플리케이션입니다.

## 시스템 요구사항
- Python 3.9+
- Docker
- Docker Compose

## 설치 방법

1. 저장소 클론
```bash
git clone [repository-url]
cd bank_predictor
```

2. 가상환경 생성 및 활성화
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
.\venv\Scripts\activate  # Windows
```

3. 의존성 설치
```bash
pip install -r requirements.txt
```

## 실행 방법

### 개발 모드
1. Backend 서버 실행
```bash
uvicorn src.backend.main:app --reload
```

2. Frontend 실행
```bash
streamlit run src.frontend.app:main
```

### Docker 실행
```bash
docker-compose up
```

## 프로젝트 구조
```
.
├── data/                # 데이터 파일
├── notebooks/           # 분석 노트북
├── src/
│   ├── frontend/       # Streamlit 앱
│   ├── backend/        # FastAPI 서버
│   └── models/         # ML 모델 관련 코드
├── tests/              # 테스트 코드
└── docker/             # Docker 설정
```

## 테스트 실행
```bash
pytest tests/
``` 
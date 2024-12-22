import streamlit as st
import pandas as pd
import plotly.express as px
import requests
import json
import os

# API 설정
API_URL = os.getenv("BACKEND_URL", "http://backend:8000")
API_V1_PREFIX = "/api/v1"

def get_model_info():
    """모델 정보를 가져옵니다."""
    try:
        response = requests.get(f"{API_URL}{API_V1_PREFIX}/model-info")
        return response.json()
    except Exception as e:
        st.error(f"Error fetching model info: {str(e)}")
        return None

def predict(features):
    """예측을 수행합니다."""
    try:
        response = requests.post(f"{API_URL}{API_V1_PREFIX}/predict", json=features)
        return response.json()
    except Exception as e:
        st.error(f"Error making prediction: {str(e)}")
        return None

def load_sample_data():
    """샘플 데이터를 로드합니다."""
    try:
        # 여러 가능한 경로 시도
        possible_paths = [
            'data/bank/bank.csv',
            '/app/data/bank/bank.csv',
            '../data/bank/bank.csv'
        ]
        
        for path in possible_paths:
            try:
                if os.path.exists(path):
                    df = pd.read_csv(path, sep=';')
                    return df.head()
            except Exception as e:
                continue
                
        st.error("샘플 데이터 파일을 찾을 수 없습니다.")
        return None
    except Exception as e:
        st.error(f"데이터 로딩 중 오류 발생: {str(e)}")
        return None

# 페이지 설정
st.set_page_config(
    page_title="Bank Marketing Predictor",
    page_icon="🏦",
    layout="wide"
)

# 제목
st.title("🏦 은행 마케팅 캠페인 예측 시스템")
st.markdown("---")

# 사이드바 - 모델 정보
with st.sidebar:
    st.header("📊 모델 정보")
    model_info = get_model_info()
    
    if model_info:
        st.metric("모델 버전", model_info['version'])
        st.metric("정확도", f"{model_info['accuracy']:.2%}")
        st.metric("정밀도", f"{model_info['precision']:.2%}")
        st.metric("재현율", f"{model_info['recall']:.2%}")
        st.metric("F1 점수", f"{model_info['f1_score']:.2%}")
        st.metric("ROC-AUC", f"{model_info['roc_auc']:.2%}")
        
        st.markdown("---")
        st.subheader("사용된 특성")
        st.write(model_info['features'])
    else:
        st.error("모델 정보를 불러올 수 없습니다.")

# 메인 컨텐츠
tab1, tab2 = st.tabs(["📝 예측", "📊 데이터 탐색"])

# 예측 탭
with tab1:
    st.header("고객 정보 입력")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.number_input("나이", min_value=18, max_value=100, value=41)
        job = st.selectbox(
            "직업",
            ["admin.", "unknown", "unemployed", "management", "housemaid",
             "entrepreneur", "student", "blue-collar", "self-employed",
             "retired", "technician", "services"]
        )
        marital = st.selectbox("결혼 상태", ["married", "divorced", "single"])
        education = st.selectbox("교육 수준", ["unknown", "secondary", "primary", "tertiary"])
        default = st.selectbox("신용불량 여부", ["no", "yes"])
        
    with col2:
        balance = st.number_input("계좌 잔액 (유로)", value=2343)
        housing = st.selectbox("주택대출 여부", ["no", "yes"])
        loan = st.selectbox("개인대출 여부", ["no", "yes"])
        contact = st.selectbox("연락 방법", ["unknown", "telephone", "cellular"])
        day = st.number_input("마지막 연락 일자", min_value=1, max_value=31, value=15)
        
    with col3:
        month = st.selectbox(
            "마지막 연락 월",
            ["jan", "feb", "mar", "apr", "may", "jun",
             "jul", "aug", "sep", "oct", "nov", "dec"]
        )
        duration = st.number_input("마지막 통화 시간 (초)", min_value=0, value=1042)
        campaign = st.number_input("��번 캠페인 연락 횟수", min_value=1, value=1)
        pdays = st.number_input("이전 캠페인 이후 경과일 (-1: 연락 안됨)", value=-1)
        previous = st.number_input("이전 캠페인 연락 횟수", min_value=0, value=0)
        poutcome = st.selectbox("이전 캠페인 결과", ["unknown", "other", "failure", "success"])
    
    if st.button("예측하기", type="primary"):
        features = {
            "age": age,
            "job": job,
            "marital": marital,
            "education": education,
            "default": default,
            "balance": balance,
            "housing": housing,
            "loan": loan,
            "contact": contact,
            "day": day,
            "month": month,
            "duration": duration,
            "campaign": campaign,
            "pdays": pdays,
            "previous": previous,
            "poutcome": poutcome
        }
        
        result = predict(features)
        
        if result:
            st.markdown("---")
            st.subheader("예측 결과")
            
            col1, col2 = st.columns(2)
            
            with col1:
                if result['prediction']:
                    st.success("✅ 정기 예금 가입 가능성이 높습니다!")
                else:
                    st.error("❌ 정기 예금 가입 가능성이 낮습니다.")
            
            with col2:
                probability = result['probability']
                st.metric("가입 확률", f"{probability:.1%}")
                
                # 게이지 차트
                fig = px.bar(
                    x=[probability], 
                    y=["확률"],
                    orientation='h',
                    range_x=[0, 1],
                    title="가입 확률"
                )
                fig.update_traces(marker_color='rgb(0, 200, 0)')
                st.plotly_chart(fig, use_container_width=True)
        else:
            st.error("예측 중 오류가 발생했습니다.")

# 데이터 탐색 탭
with tab2:
    st.header("샘플 데이터")
    df = load_sample_data()
    if df is not None:
        st.dataframe(df)
        
        st.markdown("---")
        st.subheader("데이터 시각화")
        
        col1, col2 = st.columns(2)
        
        with col1:
            # 나이 분포
            fig = px.histogram(df, x="age", title="고객 나이 분포")
            st.plotly_chart(fig, use_container_width=True)
            
            # 직업별 분포
            job_counts = df['job'].value_counts()
            fig = px.bar(x=job_counts.index, y=job_counts.values, title="직업별 고객 수")
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # 교육 수준별 분포
            education_counts = df['education'].value_counts()
            fig = px.pie(values=education_counts.values, names=education_counts.index, title="교육 수준별 분포")
            st.plotly_chart(fig, use_container_width=True)
            
            # 결혼 상태별 분포
            marital_counts = df['marital'].value_counts()
            fig = px.pie(values=marital_counts.values, names=marital_counts.index, title="결혼 상태별 분포")
            st.plotly_chart(fig, use_container_width=True)
    else:
        st.error("샘플 데이터를 불러올 수 없습니다.") 
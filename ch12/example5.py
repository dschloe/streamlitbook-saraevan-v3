import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

# Set page configuration
st.set_page_config(
    page_title="Data Dashboard",
    page_icon="📊",
    layout="wide"
)

# Add a title and description
st.title("📊 Interactive Data Dashboard")
st.markdown("This is a sample dashboard showing data visualization capabilities.")

# Create sample data
@st.cache_data  # Cache the data to improve performance
def load_data():
    df = pd.DataFrame({
        'Date': pd.date_range(start='2024-01-01', periods=100),
        'Sales': np.random.randint(100, 1000, 100),
        'Category': np.random.choice(['A', 'B', 'C'], 100)
    })
    return df

df = load_data()

# Create two columns for layout
col1, col2 = st.columns(2)

# First column content
with col1:
    st.subheader("Sales Over Time")
    fig1 = px.line(df, x='Date', y='Sales', title='Daily Sales Trend')
    st.plotly_chart(fig1, use_container_width=True)
    
    # Add interactive filter
    selected_category = st.multiselect(
        "Select Categories",
        options=df['Category'].unique(),
        default=df['Category'].unique()
    )

# Second column content
with col2:
    st.subheader("Sales by Category")
    filtered_df = df[df['Category'].isin(selected_category)]
    fig2 = px.bar(filtered_df.groupby('Category')['Sales'].sum().reset_index(), 
                  x='Category', y='Sales',
                  title='Total Sales by Category')
    st.plotly_chart(fig2, use_container_width=True)

# Add some interactive widgets
st.sidebar.header("Dashboard Controls")
date_range = st.sidebar.date_input(
    "Select Date Range",
    value=(df['Date'].min(), df['Date'].max())
)

# Display raw data with pagination
st.subheader("Raw Data")
st.dataframe(df, use_container_width=True)

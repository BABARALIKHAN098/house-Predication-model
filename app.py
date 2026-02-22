import streamlit as st
import pandas as pd
import pickle
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set page config for a premium look
st.set_page_config(
    page_title="House Valuation Pro",
    page_icon="🏠",
    layout="wide"
)

# Custom CSS for premium aesthetics
st.markdown("""
    <style>
    /* Main container styling */
    .main {
        background-color: #f8f9fc;
    }
    
    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background-color: #ffffff;
        border-right: 1px solid #e0e0e0;
    }
    
    /* Title styling */
    .title-text {
        color: #1e3a8a;
        font-family: 'Inter', sans-serif;
        font-weight: 800;
        font-size: 3rem;
        margin-bottom: 0.5rem;
    }
    
    /* Card styling */
    .metric-card {
        background-color: white;
        padding: 1.5rem;
        border-radius: 12px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        border: 1px solid #f1f5f9;
        text-align: center;
    }
    
    /* Prediction result card */
    .prediction-container {
        background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%);
        color: white;
        padding: 3rem;
        border-radius: 20px;
        box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.2);
        text-align: center;
        margin: 2rem 0;
    }
    
    .price-value {
        font-size: 4rem;
        font-weight: 900;
        margin: 1rem 0;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    
    /* Input field labels */
    .stNumberInput label, .stSelectbox label {
        color: #475569 !important;
        font-weight: 600 !important;
    }
    
    /* Tabs styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 24px;
    }
    
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        white-space: pre-wrap;
        background-color: transparent;
        border-radius: 4px 4px 0px 0px;
        gap: 1px;
        padding-top: 10px;
        padding-bottom: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Load data and model
@st.cache_data
def load_data():
    try:
        return pd.read_csv('Data.csv')
    except:
        return None

@st.cache_resource
def load_model():
    try:
        with open('pipe.pkl', 'rb') as f:
            return pickle.load(f)
    except:
        return None

df = load_data()
pipe = load_model()

# Sidebar Inputs
st.sidebar.header("🔧 Property Specifications")
st.sidebar.markdown("Adjust parameters to estimate value")

with st.sidebar:
    st.subheader("📍 Location Distances")
    taxi_dist = st.number_input("Taxi Station (m)", 0, 30000, 8200)
    market_dist = st.number_input("Market (m)", 0, 30000, 11000)
    hospital_dist = st.number_input("Hospital (m)", 0, 30000, 13000)
    
    st.subheader("📐 Dimensions")
    carpet_area = st.number_input("Carpet Area (sqft)", 100, 30000, 1500)
    builtup_area = st.number_input("Built-up Area (sqft)", 100, 40000, 1800)
    
    st.subheader("🏢 Extras")
    parking_type = st.selectbox("Parking Provision", ['Open', 'Not Provided', 'Covered', 'No Parking'])
    city_type = st.selectbox("City Category", ['CAT A', 'CAT B', 'CAT C'])
    rainfall = st.number_input("Avg Rainfall (mm)", -500, 2000, 800)

# Main Content
st.markdown('<h1 class="title-text">House Valuation Pro</h1>', unsafe_allow_html=True)
st.markdown("##### Real Estate Price Prediction Dashboard powered by Machine Learning")

tab1, tab2, tab3 = st.tabs(["💰 Prediction", "📊 Market Insights", "ℹ️ About Model"])

with tab1:
    st.write("---")
    if st.button("🚀 Generate Valuation Report"):
        if pipe:
            input_df = pd.DataFrame({
                'Taxi_dist': [taxi_dist],
                'Market_dist': [market_dist],
                'Hospital_dist': [hospital_dist],
                'Carpet_area': [carpet_area],
                'Builtup_area': [builtup_area],
                'Parking_type': [parking_type],
                'City_type': [city_type],
                'Rainfall': [rainfall]
            })
            
            try:
                prediction = pipe.predict(input_df)[0]
                
                # Display Prediction result
                st.markdown(f"""
                <div class="prediction-container">
                    <h2 style='color: #e2e8f0; margin-bottom: 0;'>Estimated Market Price</h2>
                    <div class="price-value">₹ {prediction:,.2f}</div>
                    <p style='color: #bfdbfe; font-size: 1.1rem;'>Professional appraisal based on neighborhood analytics and property specs.</p>
                </div>
                """, unsafe_allow_html=True)
                
                # Confidence/Context Metrics
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.markdown(f'<div class="metric-card"><strong>Price/sqft</strong><br>₹ {prediction/carpet_area:,.2f}</div>', unsafe_allow_html=True)
                with col2:
                    st.markdown(f'<div class="metric-card"><strong>Efficiency</strong><br>{(carpet_area/builtup_area)*100:.1f}% Carpet</div>', unsafe_allow_html=True)
                with col3:
                    st.markdown(f'<div class="metric-card"><strong>City Tier</strong><br>{city_type}</div>', unsafe_allow_html=True)
                
                st.balloons()
            except Exception as e:
                st.error(f"Error during prediction: {e}")
        else:
            st.error("Model 'pipe.pkl' not found. Please upload the model file.")

with tab2:
    if df is not None:
        st.subheader("Neighborhood Trends")
        col1, col2 = st.columns(2)
        
        with col1:
            fig, ax = plt.subplots(figsize=(8, 5))
            sns.scatterplot(data=df, x='Carpet_area', y='Price_house', hue='City_type', ax=ax)
            ax.set_title("Price vs Area Trends")
            st.pyplot(fig)
            
        with col2:
            fig, ax = plt.subplots(figsize=(8, 5))
            sns.boxplot(data=df, x='Parking_type', y='Price_house', ax=ax)
            ax.set_title("Parking Type Impact on Price")
            st.pyplot(fig)
            
        st.markdown("---")
        st.subheader("Distribution Analysis")
        fig, ax = plt.subplots(figsize=(12, 4))
        sns.histplot(df['Price_house'], kde=True, color='blue', ax=ax)
        ax.set_title("Property Price Distribution")
        st.pyplot(fig)
    else:
        st.info("Upload 'Data.csv' to visualize market trends.")

with tab3:
    st.markdown("""
    ### Model Architecture
    The underlying engine uses a **Scikit-Learn Pipeline** that automates:
    1. **Pre-processing**: Handling missing values and data cleaning.
    2. **Encoding**: Transforming categorical variables like `City_type` and `Parking_type`.
    3. **Estimation**: Advanced regression algorithms to find the line of best fit.
    
    #### Training Data Summary
    - **Dataset Size**: 932 property records
    - **Target Variable**: House Price
    - **Key Features**: Carpet area, built-up area, and distance to amenities.
    """)

# Footer
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("---")
st.markdown("<div style='text-align: center; color: #64748b;'>© 2026 House Valuation Pro | Project ML to Production</div>", unsafe_allow_html=True)

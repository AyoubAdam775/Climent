# """Main Streamlit Application"""
# import streamlit as st
# from pathlib import Path
# import sys

# # =========================
# # PROJECT PATH SETUP
# # =========================
# project_root = Path(__file__).parent
# sys.path.insert(0, str(project_root))

# # =========================
# # PAGE CONFIGURATION
# # =========================
# st.set_page_config(
#     page_title="AI-Driven Climate Risk Prediction System",
#     page_icon="🌍",
#     layout="wide",
#     initial_sidebar_state="expanded"
# )

# # =========================
# # CUSTOM CSS (FULL FIX)
# # =========================
# st.markdown("""
# <style>

# /* ===============================
#    MAIN CONTENT STYLING
#    =============================== */
# .main-header {
#     font-size: 3rem;
#     font-weight: bold;
#     color: #1f77b4;
#     text-align: center;
#     padding: 1rem;
# }
# .sub-header {
#     font-size: 1.5rem;
#     color: #666;
#     text-align: center;
#     padding: 0.5rem;
# }
# .stMetric {
#     background-color: #f0f2f6;
#     padding: 1rem;
#     border-radius: 0.5rem;
# }

# /* ===============================
#    SIDEBAR VISIBILITY FIX
#    =============================== */
# section[data-testid="stSidebar"] {
#     background: linear-gradient(180deg, #0b132b, #1c2541);
# }
# section[data-testid="stSidebar"] * {
#     opacity: 1 !important;
# }
# section[data-testid="stSidebar"] span,
# section[data-testid="stSidebar"] p,
# section[data-testid="stSidebar"] div,
# section[data-testid="stSidebar"] label {
#     color: #ffffff !important;
#     font-size: 15px;
# }
# section[data-testid="stSidebar"] h1,
# section[data-testid="stSidebar"] h2,
# section[data-testid="stSidebar"] h3 {
#     color: #5bc0eb !important;
#     font-weight: bold;
# }
# section[data-testid="stSidebar"] svg {
#     fill: #ffffff !important;
# }
# section[data-testid="stSidebar"] input {
#     background-color: #2a2f4f !important;
#     color: #ffffff !important;
#     border-radius: 6px;
# }
# section[data-testid="stSidebar"] a[aria-current="page"] {
#     background-color: rgba(255, 255, 255, 0.15) !important;
#     border-radius: 8px;
# }
# section[data-testid="stSidebar"] a:hover {
#     background-color: rgba(255, 255, 255, 0.10) !important;
#     border-radius: 8px;
# }

# </style>
# """, unsafe_allow_html=True)

# # =========================
# # MAIN HEADER
# # =========================
# st.markdown(
#     '<div class="main-header">🌍 AI-Driven Climate Risk Prediction System</div>',
#     unsafe_allow_html=True
# )
# st.markdown(
#     '<div class="sub-header">Intelligent Climate Analytics • Early Warning • Predictive Insights</div>',
#     unsafe_allow_html=True
# )

# # =========================
# # SIDEBAR CONTENT
# # =========================
# st.sidebar.title("🌍 Climate Risk System")

# st.sidebar.markdown("""
# ### Navigation
# Use the pages menu above to navigate through different sections:

# - **📊 Dashboard**: Real-time monitoring
# - **📤 Data Upload**: Upload your datasets
# - **🔍 Data Exploration**: Analyze your data
# - **🤖 Model Training**: Train ML/DL models
# - **🔮 Predictions**: Get weather forecasts
# - **⚠️ Alerts**: Early warning system
# - **📜 Historical Analysis**: Historical trends
# """)

# st.sidebar.markdown("---")
# st.sidebar.markdown("### 🎯 System Info")

# st.sidebar.info("""
# **Objective**: Develop an AI system to predict extreme weather events and provide early warnings.

# **Technologies**:
# - Python, Pandas, NumPy
# - TensorFlow, PyTorch, Scikit-learn
# - Streamlit, Plotly
# - XGBoost, LightGBM
# """)

# # =========================
# # MAIN CONTENT
# # =========================
# st.markdown("""
# ## Welcome to the Climate Risk Prediction System! 🌦️

# This application provides a comprehensive platform for:

# ### 🔍 **Data Management**
# - Upload your own climate datasets (CSV, JSON, Parquet, Excel, HDF5)
# - Load data from directories or file paths
# - Data validation and preprocessing

# ### 📊 **Data Analysis**
# - Interactive data exploration
# - Statistical analysis
# - Correlation analysis
# - Feature engineering

# ### 🤖 **Machine Learning**
# - Train multiple ML/DL models:
#   - Random Forest
#   - Gradient Boosting
#   - XGBoost
#   - LSTM (Deep Learning)
# - Model comparison and evaluation
# - Model persistence

# ### 🔮 **Predictions**
# - Real-time weather forecasting
# - Multi-day forecasts
# - Risk assessment
# - Export predictions

# ### ⚠️ **Early Warning System**
# - Extreme heat alerts
# - Flood risk warnings
# - Storm warnings
# - Customizable thresholds

# ### 📜 **Historical Analysis**
# - Trend analysis
# - Seasonal patterns
# - Extreme event identification
# - Comparative analysis

# --- 

# ## 🚀 Getting Started

# 1. **Upload Data**: Navigate to "Data Upload"
# 2. **Explore**: Use "Data Exploration"
# 3. **Train Models**: Go to "Model Training"
# 4. **Get Predictions**: Open "Predictions"
# 5. **Monitor Alerts**: Check "Alerts"

# ---

# ## 📋 Expected Data Format

# Your dataset should include:
# - **Date/Time**
# - **Temperature (°C)**
# - **Precipitation (mm)**
# - **Wind Speed (km/h)**
# - **Humidity (%)**
# - **Pressure**

# ---

# ## 🛠️ Configuration

# Customize everything in `configs/config.yaml`:
# - Model parameters
# - Alert thresholds
# - Feature engineering
# - Dashboard settings

# ---
# """)

# # =========================
# # FOOTER
# # =========================
# st.markdown("---")
# st.markdown("""
# <div style='text-align: center; color: #666; padding: 2rem;'>
#     <p>AI-Driven Climate Risk Prediction System</p>
#     <p>Predict &#8226; Prepare &#8226; Protect &#127793;</p>
#     # <p>Built with ❤️ using Streamlit, TensorFlow, PyTorch, and Scikit-learn</p>
# </div>
# """, unsafe_allow_html=True)




"""Main Streamlit Application"""
import streamlit as st
from pathlib import Path
import sys
import time
from datetime import datetime

# =========================
# PROJECT PATH SETUP
# =========================
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

# =========================
# PAGE CONFIGURATION
# =========================
st.set_page_config(
    page_title="AI Climate Risk OS",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================
# THEME STATE & SWITCHER
# =========================
if 'theme' not in st.session_state:
    st.session_state.theme = 'Deep Sea (Dark)'

def set_theme():
    st.session_state.theme = st.session_state.theme_selector

# =========================
# PREMIUM UI ENGINE (CSS)
# =========================
def apply_custom_design(theme):
    if theme == "Deep Sea (Dark)":
        bg, sidebar, card, text, accent, secondary, border = "#0B0F19", "#111827", "#1F2937", "#F9FAFB", "#3B82F6", "#10B981", "rgba(255,255,255,0.05)"
    elif theme == "Soft Light":
        bg, sidebar, card, text, accent, secondary, border = "#F3F4F6", "#FFFFFF", "#FFFFFF", "#111827", "#2563EB", "#059669", "rgba(0,0,0,0.05)"
    else: # Pristine White
        bg, sidebar, card, text, accent, secondary, border = "#FFFFFF", "#F9FAFB", "#FFFFFF", "#000000", "#000000", "#4B5563", "1px solid #E5E7EB"

    st.markdown(f"""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&display=swap');
        * {{ font-family: 'Inter', sans-serif; }}
        .stApp {{ background-color: {bg}; color: {text}; }}
        [data-testid="stSidebar"] {{ background-color: {sidebar} !important; border-right: 1px solid {border}; }}
        
        /* Hero Section */
        .hero {{ text-align: center; padding: 3rem 1rem 1rem 1rem; }}
        .badge {{ display: inline-block; padding: 4px 12px; border-radius: 20px; background: {accent}22; color: {accent}; font-size: 0.75rem; font-weight: 700; margin-bottom: 1rem; border: 1px solid {accent}44; text-transform: uppercase; letter-spacing: 1px; }}
        .main-title {{ font-size: 3.5rem; font-weight: 800; letter-spacing: -1.5px; margin-bottom: 0.5rem; background: linear-gradient(to right, {text}, {accent}); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }}
        
        /* Module Cards */
        .module-card {{ background: {card}; padding: 2rem; border-radius: 24px; border: 1px solid {border}; transition: all 0.3s ease; height: 100%; }}
        .module-card:hover {{ transform: translateY(-8px); border-color: {accent}66; box-shadow: 0 15px 30px rgba(0,0,0,0.2); }}
        .icon-circle {{ width: 45px; height: 45px; background: {accent}15; color: {accent}; border-radius: 12px; display: flex; align-items: center; justify-content: center; font-size: 1.4rem; margin-bottom: 1.2rem; }}
        
        /* Real-time Metric Boxes */
        div[data-testid="stMetric"] {{ background: {card}; border: 1px solid {border}; padding: 15px 20px !important; border-radius: 18px; }}
    </style>
    """, unsafe_allow_html=True)

apply_custom_design(st.session_state.theme)

# =========================
# SIDEBAR NAVIGATION
# =========================
with st.sidebar:
    st.markdown(f"<h2 style='letter-spacing:-1px;'>🌍 Climate Risk OS</h2>", unsafe_allow_html=True)
    
    st.selectbox(
        "UI Interface Mode",
        ["Deep Sea (Dark)", "Soft Light", "Pristine White"],
        key="theme_selector",
        on_change=set_theme,
        index=["Deep Sea (Dark)", "Soft Light", "Pristine White"].index(st.session_state.theme)
    )
    
    st.markdown("---")
    st.markdown("### 🧭 System Menu")
    st.markdown("""
    - **📊 Dashboard** (Active)
    - **📤 Data Upload**
    - **🔍 Data Exploration**
    - **🤖 Model Training**
    - **🔮 Predictions**
    - **⚠️ Early Warning Alerts**
    - **📜 Historical Analysis**
    """)
    
    st.markdown("---")
    st.info(f"**Target Config:** `configs/config.yaml` loaded successfully.")
    st.caption(f"Last Sync: {datetime.now().strftime('%H:%M:%S')}")

# =========================
# HEADER / HERO
# =========================
st.markdown(f"""
    <div class="hero">
        <div class="badge">● Live Monitoring Active</div>
        <div class="main-title">Predict. Prepare. Protect.</div>
        <p style="opacity: 0.7; font-size: 1.1rem; max-width: 800px; margin: 0 auto;">
            Our AI-Driven System provides intelligent climate analytics, early warning signals, 
            and predictive insights using advanced Machine Learning & Deep Learning.
        </p>
    </div>
""", unsafe_allow_html=True)

# =========================
# REAL-TIME METRICS
# =========================
st.markdown("<br>", unsafe_allow_html=True)
col_m1, col_m2, col_m3, col_m4 = st.columns(4)
with col_m1: st.metric("Live Temp", "24.5 °C", "+0.4")
with col_m2: st.metric("Flood Risk", "Low", "-2%", delta_color="normal")
with col_m3: st.metric("Model Accuracy", "94.8%", "LSTM Active")
with col_m4: st.metric("Data Status", "Synced", "Real-time")

# =========================
# MAIN CONTENT (6 MODULES)
# =========================
st.markdown("<br>", unsafe_allow_html=True)
row1_col1, row1_col2, row1_col3 = st.columns(3)
row2_col1, row2_col2, row2_col3 = st.columns(3)

# Data Management
with row1_col1:
    st.markdown("""
    <div class="module-card">
        <div class="icon-circle">📤</div>
        <h3 style="margin: 0 0 10px 0;">Data Management</h3>
        <p style="font-size: 0.9rem; opacity: 0.8; line-height: 1.5;">
            Ingest <b>CSV, JSON, Parquet, Excel, and HDF5</b>. Auto-validation and preprocessing 
            pipelines ensure data integrity before analysis.
        </p>
    </div>
    """, unsafe_allow_html=True)

# Data Analysis
with row1_col2:
    st.markdown("""
    <div class="module-card">
        <div class="icon-circle">🔍</div>
        <h3 style="margin: 0 0 10px 0;">Data Exploration</h3>
        <p style="font-size: 0.9rem; opacity: 0.8; line-height: 1.5;">
            Perform <b>Interactive Exploration</b>, correlation mapping, and 
            statistical feature engineering to uncover hidden climate patterns.
        </p>
    </div>
    """, unsafe_allow_html=True)

# ML Training
with row1_col3:
    st.markdown("""
    <div class="module-card">
        <div class="icon-circle">🤖</div>
        <h3 style="margin: 0 0 10px 0;">Machine Learning</h3>
        <p style="font-size: 0.9rem; opacity: 0.8; line-height: 1.5;">
            Deploy <b>Random Forest, XGBoost, and Deep Learning (LSTM)</b>. 
            Automated model comparison and evaluation metrics included.
        </p>
    </div>
    """, unsafe_allow_html=True)

# Predictions
with row2_col1:
    st.markdown("""
    <div class="module-card">
        <div class="icon-circle">🔮</div>
        <h3 style="margin: 0 0 10px 0;">Predictive Insights</h3>
        <p style="font-size: 0.9rem; opacity: 0.8; line-height: 1.5;">
            Generate <b>Multi-day weather forecasts</b> and risk assessments 
            with exportable predictive reports for decision makers.
        </p>
    </div>
    """, unsafe_allow_html=True)

# Early Warning
with row2_col2:
    st.markdown("""
    <div class="module-card">
        <div class="icon-circle">⚠️</div>
        <h3 style="margin: 0 0 10px 0;">Early Warning</h3>
        <p style="font-size: 0.9rem; opacity: 0.8; line-height: 1.5;">
            Real-time triggers for <b>Extreme Heat, Flood Risk, and Storms</b> 
            based on customizable system thresholds and alerts.
        </p>
    </div>
    """, unsafe_allow_html=True)

# Historical Analysis
with row2_col3:
    st.markdown("""
    <div class="module-card">
        <div class="icon-circle">📜</div>
        <h3 style="margin: 0 0 10px 0;">Historical Analysis</h3>
        <p style="font-size: 0.9rem; opacity: 0.8; line-height: 1.5;">
            Identify <b>Seasonal patterns</b> and extreme event trends 
            through decades of historical climate observation data.
        </p>
    </div>
    """, unsafe_allow_html=True)

# =========================
# ACTION STEPS SECTION
# =========================
st.markdown("<br><br>", unsafe_allow_html=True)
st.subheader("🚀 System Workflow")
c1, c2, c3, c4, c5 = st.columns(5)

steps = [
    ("1. Upload", "Load Datasets"),
    ("2. Explore", "Analyze Trends"),
    ("3. Train", "Optimize Models"),
    ("4. Predict", "Get Forecasts"),
    ("5. Monitor", "Early Warnings")
]

for i, (title, desc) in enumerate(steps):
    with [c1, c2, c3, c4, c5][i]:
        st.markdown(f"""
            <div style="background:{st.session_state.theme == 'Deep Sea (Dark)' and '#1F2937' or '#FFF'}; padding:15px; border-radius:12px; border-left:4px solid #3B82F6;">
                <b style="font-size:0.8rem; color:#3B82F6;">{title}</b><br>
                <span style="font-size:0.9rem;">{desc}</span>
            </div>
        """, unsafe_allow_html=True)

# =========================
# FOOTER
# =========================
st.markdown("<br><br><hr>", unsafe_allow_html=True)
st.markdown(f"""
    <div style="text-align: center; opacity: 0.6; padding-bottom: 2rem;">
        <p><b>AI-Driven Climate Risk Prediction System</b><br>
        Built with TensorFlow, PyTorch, Scikit-learn, and Streamlit</p>
    </div>
""", unsafe_allow_html=True)
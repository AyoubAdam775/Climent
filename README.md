# 🌍 AI-Driven Climate Risk Prediction System

**IndabaX & Zamzam University Hackathon Project**

An advanced AI-powered system for predicting extreme weather events and providing early warnings for disaster preparedness.

## 📋 Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Configuration](#configuration)
- [Technologies](#technologies)
- [Contributing](#contributing)

## 🎯 Introduction

Climate change is causing an increase in extreme weather events such as hurricanes, floods, and heat waves, which pose serious threats to human life, agriculture, and infrastructure. This project proposes an AI-driven climate risk prediction system that uses historical climate data, satellite imagery, and sensor data to forecast extreme weather events, enabling timely interventions to reduce damage.

### Objectives

**Primary Objective:**
- Develop an AI system to predict extreme weather events and provide early warnings.

**Secondary Objectives:**
1. Integrate diverse climate datasets including historical weather and satellite imagery.
2. Train machine learning and deep learning models for accurate prediction.
3. Create a simple dashboard for visualization and alerts.

## ✨ Features

### 🔍 Data Management
- **Multiple Format Support**: CSV, JSON, Parquet, Excel, HDF5
- **Flexible Data Loading**: Upload files, load from directories, or specify file paths
- **Data Validation**: Automatic data type detection and validation
- **Data Preprocessing**: Handle missing values and data cleaning

### 📊 Data Exploration
- **Interactive Visualizations**: Time series plots, distributions, correlations
- **Statistical Analysis**: Comprehensive statistics and summaries
- **Feature Engineering**: Automatic creation of time-based, lag, and rolling features
- **Data Quality Assessment**: Missing value analysis and data profiling

### 🤖 Machine Learning Models
- **Random Forest**: Ensemble learning for robust predictions
- **Gradient Boosting**: Advanced boosting algorithm
- **XGBoost**: High-performance gradient boosting
- **LSTM**: Deep learning for time series prediction
- **Model Comparison**: Side-by-side performance evaluation
- **Model Persistence**: Save and load trained models

### 🔮 Predictions
- **Real-time Forecasting**: Multi-day weather predictions
- **Risk Assessment**: Automatic risk level classification
- **Confidence Intervals**: Uncertainty quantification
- **Export Options**: Download predictions as CSV or JSON

### ⚠️ Early Warning System
- **Extreme Heat Alerts**: Temperature threshold monitoring
- **Flood Risk Warnings**: Precipitation-based alerts
- **Storm Warnings**: Wind speed monitoring
- **Customizable Thresholds**: Adjust alert sensitivity
- **Alert History**: Track and analyze past alerts

### 📜 Historical Analysis
- **Trend Analysis**: Long-term pattern identification
- **Seasonal Patterns**: Monthly and yearly comparisons
- **Extreme Event Detection**: Identify outliers and anomalies
- **Comparative Analysis**: Multi-variable comparisons

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Step 1: Clone the Repository

```bash
git clone <repository-url>
cd indabax-zamzam-climate-risk
```

### Step 2: Create Virtual Environment

```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On Linux/Mac
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Configure the Application

1. Copy and edit `configs/config.yaml` if needed
2. Create necessary directories:
   ```bash
   mkdir -p data models logs
   ```

## 💻 Usage

### Starting the Application

```bash
streamlit run app.py
```

The application will open in your default web browser at `http://localhost:8501`

### Quick Start Guide

1. **Upload Data**
   - Navigate to "📤 Data Upload"
   - Upload your climate dataset (CSV, JSON, etc.)
   - Or load from a directory/path

2. **Explore Data**
   - Go to "🔍 Data Exploration"
   - Analyze your data with interactive visualizations
   - Apply feature engineering if needed

3. **Train Models**
   - Navigate to "🤖 Model Training"
   - Select target variable and features
   - Choose models to train
   - Start training and view results

4. **Get Predictions**
   - Go to "🔮 Predictions"
   - Select a trained model
   - View forecasts and risk assessments

5. **Monitor Alerts**
   - Check "⚠️ Alerts" page
   - View active warnings
   - Customize thresholds

## 📁 Project Structure

```
indabax-zamzam-climate-risk/
│
├── app.py                          # Main Streamlit application
├── requirements.txt                 # Python dependencies
├── README.md                       # Project documentation
├── .gitignore                      # Git ignore file
│
├── configs/
│   └── config.yaml                 # Configuration file
│
├── data/                           # Data storage directory
│   └── .gitkeep
│
├── models/                         # Trained models storage
│   └── .gitkeep
│
├── logs/                           # Application logs
│
├── src/
│   ├── __init__.py
│   │
│   ├── data_processing/
│   │   ├── __init__.py
│   │   ├── data_loader.py          # Data loading utilities
│   │   └── feature_engineering.py  # Feature engineering
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   └── model_trainer.py        # ML/DL model training
│   │
│   ├── dashboard/
│   │   ├── __init__.py
│   │   ├── alert_system.py         # Alert system
│   │   └── pages/
│   │       ├── 1_📊_Dashboard.py
│   │       ├── 2_📤_Data_Upload.py
│   │       ├── 3_🔍_Data_Exploration.py
│   │       ├── 4_🤖_Model_Training.py
│   │       ├── 5_🔮_Predictions.py
│   │       ├── 6_⚠️_Alerts.py
│   │       └── 7_📜_Historical_Analysis.py
│   │
│   └── utils/
│       ├── __init__.py
│       ├── config_loader.py        # Configuration loader
│       └── logger.py               # Logging utilities
│
└── notebooks/                      # Jupyter notebooks for analysis
```

## ⚙️ Configuration

All settings can be customized in `configs/config.yaml`:

### Model Configuration
- Enable/disable specific models
- Adjust hyperparameters
- Set training parameters

### Alert Configuration
- Set thresholds for extreme events
- Configure alert duration requirements
- Customize alert types

### Feature Engineering
- Configure time features
- Set lag and rolling window sizes
- Define weather features

### Dashboard Settings
- Set refresh intervals
- Configure map settings
- Adjust visualization parameters

## 🛠️ Technologies

### Data Processing
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computing
- **SciPy**: Scientific computing

### Machine Learning
- **Scikit-learn**: Traditional ML algorithms
- **TensorFlow/Keras**: Deep learning
- **PyTorch**: Deep learning framework
- **XGBoost**: Gradient boosting
- **LightGBM**: Light gradient boosting

### Visualization & Dashboard
- **Streamlit**: Web application framework
- **Plotly**: Interactive visualizations
- **Matplotlib**: Static plotting
- **Seaborn**: Statistical visualizations

### Data Sources
- **Kaggle**: Climate datasets
- **NOAA**: Historical weather data
- **Google Earth Engine**: Satellite imagery (optional)

## 📊 Expected Data Format

Your climate dataset should include columns such as:

- **Date/Time**: Timestamp column (required for time series)
- **Temperature**: Temperature readings (°C)
- **Precipitation**: Precipitation amounts (mm)
- **Wind Speed**: Wind speed measurements (km/h)
- **Humidity**: Humidity percentage (%)
- **Pressure**: Atmospheric pressure

## 🎓 Project Information

**Hackathon**: IndabaX & Zamzam University Collaborative Hackathon  
**Location**: Baidoa Campus  
**Project Title**: AI-Driven Climate Risk Prediction System for Extreme Weather Events

## 📝 License

This project is developed for educational and research purposes as part of the IndabaX & Zamzam University Hackathon.

## 🤝 Contributing

This is a hackathon project. Contributions and improvements are welcome!

## 📧 Contact

For questions or issues, please refer to the hackathon organizers.

---

**Built with ❤️ for Climate Risk Prediction** 🌍

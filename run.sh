#!/bin/bash
echo "Starting Climate Risk Prediction System..."
echo ""
echo "Activating virtual environment..."
source venv/bin/activate
echo ""
echo "Starting Streamlit application..."
streamlit run app.py

# 🚀 Quick Start Guide

## Installation Steps

### 1. Install Python Dependencies

```bash
pip install -r requirements.txt
```

**Note**: If you encounter issues with TensorFlow or PyTorch, you can install them separately:

```bash
# For CPU-only TensorFlow
pip install tensorflow-cpu

# For PyTorch (CPU version)
pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu
```

### 2. Setup Project Directories

```bash
python setup.py
```

Or manually create:
- `data/` - For your climate datasets
- `models/` - For trained models
- `logs/` - For application logs

### 3. Run the Application

**Windows:**
```bash
streamlit run app.py
```

**Linux/Mac:**
```bash
streamlit run app.py
```

Or use the provided scripts:
- Windows: `run.bat`
- Linux/Mac: `run.sh` (make executable first: `chmod +x run.sh`)

## 📊 Using Your Own Data

### Supported Formats
- CSV (`.csv`)
- JSON (`.json`)
- Parquet (`.parquet`)
- Excel (`.xlsx`, `.xls`)
- HDF5 (`.h5`)

### Expected Data Columns

Your dataset should ideally include:

| Column | Description | Example |
|--------|-------------|---------|
| `date` or `timestamp` | Date/time column | 2024-01-01 |
| `temperature` | Temperature in Celsius | 25.5 |
| `precipitation` | Precipitation in mm | 10.2 |
| `wind_speed` | Wind speed in km/h | 15.3 |
| `humidity` | Humidity percentage | 65.0 |
| `pressure` | Atmospheric pressure | 1013.25 |

**Note**: The system is flexible - it will work with whatever columns you have, but these are recommended for best results.

### Uploading Data

1. Start the application
2. Navigate to **"📤 Data Upload"** page
3. Choose upload method:
   - **Upload File**: Drag and drop or browse
   - **Load from Directory**: Specify folder path
   - **Load from Path**: Specify full file path
4. Data will be automatically loaded and available across all pages

## 🎯 Typical Workflow

### Step 1: Upload Your Data
- Go to **Data Upload** page
- Upload your climate dataset
- Verify data preview

### Step 2: Explore Your Data
- Navigate to **Data Exploration**
- Review statistics and visualizations
- Apply feature engineering if needed

### Step 3: Train Models
- Go to **Model Training**
- Select target variable (what you want to predict)
- Select feature columns
- Choose models to train
- Click "Start Training"
- Review results and save best model

### Step 4: Get Predictions
- Navigate to **Predictions**
- Select trained model
- View forecasts
- Export predictions if needed

### Step 5: Monitor Alerts
- Check **Alerts** page
- View active warnings
- Customize thresholds as needed

## ⚙️ Configuration

Edit `configs/config.yaml` to customize:

- **Model parameters**: Adjust hyperparameters for each model
- **Alert thresholds**: Set temperature, precipitation, wind speed thresholds
- **Feature engineering**: Configure lag windows, rolling windows
- **Dashboard settings**: Refresh intervals, map settings

## 🐛 Troubleshooting

### Import Errors
If you get import errors, make sure:
1. All dependencies are installed: `pip install -r requirements.txt`
2. You're in the project root directory
3. Virtual environment is activated (if using one)

### Data Loading Issues
- Check file format is supported
- Verify file path is correct
- Ensure file is not corrupted
- Check file encoding (try UTF-8)

### Model Training Errors
- Ensure you have enough data (at least 100 rows recommended)
- Check for missing values in target column
- Verify feature columns are numeric
- Try reducing number of features

### Streamlit Issues
- Clear browser cache
- Restart Streamlit: Press `Ctrl+C` and restart
- Check Streamlit version: `streamlit --version`

## 📚 Additional Resources

- **Full Documentation**: See `README.md`
- **Configuration Guide**: See `configs/config.yaml`
- **Example Notebooks**: Check `notebooks/` directory (if available)

## 💡 Tips

1. **Start Small**: Begin with a small dataset to test the workflow
2. **Feature Engineering**: Apply feature engineering before training for better results
3. **Model Comparison**: Train multiple models and compare their performance
4. **Save Models**: Always save your trained models for future use
5. **Export Data**: Use export features to save predictions and analysis results

## 🆘 Need Help?

- Check the README.md for detailed documentation
- Review error messages carefully
- Ensure all dependencies are correctly installed
- Verify your data format matches expected structure

---

**Happy Predicting! 🌍**

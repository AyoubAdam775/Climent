"""Generate sample climate data for testing"""
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from pathlib import Path

def generate_sample_climate_data(n_days=365, output_path="data/sample_climate_data.csv"):
    """
    Generate sample climate data for testing
    
    Args:
        n_days: Number of days of data to generate
        output_path: Path to save the CSV file
    """
    # Create date range
    start_date = datetime.now() - timedelta(days=n_days)
    dates = pd.date_range(start=start_date, periods=n_days, freq='D')
    
    # Generate realistic climate data
    np.random.seed(42)
    
    # Temperature: seasonal pattern with noise
    base_temp = 25 + 10 * np.sin(2 * np.pi * np.arange(n_days) / 365.25)
    temperature = base_temp + np.random.normal(0, 3, n_days)
    
    # Precipitation: random with some seasonal variation
    precipitation = np.random.exponential(5, n_days)
    precipitation = np.where(np.random.random(n_days) < 0.3, precipitation, 0)  # 30% chance of rain
    
    # Wind speed: moderate with some variation
    wind_speed = np.random.gamma(2, 5, n_days)
    
    # Humidity: inversely related to temperature
    humidity = 80 - (temperature - 20) * 1.5 + np.random.normal(0, 5, n_days)
    humidity = np.clip(humidity, 20, 100)
    
    # Pressure: stable with small variations
    pressure = 1013 + np.random.normal(0, 5, n_days)
    
    # Create DataFrame
    df = pd.DataFrame({
        'date': dates,
        'temperature': np.round(temperature, 2),
        'precipitation': np.round(precipitation, 2),
        'wind_speed': np.round(wind_speed, 2),
        'humidity': np.round(humidity, 2),
        'pressure': np.round(pressure, 2)
    })
    
    # Add some extreme events
    # Extreme heat
    extreme_heat_days = np.random.choice(n_days, size=5, replace=False)
    df.loc[extreme_heat_days, 'temperature'] = np.random.uniform(40, 45, 5)
    
    # Heavy precipitation
    heavy_rain_days = np.random.choice(n_days, size=3, replace=False)
    df.loc[heavy_rain_days, 'precipitation'] = np.random.uniform(50, 100, 3)
    
    # High wind
    high_wind_days = np.random.choice(n_days, size=4, replace=False)
    df.loc[high_wind_days, 'wind_speed'] = np.random.uniform(60, 80, 4)
    
    # Save to CSV
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)
    
    print(f"✅ Generated {n_days} days of sample climate data")
    print(f"📁 Saved to: {output_path}")
    print(f"\nData Preview:")
    print(df.head(10))
    print(f"\nStatistics:")
    print(df.describe())
    
    return df

if __name__ == "__main__":
    print("Generating sample climate data...")
    print("-" * 50)
    df = generate_sample_climate_data(n_days=365)
    print("-" * 50)
    print("\n✅ Sample data ready! You can now upload it in the Data Upload page.")

"""Setup script for Climate Risk Prediction System"""
from pathlib import Path
import os

def create_directories():
    """Create necessary directories"""
    directories = [
        'data',
        'models',
        'logs',
        'notebooks',
        'static'
    ]
    
    for directory in directories:
        Path(directory).mkdir(parents=True, exist_ok=True)
        print(f"✓ Created directory: {directory}")

def create_gitkeep():
    """Create .gitkeep files in empty directories"""
    directories = ['data', 'models']
    for directory in directories:
        gitkeep_path = Path(directory) / '.gitkeep'
        if not gitkeep_path.exists():
            gitkeep_path.touch()
            print(f"✓ Created .gitkeep in {directory}")

if __name__ == "__main__":
    print("Setting up Climate Risk Prediction System...")
    print("-" * 50)
    create_directories()
    create_gitkeep()
    print("-" * 50)
    print("Setup complete!")
    print("\nNext steps:")
    print("1. Install dependencies: pip install -r requirements.txt")
    print("2. Run the application: streamlit run app.py")

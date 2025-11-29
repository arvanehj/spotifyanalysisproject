import pandas as pd
import numpy as np
import os

def create_sample_dataset():
    """Create a smaller sample dataset from the original large CSV"""
    
    #check if original file exists
    original_path = 'data/spotify.csv'
    sample_path = 'data/sample_spotify.csv'
    
    if not os.path.exists(original_path):
        print(f"Original file not found at: {original_path}")
        print("Please make sure your spotify.csv is in the data/ folder")
        return False
    
    #load the original data
    try:
        df = pd.read_csv(original_path)
        print(f"Original dataset loaded: {len(df)} rows, {len(df.columns)} columns")
    except Exception as e:
        print(f"Error loading CSV: {e}")
        return False
    
    #create a sample (200 rows)
    sample_size = min(200, len(df))
    sample_df = df.sample(n=sample_size, random_state=42)  # random_state for reproducibility

    sample_df.to_csv(sample_path, index=False)
    
    return True

if __name__ == "__main__":
    create_sample_dataset()
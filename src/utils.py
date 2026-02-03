# src/utils.py
import pandas as pd

def load_excel(file_path, sheet_name=None):
    """Load an Excel file safely."""
    try:
        if sheet_name:
            return pd.read_excel(file_path, sheet_name=sheet_name)
        return pd.read_excel(file_path)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return None

def save_csv(df, file_path):
    """Save DataFrame to CSV safely."""
    try:
        df.to_csv(file_path, index=False)
        print(f"Saved: {file_path}")
    except Exception as e:
        print(f"Error saving {file_path}: {e}")

def summarize_df(df):
    """Print basic dataset info and first few rows."""
    print("DataFrame info:")
    print(df.info())
    print("\nFirst 5 rows:")
    print(df.head())

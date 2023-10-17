import pandas as pd

dataset_url = "C:\Air_Quality_TN.csv"

try:
    df = pd.read_csv(dataset_url, encoding='latin1')
    print("Dataset loaded successfully.")
except Exception as e:
    print("Error loading the dataset:", str(e))

# Add your preprocessing steps here

print("\nFirst few rows of the dataset:")
print(df.head())

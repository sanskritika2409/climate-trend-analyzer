import pandas as pd

def preprocess_data(df):
    print("Preprocessing Started...")

    # Convert Date
    df['Date'] = pd.to_datetime(df['Date'])

    # Sort values
    df = df.sort_values(by='Date')

    # Handle missing values
    df['Temperature'] = df['Temperature'].fillna(df['Temperature'].mean())
    df['Rainfall'] = df['Rainfall'].fillna(df['Rainfall'].mean())

    print("Preprocessing Completed")
    return df
def add_rolling_average(df):
    df['Temp_Rolling'] = df['Temperature'].rolling(window=3).mean()
    df['Rain_Rolling'] = df['Rainfall'].rolling(window=3).mean()
    return df
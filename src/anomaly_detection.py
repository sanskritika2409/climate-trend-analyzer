def detect_anomalies(df):
    temp_mean = df['Temperature'].mean()
    temp_std = df['Temperature'].std()

    df['Temp_Anomaly'] = ((df['Temperature'] > temp_mean + 2*temp_std) |
                          (df['Temperature'] < temp_mean - 2*temp_std))

    return df
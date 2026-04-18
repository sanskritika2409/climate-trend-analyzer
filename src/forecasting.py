from sklearn.linear_model import LinearRegression
import numpy as np

def forecast_temperature(df):
    df['Time'] = np.arange(len(df))

    X = df[['Time']]
    y = df['Temperature']

    model = LinearRegression()
    model.fit(X, y)

    future = np.array([[len(df)+i] for i in range(12)])
    predictions = model.predict(future)

    return predictions
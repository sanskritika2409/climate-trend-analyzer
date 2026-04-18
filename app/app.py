import streamlit as st
import pandas as pd
import os
import matplotlib.pyplot as plt

# Path setup
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
file_path = os.path.join(BASE_DIR, "data/raw/climate_data.csv")

# Load data
df = pd.read_csv(file_path)
df['Date'] = pd.to_datetime(df['Date'])

# Simple anomaly logic
mean = df['Temperature'].mean()
std = df['Temperature'].std()

df['Anomaly'] = ((df['Temperature'] > mean + 2*std) |
                 (df['Temperature'] < mean - 2*std))

# UI
st.title("🌍 Climate Trend Analyzer Dashboard")

st.subheader("📈 Temperature Trend")
st.line_chart(df.set_index('Date')['Temperature'])

st.subheader("🌧 Rainfall Trend")
st.line_chart(df.set_index('Date')['Rainfall'])

# Anomaly plot
st.subheader("🚨 Temperature Anomalies")

fig, ax = plt.subplots()
ax.plot(df['Date'], df['Temperature'], label='Temperature')

anomalies = df[df['Anomaly'] == True]
ax.scatter(anomalies['Date'], anomalies['Temperature'])

ax.legend()
st.pyplot(fig)
from sklearn.linear_model import LinearRegression
import numpy as np

st.subheader("🔮 Future Temperature Forecast")

df['Time'] = np.arange(len(df))

X = df[['Time']]
y = df['Temperature']

model = LinearRegression()
model.fit(X, y)

future = np.array([[len(df)+i] for i in range(12)])
predictions = model.predict(future)

fig2, ax2 = plt.subplots()
ax2.plot(df['Time'], df['Temperature'], label='Actual')
ax2.plot(range(len(df), len(df)+12), predictions, linestyle='dashed', label='Forecast')

ax2.legend()
st.pyplot(fig2)
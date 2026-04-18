import matplotlib.pyplot as plt

def plot_anomalies(df):
    plt.figure(figsize=(10,5))

    plt.plot(df['Date'], df['Temperature'], label="Temperature")

    anomalies = df[df['Temp_Anomaly'] == True]
    plt.scatter(anomalies['Date'], anomalies['Temperature'])

    plt.title("Anomaly Detection")
    plt.legend()
    plt.grid()

    plt.savefig("outputs/graphs/anomalies.png")
    plt.show()
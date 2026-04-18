import matplotlib.pyplot as plt

def plot_temperature(df):
    plt.figure(figsize=(10,5))
    plt.plot(df['Date'], df['Temperature'])
    plt.title("Temperature Trend")
    plt.xlabel("Date")
    plt.ylabel("Temperature")
    plt.grid()
    plt.savefig("outputs/graphs/temp_trend.png")
    plt.show()

def plot_rainfall(df):
    plt.figure(figsize=(10,5))
    plt.plot(df['Date'], df['Rainfall'])
    plt.title("Rainfall Trend")
    plt.xlabel("Date")
    plt.ylabel("Rainfall")
    plt.grid()
    plt.savefig("outputs/graphs/rainfall_trend.png")
    plt.show()
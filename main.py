from src.data_loader import load_data
from src.preprocessing import preprocess_data
from src.eda import plot_temperature, plot_rainfall
from src.trend_analysis import add_rolling_average
from src.anomaly_detection import detect_anomalies
from src.forecasting import forecast_temperature
from src.visualization import plot_anomalies

def main():
    print("Starting Climate Trend Analyzer...")

    df = load_data("data/raw/climate_data.csv")

    df = preprocess_data(df)

    df = add_rolling_average(df)

    df = detect_anomalies(df)

    plot_temperature(df)
    plot_rainfall(df)
    plot_anomalies(df)

    predictions = forecast_temperature(df)

    print("\nFuture Temperature Predictions:")
    print(predictions)

if __name__ == "__main__":
    main()
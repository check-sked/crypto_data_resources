import requests
import csv
import datetime


def save_historical_tvl_to_csv():
    endpoint = "https://api.llama.fi/v2/historicalChainTvl"

    response = requests.get(endpoint)
    data = response.json()

    csv_file = "historical_tvl.csv"

    with open(csv_file, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "TVL"])

        for item in data:
            timestamp = item["date"]
            date = datetime.datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d")
            tvl = item["tvl"]
            writer.writerow([date, tvl])

    print(f"Data saved to {csv_file} successfully!")


if __name__ == "__main__":
    save_historical_tvl_to_csv()

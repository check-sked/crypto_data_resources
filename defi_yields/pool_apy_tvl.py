import csv
import requests
import datetime


def get_pool_data():
    Pool_ID = input("Enter the Pool ID: ")
    print("The script is running. Press CTRL + C to kill operation at any time.")

    response = requests.get(f"https://yields.llama.fi/chart/{Pool_ID}")
    data = response.json()

    # Open the file in write mode
    with open("pool_tvl_apy.csv", mode="w", newline="") as file:
        # Create a CSV writer
        writer = csv.writer(file)

        # Write the headers to the CSV file
        writer.writerow(["timestamp", "tvlUSD", "apy"])

        # Write the data to the CSV file
        for item in data["data"]:
            timestamp = datetime.datetime.strptime(
                item["timestamp"], "%Y-%m-%dT%H:%M:%S.%fZ"
            ).strftime("%m/%d/%Y")
            tvlUSD = item["tvlUsd"]
            apy = round(item["apy"] / 100, 5)
            writer.writerow([timestamp, tvlUSD, apy])
        print("Data written to pool_tvl_apy.csv")


if __name__ == "__main__":
    get_pool_data()

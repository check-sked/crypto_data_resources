import csv
import requests
import datetime


def get_all_stables():
    # Send GET request to the endpoint
    response = requests.get("https://stablecoins.llama.fi/stablecoincharts/all")

    # Check status code to make sure the request was successful
    if response.status_code != 200:
        print("Failed to retrieve data. Status code:", response.status_code)
        return

    # Extract data from the response
    data = response.json()

    # Open a CSV file for writing
    with open("total_stablecoins_all_chains.csv", "w", newline="") as csvfile:
        # Create a CSV writer object
        writer = csv.writer(csvfile)

        # Write the header row
        writer.writerow(
            ["Date", "Total Circulating ($)", "Total Circulating (Stablecoin Units)"]
        )

        # Write the data rows
        for item in data:
            timestamp = int(item["date"])  # convert timestamp to integer
            date = datetime.datetime.fromtimestamp(timestamp).strftime(
                "%Y-%m-%d"
            )  # format timestamp as human-readable date
            total_circulating_usd = item["totalCirculatingUSD"]["peggedUSD"]
            total_circulating_stablecoin_units = item["totalCirculating"]["peggedUSD"]

            writer.writerow(
                [date, total_circulating_usd, total_circulating_stablecoin_units]
            )

    print("Data written to total_stablecoins_all_chains.csv")


if __name__ == "__main__":
    get_all_stables()

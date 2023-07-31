import csv
import requests
import datetime


def save_total_stablecoins_all_chains_csv():
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
        writer.writerow(["Date", "peggedUSD", "peggedEUR"])

        # Write the data rows
        for item in data:
            timestamp = int(item["date"])  # convert timestamp to integer
            date = datetime.datetime.fromtimestamp(timestamp).strftime(
                "%Y-%m-%d"
            )  # format timestamp as human-readable date
            peggedUSD = item["totalCirculatingUSD"]["peggedUSD"]
            peggedEUR = item["totalCirculatingUSD"]["peggedEUR"]

            writer.writerow([date, peggedUSD, peggedEUR])

    print("Data written to total_stablecoins_all_chains.csv")


if __name__ == "__main__":
    save_total_stablecoins_all_chains_csv()

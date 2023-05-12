import requests
import csv
import datetime

# Input desired chain
chain = "tron"

# Make a GET request to the endpoint
response = requests.get(f"https://stablecoins.llama.fi/stablecoincharts/{chain}")

# Check the status code of the response
if response.status_code == 200:
    # Parse the response data
    data = response.json()

    # Open a CSV file for writing
    with open("stablecoin_supply.csv", "w", newline="") as csv_file:
        # Create a CSV writer object
        writer = csv.writer(csv_file)

        # Write the header row
        writer.writerow(
            [
                "date",
                "total_circulating_usd",
                "total_minted_usd",
                "total_bridged_to_usd",
            ]
        )
        print("data written to stablecoin_supply.csv")

        # Loop through the elements of the data list
        for element in data:
            # Get the data from the element
            date = element["date"]
            date = datetime.datetime.fromtimestamp(int(date)).strftime("%Y-%m-%d")
            stablecoin_supply = element["totalCirculating"]
            total_circulating_usd = element["totalCirculatingUSD"]["peggedUSD"]
            total_minted_usd = element["totalMintedUSD"]["peggedUSD"]
            total_bridged_to_usd = element["totalBridgedToUSD"]["peggedUSD"]

            # Write the data to the CSV file
            writer.writerow(
                [date, total_circulating_usd, total_minted_usd, total_bridged_to_usd]
            )
else:
    # Print an error message
    print("Failed to get stablecoin supply data")

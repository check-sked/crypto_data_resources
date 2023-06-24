import requests
import csv
import datetime


def create_stablecoin_prices_csv():
    # Make a request to the stablecoin prices endpoint
    response = requests.get("https://stablecoins.llama.fi/stablecoinprices")

    # Check that the request was successful
    if response.status_code == 200:
        # The request was successful, so parse the data
        data = response.json()

        # Extract the list of prices
        prices = data

        # Get the list of stablecoins
        stablecoins = list(prices[0]["prices"].keys())

        # Initialize a dictionary to store the previous day's prices for each stablecoin
        prev_prices = {}

        # Open a CSV file for writing
        with open("stablecoin_prices.csv", "w", newline="") as csvfile:
            # Create a CSV writer
            writer = csv.writer(csvfile)

            # Write the header row
            writer.writerow(["Date"] + stablecoins)

            # Write a row for each date
            for date_prices in prices:
                # Convert the Unix timestamp date to a human-readable date
                date = datetime.datetime.fromtimestamp(date_prices["date"]).strftime(
                    "%Y-%m-%d"
                )

                # Build a list of prices for this date
                row = [date]
                for stablecoin in stablecoins:
                    if stablecoin in date_prices["prices"]:
                        price = date_prices["prices"][stablecoin]
                    else:
                        # Use the previous day's price as the placeholder value
                        price = prev_prices.get(
                            stablecoin, 0
                        )  # Use null as the default value if the stablecoin has no previous price
                    row.append(price)
                    prev_prices[stablecoin] = price
                writer.writerow(row)

        # CSV successfully created
        print("CSV successfully created!")
    else:
        # There was an error with the request
        print(f"Request failed with status code {response.status_code}")


if __name__ == "__main__":
    create_stablecoin_prices_csv()

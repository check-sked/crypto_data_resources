import requests
import csv
import datetime


def save_stablecoin_supply_csv(chain):
    # Make a GET request to the endpoint
    response = requests.get(f"https://stablecoins.llama.fi/stablecoincharts/{chain}")

    # Check the status code of the response
    if response.status_code == 200:
        # Parse the response data
        data = response.json()

        # Open a CSV file for writing
        with open(f"{chain}_NATIVE_stablecoin_supply.csv", "w", newline="") as csv_file:
            # Create a CSV writer object
            writer = csv.writer(csv_file)

            # Write the header row
            writer.writerow(["date", "total_circulating_usd"])
            print(f"Data written to {chain}_USD_stablecoin_supply.csv")

            # Loop through the elements of the data list
            for element in data:
                # Get the data from the element
                date = element["date"]
                date = datetime.datetime.fromtimestamp(int(date)).strftime("%Y-%m-%d")
                total_circulating_usd = element["totalCirculating"]["peggedUSD"]

                # Write the data to the CSV file
                writer.writerow([date, total_circulating_usd])
    else:
        # Print an error message
        print("Failed to get stablecoin supply data")


if __name__ == "__main__":
    chain = input("Enter the chain: ")
    save_stablecoin_supply_csv(chain)

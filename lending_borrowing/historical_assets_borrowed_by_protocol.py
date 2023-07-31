import csv
import datetime
import requests


def main():
    # Set the API end point URL
    protocol = input("Enter the lending protocol: ")

    print("The script is running. Press CTRL + C to kill operation at any time.")

    # Make the API request
    response = requests.get(f"https://api.llama.fi/protocol/{protocol}")

    # Check for successful request
    if response.status_code == 200:
        # Get the data from the response
        data = response.json()

        # Get the TVL data
        borrowed_data = data["chainTvls"]["borrowed"]["tvl"]

        # Open a CSV file for writing
        with open(f"{protocol}_historical_borrowed.csv", "w", newline="") as csvfile:
            # Create a CSV writer
            writer = csv.writer(csvfile)
            print(f"data written to {protocol}_historical_borrowed.csv!")

            # Write the header row to the CSV file
            writer.writerow(["Date", "Borrowed_Assets"])

            # Write the TVL data to the CSV file
            for datapoint in borrowed_data:
                # Convert the date value to a human-readable string
                date_string = str(datapoint["date"])
                date = datetime.datetime.fromtimestamp(int(date_string)).strftime(
                    "%Y/%m/%d"
                )  # format the date as 'YYYY/MM/DD'
                tvl = "${:,.2f}".format(
                    float(datapoint["totalLiquidityUSD"])
                )  # format the number as currency
                writer.writerow([date, tvl])
    else:
        # Print an error message
        print("Failed to retrieve data")


if __name__ == "__main__":
    main()

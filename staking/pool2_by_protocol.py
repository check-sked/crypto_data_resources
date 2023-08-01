import csv
import datetime
import requests


def main():
    # Set the API end point URL
    protocol = input("Enter a protocol: ")
    print("The script is running. Press CTRL + C to kill the operation at any time.")

    # Make the API request
    response = requests.get(f"https://api.llama.fi/protocol/{protocol}")

    # Check for successful request
    if response.status_code == 200:
        # Get the data from the response
        data = response.json()

        # Check if the protocol data contains the required information
        if (
            "chainTvls" in data
            and "pool2" in data["chainTvls"]
            and "tvl" in data["chainTvls"]["pool2"]
        ):
            # Get the TVL data
            pool2_data = data["chainTvls"]["pool2"]["tvl"]

            # Open a CSV file for writing
            with open(f"{protocol}_pool2.csv", "w", newline="") as csvfile:
                # Create a CSV writer
                writer = csv.writer(csvfile)

                # Write the header row to the CSV file
                writer.writerow(["Date", "Pool2"])
                print(f"Data written to {protocol}_pool2.csv!")

                # Write the TVL data to the CSV file
                for datapoint in pool2_data:
                    # Convert the date value to a human-readable string
                    date = datetime.datetime.fromtimestamp(
                        int(datapoint["date"])
                    ).strftime("%m/%d/%Y")
                    tvl = datapoint["totalLiquidityUSD"]
                    writer.writerow([date, tvl])
        else:
            # Print an error message for unrecognized protocol
            print(
                "Protocol not recognized. Check protocols_list.py in defi_protocols_chains folder for list."
            )
    else:
        # Print an error message for failed request
        print("Failed to retrieve data")


if __name__ == "__main__":
    main()

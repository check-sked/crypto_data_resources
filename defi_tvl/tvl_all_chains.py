import csv
import requests
from datetime import datetime


def main():
    print("Script is running...")  # Added this line

    # Send a GET request to the chains endpoint
    response = requests.get("https://api.llama.fi/chains")

    # Parse the response JSON data
    chains = response.json()

    # Create a dictionary to hold the TVL data for each chain
    chain_data = {}

    # Iterate through each chain object and retrieve its TVL data
    for chain in chains:
        # Replace any spaces in the chain name with a "-" character
        chain_name = chain["name"].replace(" ", "-")

        # Send a GET request to the chart endpoint for the current chain
        chart_url = f"https://api.llama.fi/charts/{chain_name}"
        chart_response = requests.get(chart_url)

        # Parse the response JSON data and add it to the chain_data dictionary
        chart_data = chart_response.json()
        for item in chart_data:
            # Check if the item has a "date" key before processing its TVL data
            if "date" not in item:
                continue

            # Convert the date from Unix timestamp to human-readable format
            date = int(item["date"])  # Convert the date string to an integer
            date_str = datetime.fromtimestamp(date).strftime(
                "%Y-%m-%d %H:%M:%S"
            )  # %d-%m-%Y

            # Add the TVL data for the current item to the chain_data dictionary
            if chain_name not in chain_data:
                chain_data[chain_name] = []
            chain_data[chain_name].append((date_str, item["totalLiquidityUSD"]))

    # Define the output CSV filename
    output_filename = "tvl_all_chains.csv"

    # Write the TVL data to the output CSV file
    with open(output_filename, mode="w", newline="") as csv_file:
        # Define the CSV fieldnames (i.e. column headers)
        fieldnames = ["date"] + [chain["name"] for chain in chains]

        # Create the CSV writer object and write the fieldnames
        writer = csv.writer(csv_file)
        writer.writerow(fieldnames)

        # Find the date range for all TVL data
        min_date = min(
            [min(data, key=lambda x: x[0])[0] for data in chain_data.values()]
        )
        max_date = max(
            [max(data, key=lambda x: x[0])[0] for data in chain_data.values()]
        )
        all_dates = set([data[0] for data in chain_data.values() for data in data])

        # Write each TVL data point as a new row in the CSV file
        for date in sorted(all_dates):
            row = [date]
            for chain in chains:
                chain_name = chain["name"].replace(" ", "-")
                if chain_name in chain_data and date in [
                    data[0] for data in chain_data[chain_name]
                ]:
                    row.append(
                        [data[1] for data in chain_data[chain_name] if data[0] == date][
                            0
                        ]
                    )
                else:
                    row.append("")
            writer.writerow(row)

    # Print a message to confirm that
    print(f"TVL successfully written to {output_filename}!")


if __name__ == "__main__":
    main()

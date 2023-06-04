# Import necessary libraries
import requests
import csv
from datetime import datetime


# Define a function to get protocol data
def get_protocol_data(endpoint):
    # Send GET request to the endpoint
    response = requests.get(endpoint)
    # Parse JSON response
    data = response.json()
    # Extract chain TVLs data
    chain_tvls = data.get("chainTvls", {})
    # Initialize a dictionary to store liquidity data
    liquidity_data = {}

    # Iterate over each chain and its data in chain_tvls
    for chain, chain_data in chain_tvls.items():
        # Iterate over each entry in 'tvl' list
        for entry in chain_data.get("tvl", []):
            # Extract and format the date from the timestamp
            timestamp = entry["date"]
            date = datetime.utcfromtimestamp(timestamp).strftime("%Y-%m-%d")
            # Extract liquidity in USD
            liquidity_usd = entry["totalLiquidityUSD"]
            # Format protocol-chain string
            protocol_chain = f"{endpoint.split('/')[-1]}-{chain}"
            # Store liquidity data in the dictionary
            if date in liquidity_data:
                liquidity_data[date][protocol_chain] = liquidity_usd
            else:
                liquidity_data[date] = {protocol_chain: liquidity_usd}

    # Return the populated liquidity data
    return liquidity_data


# Define the main execution flow
if __name__ == "__main__":
    # Define the endpoints to scrape data from
    endpoints = ["https://api.llama.fi/protocol/centrifuge"]

    # Initialize a dictionary to store protocol data and a set for protocol_chains
    protocol_data = {}
    protocol_chains = set()

    # Iterate over each endpoint
    for endpoint in endpoints:
        # Get liquidity data from the endpoint
        liquidity_data = get_protocol_data(endpoint)
        # Update protocol data with the obtained liquidity data
        protocol_data.update(liquidity_data)
        # Update protocol chains with the keys of the obtained liquidity data
        for date in liquidity_data:
            protocol_chains.update(liquidity_data[date].keys())

    # Get unique dates sorted
    unique_dates = sorted(protocol_data.keys())
    # Initialize a dictionary to store protocol data by chain
    chain_protocol_data = {protocol_chain: [] for protocol_chain in protocol_chains}

    # Populate chain_protocol_data
    for date in unique_dates:
        for protocol_chain in protocol_chains:
            if protocol_chain in protocol_data[date]:
                chain_protocol_data[protocol_chain].append(
                    protocol_data[date][protocol_chain]
                )
            else:
                chain_protocol_data[protocol_chain].append(None)

    # Set CSV filename
    filename = "centrifuge.csv"

    # Open a new CSV file for writing
    with open(filename, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        # Write the header row
        header_row = ["Date"] + list(chain_protocol_data.keys())
        writer.writerow(header_row)

        # Write each row of data
        for i, date in enumerate(unique_dates):
            row = [date] + [
                chain_protocol_data[protocol_chain][i]
                for protocol_chain in chain_protocol_data
            ]
            writer.writerow(row)

    # Print success message with filename
    print(f"Protocol data saved to '{filename}' CSV file.")

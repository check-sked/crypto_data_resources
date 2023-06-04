import requests
import csv
from datetime import datetime


def get_protocol_data(endpoint):
    response = requests.get(endpoint)
    data = response.json()
    chain_tvls = data.get("chainTvls", {})
    ethereum_tvls = chain_tvls.get("Ethereum", {}).get("tvl", [])
    solana_tvls = chain_tvls.get("Solana", {}).get("tvl", [])

    liquidity_data = {}  # Dictionary to store liquidity data by date

    for entry in ethereum_tvls + solana_tvls:
        timestamp = entry["date"]
        date = datetime.utcfromtimestamp(timestamp).strftime("%Y-%m-%d")
        liquidity_usd = entry["totalLiquidityUSD"]
        liquidity_data[date] = liquidity_usd

    return liquidity_data


if __name__ == "__main__":
    endpoints = [
        "https://api.llama.fi/protocol/centrifuge",
        "https://api.llama.fi/protocol/maple",
        "https://api.llama.fi/protocol/goldfinch",
        "https://api.llama.fi/protocol/credix",
        "https://api.llama.fi/protocol/truefi",
        "https://api.llama.fi/protocol/clearpool",
        "https://api.llama.fi/protocol/homecoin",
        "https://api.llama.fi/protocol/ribbon-lend",
    ]

    protocol_data = {}  # Dictionary to store protocol-specific liquidity data

    all_dates = set()  # Set to store all unique dates

    for endpoint in endpoints:
        protocol_name = endpoint.split("/")[-1]
        liquidity_data = get_protocol_data(endpoint)
        protocol_data[protocol_name] = liquidity_data
        all_dates.update(liquidity_data.keys())

    # Sort the dates in ascending order
    unique_dates = sorted(all_dates)

    # Prepare the data for CSV
    csv_data = []
    for date in unique_dates:
        row = [date]
        for protocol, liquidity_data in protocol_data.items():
            liquidity_usd = liquidity_data.get(date, "")
            row.append(liquidity_usd)
        csv_data.append(row)

    # Save the data to a CSV file
    filename = "alt_rwa_protocol_data.csv"

    with open(filename, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)

        # Write header row
        header_row = ["Date"] + list(protocol_data.keys())
        writer.writerow(header_row)

        # Write data rows
        for row in csv_data:
            writer.writerow(row)

    print(f"Protocol data saved to '{filename}' CSV file.")

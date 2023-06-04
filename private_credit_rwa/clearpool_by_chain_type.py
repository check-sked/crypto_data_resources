import requests
import csv
from datetime import datetime


def get_protocol_data(endpoint):
    response = requests.get(endpoint)
    data = response.json()
    chain_tvls = data.get("chainTvls", {})
    liquidity_data = {}

    for chain, chain_data in chain_tvls.items():
        for entry in chain_data.get("tvl", []):
            timestamp = entry["date"]
            date = datetime.utcfromtimestamp(timestamp).strftime("%Y-%m-%d")
            liquidity_usd = entry["totalLiquidityUSD"]
            protocol_chain = f"{endpoint.split('/')[-1]}-{chain}"
            if date in liquidity_data:
                liquidity_data[date][protocol_chain] = liquidity_usd
            else:
                liquidity_data[date] = {protocol_chain: liquidity_usd}

    return liquidity_data


if __name__ == "__main__":
    endpoints = ["https://api.llama.fi/protocol/clearpool"]

    protocol_data = {}
    protocol_chains = set()

    for endpoint in endpoints:
        liquidity_data = get_protocol_data(endpoint)
        protocol_data.update(liquidity_data)
        for date in liquidity_data:
            protocol_chains.update(liquidity_data[date].keys())

    unique_dates = sorted(protocol_data.keys())
    chain_protocol_data = {protocol_chain: [] for protocol_chain in protocol_chains}

    for date in unique_dates:
        for protocol_chain in protocol_chains:
            if protocol_chain in protocol_data[date]:
                chain_protocol_data[protocol_chain].append(
                    protocol_data[date][protocol_chain]
                )
            else:
                chain_protocol_data[protocol_chain].append(None)

    filename = "clearpool.csv"

    with open(filename, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        header_row = ["Date"] + list(chain_protocol_data.keys())
        writer.writerow(header_row)

        for i, date in enumerate(unique_dates):
            row = [date] + [
                chain_protocol_data[protocol_chain][i]
                for protocol_chain in chain_protocol_data
            ]
            writer.writerow(row)

    print(f"Protocol data saved to '{filename}' CSV file.")

import requests
import csv
import datetime

BRIDGE_MAPPING = {
    "polygon": 1,
    "arbitrum": 2,
    "avalanche": 3,
    "optimism": 4,
    "multichain": 5,
    "portal": 9,
    "celer": 10,
    "synapse": 11,
    "stargate": 12,
    "hop": 13,
    "avalanche-btc": 15,
    "xdai": 16,
    "rainbowbridge": 18,
    "across": 19,
    "allbridge": 22,
    "polygon_zkevm": 23,
    "zksync": 26,
}


def save_bridge_volume_to_csv(chain, bridge_name):
    if bridge_name not in BRIDGE_MAPPING:
        print("Invalid bridge name.")
        return

    bridge_id = BRIDGE_MAPPING[bridge_name]
    endpoint = f"https://bridges.llama.fi/bridgevolume/{chain}?id={bridge_id}"

    response = requests.get(endpoint)
    data = response.json()

    csv_file = f"{chain}_{bridge_name}_volume.csv"  # Updated filename format

    with open(csv_file, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(
            ["Date", "DepositUSD", "WithdrawUSD", "DepositTxs", "WithdrawTxs"]
        )

        for item in data:
            timestamp = item["date"]
            date = datetime.datetime.fromtimestamp(int(timestamp)).strftime("%Y-%m-%d")
            deposit_usd = item["depositUSD"]
            withdraw_usd = item["withdrawUSD"]
            deposit_txs = item["depositTxs"]
            withdraw_txs = item["withdrawTxs"]

            writer.writerow(
                [date, deposit_usd, withdraw_usd, deposit_txs, withdraw_txs]
            )

    print(f"Data saved to {csv_file} successfully.")


if __name__ == "__main__":
    chain = input("Enter the chain: ")
    bridge_name = input("Enter the bridge name: ")
    save_bridge_volume_to_csv(chain, bridge_name)

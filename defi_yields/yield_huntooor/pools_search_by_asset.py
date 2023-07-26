import csv
import requests


def search_by_asset():
    symbol_characters = input("Enter asset ticker: ")
    print("The script is running. Press CTRL + C to kill operation at any time.")

    response = requests.get("https://yields.llama.fi/pools")
    response.raise_for_status()
    data = response.json()

    data = [item for item in data["data"] if symbol_characters in item["symbol"]]
    data = sorted(data, key=lambda x: x["apy"], reverse=True)

    if not data:
        print("No results found for this asset.")
    else:
        with open(f"{symbol_characters}_pools.csv", mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Chain", "Project", "Symbol", "Pool_ID", "APY", "TVL"])
            for item in data:
                project = item["project"]
                symbol = item["symbol"]
                pool = item["pool"]
                chain = item["chain"]
                apy = item["apy"]
                tvl = "${:,.0f}".format(item["tvlUsd"])
                writer.writerow([chain, project, symbol, pool, apy, tvl])

        print(f"Data written to {symbol_characters}_pools.csv")


if __name__ == "__main__":
    search_by_asset()

import csv
import requests

symbol_characters = input("Enter asset ticker you want opportunities for: ")

response = requests.get('https://yields.llama.fi/pools')
response.raise_for_status()
data = response.json()

data = [item for item in data["data"] if symbol_characters in item["symbol"]]
data = sorted(data, key=lambda x: x["apy"], reverse=True)

if not data:
    print("No results found for this asset.")
else:
    with open('pools_search_by_asset.csv.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Chain', 'Project', 'Symbol', 'Pool_ID', 'APY', 'TVL'])
        for item in data:
            project = item['project']
            symbol = item['symbol']
            pool = item['pool']
            chain = item['chain']
            apy = "{:,.2%}".format(item['apy'])
            tvl = "${:,.0f}".format(item['tvlUsd'])
            writer.writerow([chain, project, symbol, pool, apy, tvl])

    print("Data written to pools_search_by_asset.csv")
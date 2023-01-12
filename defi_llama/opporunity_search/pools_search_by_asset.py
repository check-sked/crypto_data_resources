import csv
import requests

symbol_characters = input("Enter symbol characters to filter by: ")

response = requests.get('https://yields.llama.fi/pools')
data = response.json()

data = [item for item in data["data"] if symbol_characters in item["symbol"]]
data = sorted(data, key=lambda x: x["apy"], reverse=True)

with open('pools_search_by_asset.csv.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Chain', 'Project', 'Symbol', 'Pool_ID', 'APY'])
    for item in data:
        project = item['project']
        symbol = item['symbol']
        pool = item['pool']
        chain = item['chain']
        apy = item['apy']
        writer.writerow([chain, project, symbol, pool, apy])

print("Data written to pools_search_by_asset.csv")
import csv
import requests
from fuzzywuzzy import fuzz

symbol = input("Please enter the symbol you want to search for: ")
category = input("Please enter the category you want to filter by (leave blank for no filter): ")

response = requests.get('https://yields.llama.fi/pools')
data = response.json()
data = [x for x in data["data"] if symbol.lower() in x["symbol"].lower()]

if category:
    projects = [x["project"] for x in data]
    response = requests.get('https://api.llama.fi/protocols')
    protocols = response.json()
    protocols = {x["name"]: x["category"] for x in protocols if "name" in x and x["name"] in projects}
    data = [x for x in data if any(fuzz.token_sort_ratio(x["project"], protocol) > 90 for protocol in protocols) and protocols.get(x["project"]) == category]

data = sorted(data, key=lambda x: x["apy"], reverse=True)

with open('pools_data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Chain', 'Project', 'Symbol', 'Pool_ID', 'APY', 'Category'])
    for item in data:
        project = item['project']
        symbol = item['symbol']
        pool = item['pool']
        chain = item['chain']
        apy = item["apy"]
        category = protocols.get(project)
        writer.writerow([chain, project, symbol, pool, apy, category])

print("Data written to pools_data.csv")

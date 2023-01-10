import csv
import requests

response = requests.get('https://yields.llama.fi/pools')
data = response.json()

data = sorted(data["data"], key=lambda x: (x["chain"], x["project"]))

with open('pools_glossary.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Chain', 'Project', 'Symbol', 'Pool_ID'])
    for item in data:
        project = item['project']
        symbol = item['symbol']
        pool = item['pool']
        chain = item['chain']
        writer.writerow([chain, project, symbol, pool])

print("Data written to pools_glossary.csv")
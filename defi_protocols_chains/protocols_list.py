import csv
import requests
from operator import itemgetter

response = requests.get("https://api.llama.fi/protocols")
data = response.json()

# Sort data alphabetically by name and by chain within name
data = sorted(data, key=lambda x: x['name'])
for protocol in data:
    protocol['chains'] = sorted(protocol['chains'])

with open('protocols_list.csv', mode='w') as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Chain"])
    print("data written to protocols_list.csv")

    for protocol in data:
        for chain in protocol["chains"]:
            writer.writerow([protocol["name"], chain])

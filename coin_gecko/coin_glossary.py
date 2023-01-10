import json
import requests
import csv

url = "https://api.coingecko.com/api/v3/coins/list?include_platform=true"
response = requests.get(url)
data = json.loads(response.text)

# Sorting the data alphabetically by name
data = sorted(data, key=lambda x: x["name"])

# Prepare the CSV file
with open('coin_glossary.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["name", "id", "symbol"])
    print("data written to coin_glossary.csv")
    
    # Write the data to the CSV file
    for coin in data:
        writer.writerow([coin["name"], coin["id"], coin["symbol"]])

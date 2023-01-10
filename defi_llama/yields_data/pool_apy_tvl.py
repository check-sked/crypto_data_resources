import csv
import requests
import datetime

# Input Pool ID (Pool IDs can be found in the Pool Glossary)
Pool_ID = "747c1d2a-c668-4682-b9f9-296708a3dd90"

response = requests.get(f"https://yields.llama.fi/chart/{Pool_ID}")
data = response.json()

# Open the file in write mode
with open('pool_tvl_apy.csv', mode='w', newline='') as file:
    # Create a CSV writer
    writer = csv.writer(file)

    # Write the headers to the CSV file
    writer.writerow(["timestamp", "tvlUSD", "apy"])

    # Write the data to the CSV file
    for item in data["data"]:
        timestamp = datetime.datetime.strptime(item['timestamp'], '%Y-%m-%dT%H:%M:%S.%fZ').strftime('%m/%d/%Y')
        tvlUSD = item['tvlUsd']
        apy = round(item['apy']/100, 5)
        writer.writerow([timestamp, tvlUSD, apy])
    print("Data written to pool_tvl_apy.csv")

import requests
import csv

endpoint = "https://bridges.llama.fi/bridges?includeChains=true"

response = requests.get(endpoint)
data = response.json()

csv_file = "bridges.csv"

with open(csv_file, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "ID"])

    bridges = data["bridges"]
    for bridge in bridges:
        name = bridge["name"]
        bridge_id = bridge["id"]
        writer.writerow([name, bridge_id])

print(f"Data saved to {csv_file} successfully.")

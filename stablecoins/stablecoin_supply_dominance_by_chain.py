import requests
import csv
from datetime import datetime

# Input chain to observe
Chain = "Ethereum"

# Input ID of stablecoin. IDs of each stablecoin can be found in stablecoin_dictionary.py
ID = "1"

# Make requests to the endpoints
response1 = requests.get(
    f"https://stablecoins.llama.fi/stablecoincharts/{Chain}?stablecoin={ID}"
)
response2 = requests.get(f"https://stablecoins.llama.fi/stablecoincharts/{Chain}")

# Parse the JSON data
data1 = response1.json()
data2 = response2.json()

# Create an empty list to hold the data
rows = []

# Loop through the data and append the "peggedUSD" and date to the list
for item in data1:
    date = datetime.fromtimestamp(int(item["date"])).strftime("%Y-%m-%d %H:%M:%S")
    peggedUSD = item["totalCirculating"].get("peggedUSD")
    if not peggedUSD:
        peggedUSD = item["totalCirculating"].get("peggedEUR")
    if peggedUSD:
        rows.append([date, peggedUSD, ""])

for item in data2:
    date = datetime.fromtimestamp(int(item["date"])).strftime("%Y-%m-%d %H:%M:%S")
    peggedUSD = item["totalCirculating"].get("peggedUSD")
    if not peggedUSD:
        peggedUSD = item["totalCirculating"].get("peggedEUR")
    if peggedUSD:
        for row in rows:
            if row[0] == date:
                row[2] = peggedUSD

# Add the "stablecoin_dominance" column
for row in rows:
    if row[1] and row[2]:
        stablecoin_dominance = (row[1] / row[2]) * 100
        row.append("{:.2f}%".format(stablecoin_dominance))
    else:
        row.append("N/A")

# Write the data to a CSV file
with open("stablecoin_supply_dominance_by_chain.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(
        [
            "Date",
            "Individual_Stablecoin_Supply",
            "Total_Chain_Supply",
            "stablecoin_dominance",
        ]
    )
    print("data written to stablecoin_supply_dominance_by_chain.csv")
    writer.writerows(rows)

import requests
import pandas as pd

url = "https://api.llama.fi/overview/fees/ethereum?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true&dataType=dailyFees"
response = requests.get(url)
data = response.json()

# Initialize an empty list to store the data
rows = []

for protocol in data["protocols"]:
    # Append a new row to the list for each protocol
    row = {
        "protocol_name": protocol["name"],
        "total24h": protocol["total24h"],
        "change_1d": protocol["change_1d"],
        "change_7d": protocol["change_7d"],
        "change_1m": protocol["change_1m"],
    }
    rows.append(row)

# Create a pandas DataFrame from the list of rows
df = pd.DataFrame(rows)

# Reorder the columns to make the protocol name the first column
df = df[["protocol_name", "total24h", "change_1d", "change_7d", "change_1m"]]

# Write the DataFrame to a CSV file
df.to_csv("protocol_fees_by_chain.csv", index=False)
print("Data written to protocol_fees_by_chain.csv")
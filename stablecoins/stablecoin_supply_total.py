import csv
import requests
import datetime

# Send GET request to the endpoint
response = requests.get("https://stablecoins.llama.fi/stablecoincharts/all")

# Check status code to make sure the request was successful
if response.status_code != 200:
    print("Failed to retrieve data. Status code:", response.status_code)
    exit()

# Extract data from the response
data = response.json()

# Open a CSV file for writing
with open("total_stablecoins_all_chains.csv", "w", newline="") as csvfile:
    # Create a CSV writer object
    writer = csv.writer(csvfile)

    # Write the header row
    writer.writerow(["Date", "peggedUSD", "peggedEUR"])

    # Write the data rows
    for item in data:
        timestamp = int(item["date"])  # convert timestamp to integer
        date = datetime.datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d")  # format timestamp as human-readable date
        peggedUSD = item["totalCirculating"]["peggedUSD"]
        peggedEUR = item["totalCirculating"]["peggedEUR"]

        writer.writerow([date, peggedUSD, peggedEUR])

print("Data written to total_stablecoins_all_chains.csv")
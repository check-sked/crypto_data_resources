import csv # For csv file creation
import requests # For get request
import time  # For date parsing and formatting

# Input chain name
chain = "Ethereum"

# Make a request to the endpoint
response = requests.get(f"https://api.llama.fi/charts/{chain}")

# Parse the JSON response
data = response.json()

# Write the data to a CSV file
with open("defi_llama_chain.csv", "w", newline="") as csvfile:
    fieldnames = data[0].keys()
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for entry in data:
        # Parse the date using time.strptime and reformat it using time.strftime
        date_time = time.gmtime(int(entry['date']))
        entry['date'] = time.strftime("%B %d, %Y", date_time)
        writer.writerow(entry)
import csv # For csv file creation
import requests # For get request
import datetime  # For date reformat

# Make a request to the endpoint
response = requests.get("https://api.llama.fi/charts")

# Parse the JSON response
data = response.json()

# Write the data to a CSV file
with open("defi_llama.csv", "w", newline="") as csvfile:
    fieldnames = data[0].keys()
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for entry in data:
        writer.writerow(entry)
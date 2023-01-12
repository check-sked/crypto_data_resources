import requests
import json
import csv

url = "https://yields.llama.fi/pools"
try:
    # Make API request and get response
    response = requests.get(url)
    # Check if the response is successful
    response.raise_for_status()
    if response.headers['Content-Type'] != 'application/json':
        print("Unexpected Content-Type: ", response.headers['Content-Type'])
        raise ValueError("Unexpected Content-Type")
    data = json.loads(response.text)

    # Sorting the data by APY in descending order
    data = sorted(data["data"], key=lambda x: x["apy"], reverse=True)

    # Open a CSV file for writing
    with open("all_pools_by_apy.csv", "w", newline="") as csvfile:
        # Create a CSV writer
        writer = csv.writer(csvfile)

        # Write the header row
        writer.writerow(["chain", "project", "symbol", "apy", "pool"])

        # Write the data rows
        for pool in data:
            writer.writerow([pool["chain"], pool["project"], pool["symbol"], pool["apy"], pool["pool"]])
    print("data written to all_pools_by_apy.csv")
except requests.exceptions.HTTPError as err:
    print(f"HTTP Error Occured: {err}")
except requests.exceptions.RequestException as err:
    print(f"Something went wrong: {err}")
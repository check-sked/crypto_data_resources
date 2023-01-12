import json
import requests
import csv

url = "https://api.coingecko.com/api/v3/coins/list?include_platform=true"
try:
    # Make API request and get response
    response = requests.get(url)
    # Check if the response is successful
    response.raise_for_status()
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
except requests.exceptions.RequestException as e:
    print("An error occurred while making the API request:", e)
except json.decoder.JSONDecodeError as e:
    print("An error occurred while parsing the API response:", e)
except KeyError as e:
    print("An error occurred while processing the data:", e)
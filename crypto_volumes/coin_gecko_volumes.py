import requests
import csv
import json
import datetime
import time

# Link to CoinGecko Docs: https://www.coingecko.com/en/api/documentation

# Input cryptocurrency ID (refer to coin glossary for IDs of all coins on CoinGecko)
cryptocurrency = "stellar"

# Input Base Currency of Crypto Pair to Observe
vs_currency = "usd"

# Input Time Frame - UTC
start_date = datetime.datetime(
    2020, 1, 1, 0, 0, 0
)  # Year, Month, Day, Hour, Minute, Second
end_date = datetime.datetime(2022, 12, 31, 23, 59, 59)
# Convert to UNIX Format For CoinGecko API
start_date_unix = time.mktime(start_date.timetuple())
end_date_unix = time.mktime(end_date.timetuple())


# Set base URL for API endpoint - Example: https://api.coingecko.com/api/v3/coins/bitcoin/market_chart/range?vs_currency=usd&from=1392577232&to=1422577232
base_url = "https://api.coingecko.com/api/v3/coins"

try:
    # Make API request and get response
    response = requests.get(
        f"{base_url}/{cryptocurrency}/market_chart/range?vs_currency={vs_currency}&from={start_date_unix}&to={end_date_unix}"
    )

    # Check if the response is successful
    response.raise_for_status()

    data = json.loads(response.text)

    # Open a CSV file for writing
    with open("crypto_volumes.csv", "w", newline="") as csvfile:
        # Create a CSV writer
        writer = csv.writer(csvfile)

        # Write the header row
        writer.writerow(["date", "volume"])

        # Data successfully written message
        print("data written to crypto_volumes.csv")

        # Write the data rows
        for datapoint in data["total_volumes"]:
            # Convert the timestamp to a human-readable date
            date = datetime.datetime.fromtimestamp(datapoint[0] / 1000.0)
            date_str = date.strftime("%Y-%m-%d")
            # Write the row to the CSV file
            writer.writerow([date_str, datapoint[1]])
except requests.exceptions.RequestException as e:
    print("An error occurred while making the API request:", e)
except json.decoder.JSONDecodeError as e:
    print("An error occurred while parsing the API response:", e)
except KeyError as e:
    print("An error occurred while processing the data:", e)

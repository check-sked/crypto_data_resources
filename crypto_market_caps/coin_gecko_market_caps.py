import requests
import csv
import json
import datetime
import time

# Link to CoinGecko Docs: https://www.coingecko.com/en/api/documentation

# Input list of cryptocurrency IDs. Put them in ' ' and separate with commas. (refer to coin glossary for IDs of all coins on CoinGecko)
cryptocurrency_ids = ['bitcoin', 'ethereum']

# Input Base Currency of Crypto Pair to Observe
vs_currency = 'usd'

# Input Time Frame - UTC
start_date = datetime.datetime(2021, 6, 1, 0, 0, 0) # Year, Month, Day, Hour, Minute, Second
end_date = datetime.datetime(2023, 2, 1, 23, 59, 59)
# Convert to UNIX Format For CoinGecko API
start_date_unix = int(time.mktime(start_date.timetuple()))
end_date_unix = int(time.mktime(end_date.timetuple()))

# Set base URL for API endpoint - Example: https://api.coingecko.com/api/v3/coins/bitcoin/market_chart/range?vs_currency=usd&from=1392577232&to=1422577232
base_url = "https://api.coingecko.com/api/v3/coins"

# Define a dict to store the data for each cryptocurrency ID
market_cap_dict = {}

try:
    # Open a CSV file for writing
    with open(f"{cryptocurrency_ids}_market_caps.csv", "w", newline="") as csvfile:
        # Create a CSV writer
        writer = csv.writer(csvfile)

        # Create a dictionary to store all the market capitalizations for each cryptocurrency
        market_cap_dict = {}
        for cryptocurrency_id in cryptocurrency_ids:
            # Make API request and get response
            response = requests.get(f"{base_url}/{cryptocurrency_id}/market_chart/range?vs_currency={vs_currency}&from={start_date_unix}&to={end_date_unix}")
            data = json.loads(response.text)

            # Check if the API returned an error
            if "market_caps" not in data:
                raise Exception(f"An error occurred while retrieving data for {cryptocurrency_id}: {data}")

            # Add the market capitalizations for this cryptocurrency to the market cap dictionary
            market_cap_dict[cryptocurrency_id] = {datetime.datetime.fromtimestamp(datapoint[0] / 1000.0).strftime("%Y-%m-%d"): datapoint[1] for datapoint in data["market_caps"]}

        # Write the header row
        writer.writerow(["date"] + [c_id.capitalize() for c_id in cryptocurrency_ids])

        # Get a set of all the dates in the market cap dictionary
        all_dates = set(date for market_caps in market_cap_dict.values() for date in market_caps)

        # Write the data rows
        for date in sorted(all_dates):
            row = [date]
            for cryptocurrency_id in cryptocurrency_ids:
                row.append(market_cap_dict[cryptocurrency_id].get(date, ""))
            writer.writerow(row)

        # Data successfully written message
        print(f"data written to {cryptocurrency_ids}_market_caps.csv!")

except requests.exceptions.RequestException as e:
    print("An error occurred while making the API request:", e)
except json.decoder.JSONDecodeError as e:
    print("An error occurred while parsing the API response:", e)
except Exception as e:
    print("An error occurred:", e)
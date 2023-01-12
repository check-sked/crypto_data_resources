import csv
import datetime
import requests

# Set the API end point URL
protocol = "aave"

# Make the API request
response = requests.get(f"https://api.llama.fi/protocol/{protocol}")

# Check for successful request
if response.status_code == 200:
  # Get the data from the response
  data = response.json()

  # Get the TVL data
  tvl_data = data["tvl"]

  # Open a CSV file for writing
  with open("tvl_data.csv", "w", newline="") as csvfile:
    # Create a CSV writer
    writer = csv.writer(csvfile)

    # Write the header row to the CSV file
    writer.writerow(["Date", "TVL"])

    # Write the TVL data to the CSV file
    for datapoint in tvl_data:
      # Convert the date value to a human-readable string
      date_string = str(datapoint["date"])
      date = datetime.datetime.fromtimestamp(int(date_string)).isoformat()
      tvl = datapoint["totalLiquidityUSD"]
      writer.writerow([date, tvl])
else:
  # Print an error message
  print("Failed to retrieve data")

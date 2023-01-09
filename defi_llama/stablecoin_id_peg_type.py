import requests
import csv

# Send a GET request to the endpoint
response = requests.get("https://stablecoins.llama.fi/stablecoins?includePrices=true")

# Check the status code to make sure the request was successful
if response.status_code == 200:
  # The request was successful, so parse the JSON response
  data = response.json()
  # Open a file for writing the data
  with open('stablecoins.csv', 'w', newline='') as csvfile:
    # Create a CSV writer
    writer = csv.writer(csvfile)
    # Write the header row
    writer.writerow(['Symbol', 'ID', 'Peg Type'])
    # Loop through the list of stablecoins
    for stablecoin in data['peggedAssets']:
      # Write the stablecoin data to the CSV file
      writer.writerow([stablecoin['symbol'], stablecoin['id'], stablecoin['pegType']])
else:
  # The request was not successful, so print an error message
  print("An error occurred while retrieving the data")

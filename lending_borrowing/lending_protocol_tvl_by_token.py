import csv
import requests
import datetime

# Input protocol to observe
Protocol = "compound"

# Starting date for UNIX timestamps (in seconds)
start_date = datetime.datetime(2021, 1, 1)
start_timestamp = int((start_date - datetime.datetime(1970, 1, 1)).total_seconds())

try:
    # Retrieve data from API
    response = requests.get(f"https://api.llama.fi/protocol/{Protocol}")
    response.raise_for_status()
    data = response.json()
except requests.exceptions.HTTPError as errh:
    print ("HTTP Error:",errh)
except requests.exceptions.ConnectionError as errc:
    print ("Error Connecting:",errc)
except requests.exceptions.Timeout as errt:
    print ("Timeout Error:",errt)
except requests.exceptions.RequestException as err:
    print ("Something went wrong:",err)

# Create a list to hold the header row
header_row = ['Date']
header_row.extend(list(data['tokens'][0]['tokens'].keys())) # add all the assets as columns in the header row

# Create a list to hold the rows of data
data_rows = []

# Iterate through the data
for tvl_data in data['tokens']:
    date = datetime.datetime.fromtimestamp(start_timestamp + tvl_data['date']/1000).strftime('%Y-%m-%d')
    tokens = tvl_data['tokens']
    data_rows.append([date] + [tokens.get(token, 0) for token in header_row[1:]])

# Write the data to a CSV file
with open('tvl_by_token.csv', mode='w') as file:
    print('data written to tvl_by_token.csv')
    writer = csv.writer(file)
    writer.writerow(header_row)
    for row in data_rows:
        writer.writerow(row)
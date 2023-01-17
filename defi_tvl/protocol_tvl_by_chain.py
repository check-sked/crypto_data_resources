import csv
import requests
import datetime

# Input protocol to observe
Protocol = "frax"

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

# Create a list to hold the rows of data
data_rows = []

# Iterate through the chainTvls data
for chain, tvl_data in data['chainTvls'].items():
    if 'borrowed' in chain or 'staking' in chain or chain == 'pool2':
        continue
    header_row.append(chain)
    for tvl in tvl_data['tvl']:
        date = datetime.datetime.fromtimestamp(start_timestamp + tvl['date']/1000)
        found = False
        for row in data_rows:
            if row[0] == date:
                row.append(tvl['totalLiquidityUSD'])
                found = True
                break
        if not found:
            data_rows.append([date, tvl['totalLiquidityUSD']])

# Sort the data by date
data_rows = sorted(data_rows, key=lambda x: x[0])

# Write the data to a CSV file
with open('tvl_by_protocol_chain.csv', mode='w') as file:
    writer = csv.writer(file)
    writer.writerow(header_row)
    for row in data_rows:
        writer.writerow([row[0].strftime('%Y-%m-%d %H:%M:%S'), row[1]])
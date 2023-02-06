import requests
import csv
import time

# get all the protocols from lending category
response = requests.get("https://api.llama.fi/protocols")
data = response.json()
protocols = [protocol['slug'].replace(" ", "-") for protocol in data if protocol['category'] == 'Lending']

# get the tvl data for each protocol
results = {}
for protocol in protocols:
    response = requests.get(f"https://api.llama.fi/protocol/{protocol}")
    data = response.json()
    try:
        tvl = data['chainTvls']['borrowed']['tvl']
        results[protocol] = {time.strftime('%Y-%m-%d', time.gmtime(int(x['date']))): x['totalLiquidityUSD'] for x in tvl}
    except KeyError:
        continue

# create a list of unique dates from the tvl data
dates = set()
for protocol in results:
    for date in results[protocol]:
        dates.add(date)

dates = list(dates)
dates.sort()

# write the data to a csv
with open("cumulative_DeFi_assets_borrowed.csv", "w", newline="") as f:
    writer = csv.writer(f)
    header = ["Date"] + protocols
    writer.writerow(header)
    print("Data written to cumulative_DeFi_assets_borrowed.csv!")

    for date in dates:
        row = [date]
        for protocol in protocols:
            try:
                row.append(results[protocol][date])
            except KeyError:
                row.append("")
        writer.writerow(row)
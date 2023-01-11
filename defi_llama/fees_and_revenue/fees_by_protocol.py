import csv
import requests
from datetime import datetime

# Input protocol to observe. Reference protocols_list_fees.csv for available protocols.
Protocol = "Uniswap"

# Input time period (daily or total)
Type = "daily"

response = requests.get(f"https://api.llama.fi/summary/fees/{Protocol}?dataType={Type}Fees")
data = response.json()

with open('fees_by_protocol.csv', mode='w', newline='') as csv_file:
    fieldnames = ['date', 'fees']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    print("data written to fees_by_protocol.csv")

    for day in data['totalDataChart']:
        timestamp = day[0]
        fees = day[1]
        date = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d')
        writer.writerow({'date': date, 'fees': fees})


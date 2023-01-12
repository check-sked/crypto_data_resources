import csv
import requests
from datetime import datetime

# Input protocol to observe. Reference protocols_list_fees.csv for available protocols.
Protocol = "aave"

# Input type (daily or total)
Type = "daily"

response = requests.get(f"https://api.llama.fi/summary/fees/{Protocol}?dataType={Type}Revenue")
data = response.json()

with open('revenue_by_protocol.csv', mode='w', newline='') as csv_file:
    fieldnames = ['date', 'revenue']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    print("data written to revenue_by_protocol.csv")

    for day in data['totalDataChart']:
        timestamp = day[0]
        fees = day[1]
        date = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d')
        writer.writerow({'date': date, 'fees': fees})
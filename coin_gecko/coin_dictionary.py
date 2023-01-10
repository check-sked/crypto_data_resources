import requests
import csv

url = "https://api.coingecko.com/api/v3/coins/list?include_platform=true" # Includes all coins and tokens on CoinGecko 
response = requests.get(url)
data = response.json()

# Prepare the CSV file
with open('cryptocurrency_list.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["id", "symbol", "name"])
    print("data written to cryptocurrency_list.csv")
    
    # Write the data to the CSV file
    for coin in data:
        writer.writerow([coin["id"], coin["symbol"], coin["name"]])

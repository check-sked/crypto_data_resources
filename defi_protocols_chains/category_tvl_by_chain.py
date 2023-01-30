import requests
import csv
import time
from datetime import datetime, timedelta

def get_protocols(category, chain):
    response = requests.get('https://api.llama.fi/protocols')
    data = response.json()
    protocols = []
    for item in data:
        if item['category'] == category and chain in item['chains']:
            protocols.append(item['slug'].replace(' ', '-'))
    return protocols

def get_tvl(protocol_name, chain):
    response = requests.get(f'https://api.llama.fi/protocol/{protocol_name}')
    data = response.json()
    tvl = []
    for item in data['chainTvls'][chain]['tvl']:
        date = datetime.fromtimestamp(item['date']).strftime('%Y-%m-%d')
        tvl.append({'date': date, 'totalLiquidityUSD': item['totalLiquidityUSD']})
    return tvl

def main():
    category = input("Enter category: ")
    chain = input("Enter chain: ")
    protocols = get_protocols(category, chain)
    with open(f'{chain}_{category}_TVL.csv', 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['date'] + protocols + ['Total'])
        writer.writeheader()
        for i in range(3):
            row = {}
            row['date'] = (datetime.today() - timedelta(days=i)).strftime('%Y-%m-%d')
            total = 0
            for protocol_name in protocols:
                tvl = get_tvl(protocol_name, chain)
                for item in tvl:
                    if item['date'] == row['date']:
                        row[protocol_name] = "${:,.2f}".format(item['totalLiquidityUSD'])
                        total += item['totalLiquidityUSD']
                        break
            row['Total'] = "${:,.2f}".format(total)
            writer.writerow(row)
    print(f'Data written to {chain}_{category}_TVL.csv!')

if __name__ == "__main__":
    main()

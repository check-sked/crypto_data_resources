import requests
import csv

# Set up filters
pool_tokens = input("Enter pool token symbol (leave blank if not filtering by token): ")
pool_rewards = input("Enter pool rewards symbol (leave blank if not filtering by rewards): ")
chain = input("Enter chain name (leave blank if not filtering by chain): ")

# Make GET request to Frax API endpoint
response = requests.get('https://api.frax.finance/pools')
data = response.json()

# Sort data by apy in descending order
data = sorted(data, key=lambda x: x['apy'], reverse=True)

# Apply filters
if pool_tokens:
    data = [pool for pool in data if any(token.lower() == pool_tokens.lower() for token in pool['pool_tokens'])]
if pool_rewards:
    data = [pool for pool in data if pool_rewards.lower() in pool['pool_rewards'].lower()]
if chain:
    data = [pool for pool in data if chain.lower() in pool['chain'].lower()]

# Write data to CSV file
with open('frax_pools_search.csv', mode='w') as file:
    writer = csv.writer(file)
    headers = ["chain", "platform", "pool_tokens", "pool_rewards", "liquidity_locked", "apy", "apy_max"]
    writer.writerow(headers)
    for pool in data:
        writer.writerow([pool['chain'], pool['platform'], pool['pool_tokens'], pool['pool_rewards'], "${:,.2f}".format(float(pool['liquidity_locked'])), "{:.2%}".format(float(pool['apy'])), "{:.2%}".format(float(pool['apy_max']))])
        
print("Data filtered and written to frax_pools_search.csv.")
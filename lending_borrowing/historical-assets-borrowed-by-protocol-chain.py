import requests
import pandas as pd

# input chain (check chain_list.py for all chains)
chain = input("Enter chain (Ethereum, Optimism, Aptos, etc.): ")

# input protocol name (check protocols_list.py for all protocols)
Protocol_Name = input("Enter lending protocol (Aave, Compound, Venus, etc.): ")

# make a GET request to the API endpoint
response = requests.get(f"https://api.llama.fi/protocol/{Protocol_Name}")

# convert the response to a dictionary
data = response.json()

# get all of the borrowed keys
borrowed_keys = [key for key in data['chainTvls'].keys() if chain in key]

# create a dictionary of dataframes, with each key representing a borrowed key
dfs = {key: pd.DataFrame(data['chainTvls'][key]['tvl']) for key in borrowed_keys}

# merge all of the dataframes into a single dataframe
result = pd.concat(dfs, axis=1)

# write the resulting dataframe to a csv file
result.to_csv(f'historical_{Protocol_Name}_{chain}_borrowed_tvl.csv'.format(chain), index=False)
print(f"data written to historical_{Protocol_Name}_{chain}_borrowed_tvl.csv!")
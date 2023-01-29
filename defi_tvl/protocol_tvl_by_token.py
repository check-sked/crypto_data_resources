import pandas as pd
import requests
from datetime import datetime

Protocol = "binance-cex"

try:
    response = requests.get(f"https://api.llama.fi/protocol/{Protocol}")
    response.raise_for_status()
    data = response.json()
except requests.exceptions.RequestException as e:
    print("An error occurred while making the API request:", e)
    raise SystemExit(1)

# Create an empty list to store the data in
output_data = []

# Iterate through the list of tokens in the response
for token_data in data['tokens']:
    date = datetime.fromtimestamp(token_data['date']).strftime('%Y-%m-%d')
    tokens = token_data['tokens']
    for token, tvl in tokens.items():
        output_data.append({'date': date, 'token': token, 'tvl': tvl})

# Convert the list of dictionaries to a DataFrame
output_df = pd.DataFrame(output_data)

# group by date and token
grouped_df = output_df.groupby(['date','token'], as_index=False).sum()

# unstack the dataframe
pivot_df = grouped_df.pivot(index='date', columns='token', values='tvl')

# Add the date column
pivot_df.insert(0, 'date', pivot_df.index)

# Save the DataFrame to a CSV file named output.csv
try:
    pivot_df.to_csv('protocol_tvl_by_token.csv', index=False)
    print("Data written to protocol_tvl_by_token.csv")
except Exception as e:
    print("An error occurred while writing the CSV file:", e)
    raise SystemExit(1)
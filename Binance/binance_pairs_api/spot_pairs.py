from binance.client import Client
import pandas as pd

# Insert API Key and API Secret Key
client = Client('api_key', 'api_secret')

# Call to retreive all available tickers
pairs = pd.DataFrame.from_dict(client.get_all_tickers())['symbol'].to_list()

# Sort pairs in alphabetical order
pairs_sorted = pd.DataFrame.from_dict(client.get_all_tickers()).sort_values(by=['symbol'], ascending=True)['symbol']

# Create Excel file that appears in root directory
OUTPUT_FILENAME = "Binance_Available_Pairs.xlsx"
pairs_sorted.to_excel(OUTPUT_FILENAME, index=False)
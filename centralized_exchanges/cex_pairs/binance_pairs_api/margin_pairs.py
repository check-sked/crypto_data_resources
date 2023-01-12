from binance.client import Client
import pandas as pd

# Insert API Key and API Secret Key
client = Client('api_key', 'api_secret')

# Call to retreive pairs
symbols = client.get_exchange_info()
df = pd.DataFrame(symbols['symbols'])

# Create list element
li = []

# Check if pair is avaialble for margin trading and append li
for index, data in df.iterrows():
    if data['isMarginTradingAllowed'] == True:
        li.append(data['symbol'])

# Create Excel file that appears in root directory
fdf = pd.DataFrame(li)
fdf.to_excel('Binance_Available_Margin_Pairs.xlsx', index=False)
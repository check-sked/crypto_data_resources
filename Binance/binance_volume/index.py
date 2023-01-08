import pandas as pd
from binance.client import Client
import datetime as dt

# Insert API Key and API Secret Key
client = Client("api_key", "api_secret")

# Pair to pull volume data for. THIS IS INPUT BY THE USER
sym = "ETHUSDT"

# Duration of bar size measured. Request is daily in this case but can be substituted with 1s-> seconds; 1,3,5,15,30 m -> minutes; 1,2,4,6,8,12 h -> hours; 1 or 3 d -> days; 1w -> weeks; 1M -> months
interval = "1d"

# Call to retreive volume by specified pair. START and END points for the request TO BE INPUT BY THE USER.
Client.KLINE_INTERVAL_1DAY
klines = client.get_historical_klines(sym, interval, "1 Dec,2021")
data = pd.DataFrame(klines)

# Format columns names
data.columns = ["datetime", "open", "high", "low", "close", "volume","close_time", "qav", "num_trades","taker_base_vol", "taker_quote_vol", "ignore"]          

# Convert the timestamp values in the 'datetime' column to a human-readable string format
data['datetime'] = data['datetime'].apply(lambda x: dt.datetime.fromtimestamp(x/1000.0).strftime('%Y-%m-%d %H:%M:%S'))

data.index = [dt.datetime.fromtimestamp(x/1000.0) for x in data.close_time]

# Adjust displayed columns to reflect relevant data. "open", "high", "low", "close_time", "qav","taker_base_vol", "taker_quote_vol", "ignore" can be added as needed.
data = data[["datetime", "volume", "close", "num_trades"]]

# Create Excel file that appears in root directory
OUTPUT_FILENAME = "Binance_volume_by_pair_" + sym + ".xlsx"
data.to_excel(OUTPUT_FILENAME, index=False)
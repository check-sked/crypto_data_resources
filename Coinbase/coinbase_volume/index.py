import requests
import pandas as pd
import time
from datetime import datetime, timedelta

# API URL to call from
apiURL = 'https://api.pro.coinbase.com'

# Pair to pull volume data for. THIS IS INPUT BY THE USER
sym = 'ETH-USDC'

# Duration of bar size measured in seconds. Request is daily (86,400 seconds = 1 day). Must match delta variable below.
barSize = '86400'

# Delta corresponding to bar size. Used to determine start time. This can be changed to weeks, minutes, seconds. Must match barSize variable above.
delta = timedelta(days = 1)

# Get data up to present
timeEnd = datetime.now()

# Start request 300 days in the past (request cannot be more than 300 bars)
timeStart = timeEnd - (300 * delta)

# Change output to iso format for API recognition
timeStart = timeStart.isoformat()
timeEnd = timeEnd.isoformat()

# Parameters outlined by Coinbase API documentation
parameters = {
    "start": timeStart,
    "end": timeEnd,
    "granularity": barSize,
}

# Get request
data = requests.get(f"{apiURL}/products/{sym}/candles",
params = parameters,
headers = {"content-type": "application/json"})

# Convert request to JSON and format columns
df = pd.DataFrame(data.json(),
columns = ["time","low","high","open","close","volume"])

# Substitute date format for default time format
df["date"] = pd.to_datetime(df["time"], unit = "s")

# Adjust displayed columns to reflect relevant data. "open" and "high" can be added as needed.
df = df[["date", "volume", "close"]]

# create Excel file that appears in root directory
OUTPUT_FILENAME = "Coinbase_volume_by_pair_" + sym + ".xlsx"
df.to_excel(OUTPUT_FILENAME, index=False)
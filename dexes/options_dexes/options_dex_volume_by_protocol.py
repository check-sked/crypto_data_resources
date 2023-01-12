import requests
import csv
from datetime import datetime

# Input name of dex you want to observe
Protocol = "lyra"

# Input daily or total volume
Type = "daily"

# Input type of volume (Notional or Premium - **CASE SENSITIVE**)
Volume = "Notional"

try:
    response = requests.get(f"https://api.llama.fi/summary/options/{Protocol}?dataType={Type}{Volume}Volume")
    response.raise_for_status()
    data = response.json()

    with open('options_dex_volume.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["date", "volume"])
        for item in data["totalDataChart"]:
            date = datetime.fromtimestamp(item[0]).strftime('%Y-%m-%d')
            volume = item[1]
            writer.writerow([date, volume])
    print("Data written to options_dex_volume.csv")
except requests.exceptions.HTTPError as e:
    print("HTTP Error:", e)
except requests.exceptions.ConnectionError as e:
    print("Error Connecting:", e)
except requests.exceptions.Timeout as e:
    print("Timeout Error:", e)
except requests.exceptions.RequestException as e:
    print("Something went wrong", e)
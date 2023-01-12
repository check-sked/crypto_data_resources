import requests
import csv
from datetime import datetime

# Input name of dex you want to observe
Protocol = "sushiswap"

# Input daily or total volume
Type = "daily"

try:
    response = requests.get(f"https://api.llama.fi/summary/dexs/{Protocol}?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true&dataType={Type}Volume")
    response.raise_for_status()
    data = response.json()

    with open('dex_volume.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["date", "dex_volume"])
        for item in data["totalDataChart"]:
            timestamp = item[0]
            volume = item[1]
            date = datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d")
            writer.writerow([date, volume])
    print("Data written to dex_volume.csv")
except requests.exceptions.HTTPError as e:
    print("HTTP Error:", e)
except requests.exceptions.ConnectionError as e:
    print("Error Connecting:", e)
except requests.exceptions.Timeout as e:
    print("Timeout Error:", e)
except requests.exceptions.RequestException as e:
    print("Something went wrong", e)
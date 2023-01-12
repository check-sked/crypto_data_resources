import requests
import csv

url = "https://api.llama.fi/overview/options?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true&dataType=dailyNotionalVolume"

try:
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    with open('options_dex_names_volumes.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["name", "display_name", "change_1d", "change_7d", "change_1m", "chain"])
        for item in data["protocols"]:
            name = item["name"]
            display_name = item["displayName"]
            change_1d = item["change_1d"]
            change_7d = item["change_7d"]
            change_1m = item["change_1m"]
            chain = item["chains"][0]
            writer.writerow([name, display_name, change_1d, change_7d, change_1m, chain])
    print("Data written to options_data.csv")
except requests.exceptions.HTTPError as e:
    print("HTTP Error:", e)
except requests.exceptions.ConnectionError as e:
    print("Error Connecting:", e)
except requests.exceptions.Timeout as e:
    print("Timeout Error:", e)
except requests.exceptions.RequestException as e:
    print("Something went wrong", e)
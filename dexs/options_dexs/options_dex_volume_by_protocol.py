import requests
import csv
from datetime import datetime


def get_dex_volume():
    Protocol = input("Enter dex name: ")
    Type = input("Enter granularity type (daily or total volume): ")
    Volume = input("Enter the volume type (Notional or Premium): ")
    print("The script is running. Press CTRL + C to kill operation at any time.")

    try:
        response = requests.get(
            f"https://api.llama.fi/summary/options/{Protocol}?dataType={Type}{Volume}Volume"
        )
        response.raise_for_status()
        data = response.json()

        with open(f"{Protocol}_{Type}_{Volume}_Volume.csv", "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["date", "volume"])
            for item in data["totalDataChart"]:
                date = datetime.fromtimestamp(item[0]).strftime("%Y-%m-%d")
                volume = item[1]
                writer.writerow([date, volume])
        print(f"Data written to {Protocol}_{Type}_{Volume}_Volume.csv")
    except requests.exceptions.HTTPError as e:
        print("HTTP Error:", e)
    except requests.exceptions.ConnectionError as e:
        print("Error Connecting:", e)
    except requests.exceptions.Timeout as e:
        print("Timeout Error:", e)
    except requests.exceptions.RequestException as e:
        print("Something went wrong", e)


if __name__ == "__main__":
    get_dex_volume()

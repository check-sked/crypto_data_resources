import requests
import csv


def get_dex_names_and_volumes():
    url = "https://api.llama.fi/overview/dexs?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true&dataType=dailyVolume"
    print("The script is running. Press CTRL + C to kill operation at any time.")

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        with open("dex_names_and_volumes.csv", "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(
                ["name", "display_name", "change_1d", "change_7d", "change_1m"]
            )
            for item in data["protocols"]:
                name = item["name"]
                display_name = item["displayName"]
                change_1d = item["change_1d"]
                change_7d = item["change_7d"]
                change_1m = item["change_1m"]
                writer.writerow([name, display_name, change_1d, change_7d, change_1m])
        print("Data written to dex_names_and_volumes.csv")
    except requests.exceptions.HTTPError as e:
        print("HTTP Error:", e)
    except requests.exceptions.ConnectionError as e:
        print("Error Connecting:", e)
    except requests.exceptions.Timeout as e:
        print("Timeout Error:", e)
    except requests.exceptions.RequestException as e:
        print("Something went wrong", e)


if __name__ == "__main__":
    get_dex_names_and_volumes()

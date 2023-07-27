import csv
import requests


def write_to_csv(data, chain):
    with open(f"{chain}_volume_highlights.csv", mode="w") as csv_file:
        fieldnames = ["name", "total24h", "total7d", "total30d"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        total24h = 0
        total7d = 0
        total30d = 0
        for item in data:
            total24h += item["total24h"]
            total7d += item["total7d"]
            total30d += item["total30d"]
            writer.writerow(
                {
                    "name": item["name"],
                    "total24h": item["total24h"],
                    "total7d": item["total7d"],
                    "total30d": item["total30d"],
                }
            )
        writer.writerow(
            {
                "name": "Total",
                "total24h": total24h,
                "total7d": total7d,
                "total30d": total30d,
            }
        )


def get_data(chain):
    try:
        response = requests.get(
            f"https://api.llama.fi/overview/dexs/{chain}?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true&dataType=dailyVolume"
        )
        response.raise_for_status()
        protocols = response.json()["protocols"]
        data = []
        for protocol in protocols:
            data.append(
                {
                    "name": protocol["name"],
                    "total24h": protocol["total24h"],
                    "total7d": protocol["total7d"],
                    "total30d": protocol["total30d"],
                }
            )
        return data
    except requests.exceptions.HTTPError as errh:
        print("Http Error:", errh)
    except requests.exceptions.ConnectionError as errc:
        print("Error Connecting:", errc)
    except requests.exceptions.Timeout as errt:
        print("Timeout Error:", errt)
    except requests.exceptions.RequestException as err:
        print("Something went wrong:", err)


def main():
    chain = input("Enter chain: ")
    print("The script is running. Press CTRL + C to kill operation at any time.")
    data = get_data(chain)
    write_to_csv(data, chain)
    print(f"Data written to {chain}_volume_highlights.csv")


if __name__ == "__main__":
    main()

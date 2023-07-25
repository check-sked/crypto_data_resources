import requests
import csv
from datetime import datetime


def get_protocols(category):
    protocols = []
    response = requests.get("https://api.llama.fi/protocols")
    if response.status_code == 200:
        protocols_data = response.json()
        for protocol in protocols_data:
            if protocol["category"] == category:
                protocols.append(protocol["name"].replace(" ", "-"))
    return protocols


def get_protocol_tvl(protocol):
    tvl = []
    response = requests.get(f"https://api.llama.fi/protocol/{protocol}")
    if response.status_code == 200:
        tvl_data = response.json()["tvl"]
        for data in tvl_data:
            date = datetime.fromtimestamp(data["date"]).strftime("%Y-%m-%d")
            tvl.append({"date": date, "totalLiquidityUSD": data["totalLiquidityUSD"]})
    return tvl


def main():
    category = input("Enter a category: ")
    protocols = get_protocols(category)
    data = {}
    for protocol in protocols:
        data[protocol] = get_protocol_tvl(protocol)

    with open(f"{category}_tvl.csv", "w", newline="") as csvfile:
        fieldnames = ["date"] + protocols
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        dates = set()
        for protocol in protocols:
            for d in data[protocol]:
                dates.add(d["date"])
        for date in sorted(dates):
            row = {"date": date}
            for protocol in protocols:
                for d in data[protocol]:
                    if d["date"] == date:
                        row[protocol] = d["totalLiquidityUSD"]
                        break
            writer.writerow(row)
        print(f"Data written to {category}_tvl.csv")


if __name__ == "__main__":
    main()

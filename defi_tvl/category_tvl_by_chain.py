import requests
import csv
import time
from datetime import datetime, timedelta
from requests.exceptions import ConnectionError, HTTPError, JSONDecodeError


def get_protocols(category, chain):
    try:
        response = requests.get("https://api.llama.fi/protocols")
        data = response.json()
    except ConnectionError as e:
        print(f"Connection error occurred: {e}")
        return []
    protocols = []
    for item in data:
        if item["category"] == category and chain in item["chains"]:
            protocols.append(item["slug"].replace(" ", "-"))
    return protocols


def get_tvl(protocol_name, chain):
    try:
        response = requests.get(f"https://api.llama.fi/protocol/{protocol_name}")
        response.raise_for_status()  # raise exception if invalid response
        data = response.json()
    except (ConnectionError, HTTPError) as e:
        print(f"Connection or HTTP error occurred for protocol: {protocol_name}. {e}")
        return None
    except JSONDecodeError:
        print(f"No data was returned for protocol: {protocol_name}")
        return None
    if "chainTvls" not in data or chain not in data["chainTvls"]:
        return []
    tvl = []
    for item in data["chainTvls"][chain]["tvl"]:
        date = datetime.fromtimestamp(item["date"]).strftime("%Y-%m-%d")
        tvl.append({"date": date, "totalLiquidityUSD": item["totalLiquidityUSD"]})
    return tvl


def main():
    category = input("Enter category: ")
    chain = input("Enter chain: ")
    days = int(input("Enter number of days: "))  # get number of days as input
    try:
        protocols = get_protocols(category, chain)
        if not protocols:
            print(
                "No results produced. Check to make sure you input Category, Chain, and Days correctly. If the problem persists, the chain <> category combination doesn't exist."
            )
            return
    except Exception as e:
        print(
            "No results produced. Check to make sure you input Category, Chain, and Days correctly. If the problem persists, the chain <> category combination doesn't exist."
        )
        print(f"Error details: {str(e)}")
        return

    failed_protocols = set()
    with open(f"{chain}_{category}_TVL.csv", "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["date"] + protocols + ["Total"])
        writer.writeheader()
        for i in range(days):  # use user-specified number of days
            row = {}
            row["date"] = (datetime.today() - timedelta(days=i)).strftime("%Y-%m-%d")
            total = 0
            for protocol_name in protocols:
                if protocol_name in failed_protocols:
                    continue
                tvl = get_tvl(protocol_name, chain)
                if tvl is None:
                    failed_protocols.add(protocol_name)
                    continue
                for item in tvl:
                    if item["date"] == row["date"]:
                        row[protocol_name] = "${:,.2f}".format(
                            item["totalLiquidityUSD"]
                        )
                        total += item["totalLiquidityUSD"]
                        break
            row["Total"] = "${:,.2f}".format(total)
            writer.writerow(row)
            progress_percentage = (
                (i + 1) / days * 100
            )  # calculate progress percentage based on user input
            print(
                f"{i+1} days of data have been produced. Your request is {progress_percentage}% complete."
            )
    print(f"Data written to {chain}_{category}_TVL.csv!")


if __name__ == "__main__":
    main()

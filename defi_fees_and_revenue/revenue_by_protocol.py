import csv
import requests
from datetime import datetime
from collections import defaultdict


def main():
    # Input protocol to observe. Reference protocols_list_fees.csv for available protocols.
    Protocol = input("Enter the protocol: ")

    # Input type (daily or total - no space and no caps)
    Type = input("Enter the type (daily or total): ")

    response = requests.get(
        f"https://api.llama.fi/summary/fees/{Protocol}?dataType={Type}Revenue"
    )
    data = response.json()

    all_chains = set()
    all_versions = set()
    breakdown = defaultdict(lambda: defaultdict(int))
    for day in data["totalDataChartBreakdown"]:
        timestamp = day[0]
        date = datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d")
        for chain, fees_by_version in day[1].items():
            all_chains.add(chain)
            for version, fees in fees_by_version.items():
                all_versions.add(version)
                breakdown[date][chain + "_" + version] += fees

    csv_filename = f"{Protocol}_{Type}_revenue.csv"  # Filename with protocol and type

    with open(csv_filename, mode="w", newline="") as csv_file:
        fieldnames = (
            ["date"]
            + sorted(
                [
                    chain + "_" + version
                    for chain in all_chains
                    for version in all_versions
                ]
            )
            + ["total_fees"]
        )
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        print(f"Data written to {csv_filename}")

        for date, fees_by_chain in breakdown.items():
            row = {"date": date}
            total_fees = 0
            for chain in all_chains:
                for version in all_versions:
                    key = chain + "_" + version
                    row[key] = fees_by_chain.get(key, 0)
                    total_fees += fees_by_chain.get(key, 0)
            row["total_fees"] = total_fees
            writer.writerow(row)


if __name__ == "__main__":
    main()

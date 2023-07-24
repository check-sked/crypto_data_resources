import csv
import requests


def main():
    url = "https://api.llama.fi/overview/fees?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true&dataType=dailyFees"

    response = requests.get(url)
    data = response.json()

    with open("protocols_list_fees.csv", mode="w", newline="") as csv_file:
        fieldnames = ["name", "category"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        print("Data written to protocols_list_fees.csv")

        for protocol in data["protocols"]:
            writer.writerow(
                {"name": protocol["name"], "category": protocol["category"]}
            )


if __name__ == "__main__":
    main()

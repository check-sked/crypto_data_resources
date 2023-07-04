import csv
import requests
import datetime


def main():
    chart_name = "estimated-transaction-volume"
    timespan = "3years"

    try:
        response = requests.get(
            f"https://api.blockchain.info/charts/{chart_name}?timespan={timespan}"
        )
        data = response.json()
    except requests.exceptions.RequestException as e:
        print("Error: Could not connect to endpoint")
        print("Error details:", e)
        exit()
    except ValueError as e:
        print("Error: Could not parse JSON response")
        print("Error details:", e)
        exit()

    points = data["values"]

    with open("blockchain.com.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)

        writer.writerow(["date", chart_name])

        for point in points:
            date_string = datetime.datetime.fromtimestamp(point["x"]).strftime(
                "%Y-%m-%d"
            )
            writer.writerow([date_string, point["y"]])

    print("Data written to blockchain.com.csv")


if __name__ == "__main__":
    main()

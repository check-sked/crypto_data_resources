import csv
import requests
import datetime


def main():
    chart_name = input("Enter the chart name (don't forget to include the dashes): ")
    timespan = input("Enter the timespan (Choose 3years, 6months, 1year, or all): ")

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

    csv_filename = f"blockchain.com_{chart_name}_{timespan}.csv"

    with open(csv_filename, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)

        writer.writerow(["date", chart_name])

        for point in points:
            date_string = datetime.datetime.fromtimestamp(point["x"]).strftime(
                "%Y-%m-%d"
            )
            writer.writerow([date_string, point["y"]])

    print(f"Data written to {csv_filename}")


if __name__ == "__main__":
    main()

import csv # For csv file creation
import requests # For get request
import datetime  # For date reformat

# Name of chart that contains data
chart_name = "estimated-transaction-volume"

# Desired timespan; leave blank for default 1year (1month, 3month, 6month, 1year, 3years, all)
timespan = "3years"

# Make a request to the endpoint
response = requests.get(f"https://api.blockchain.info/charts/{chart_name}?timespan={timespan}")

# Parse the JSON response
data = response.json()

# Extract the data points from the response
points = data["values"]

# Open a file for writing
with open("blockchain.com.csv", "w", newline="") as csvfile:
    # Create a CSV writer
    writer = csv.writer(csvfile)

    # Write the header row
    writer.writerow(["date", chart_name])

    # Write the data rows
    for point in points:
        # Convert unix timestamp to formatted date string
        date_string = datetime.datetime.fromtimestamp(point["x"]).strftime("%Y-%m-%d %H:%M:%S")
        writer.writerow([date_string, point["y"]])
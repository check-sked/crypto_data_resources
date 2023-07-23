import requests
import openpyxl

# Set API key and parameters
api_key = "0da13dd9-4db8-45a5-a885-39431d8e3234"
params = {
    "slug": "bitcoin,ethereum,cardano",
    "convert": "USD",
    "start": "2022-01-01",  # Start date input
    "end": "2022-12-31",  # End date input
}

# Set base URL for API endpoint
base_url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/historical"

# Make API request and get response
response = requests.get(base_url, params=params, headers={"X-CMC_PRO_API_KEY": api_key})

# Print response data and HTTP status code
print(response.json())
print(response.status_code)

# Check if the API response has an error
data = response.json()
if "status" in data and "error_code" in data["status"]:
    error_code = data["status"]["error_code"]
    error_message = data["status"]["error_message"]
    print(f"Error: {error_code} - {error_message}")
    exit()

# Parse response data and extract relevant information
prices = []
for currency, info in data.items():
    for date, daily_info in info["quote"]["USD"].items():
        name = info["name"]
        symbol = info["symbol"]
        price = daily_info["close"]
        prices.append([name, symbol, date, price])

# Create a new Excel workbook and add a sheet
workbook = openpyxl.Workbook()
worksheet = workbook.active

# Write data to the sheet
worksheet.append(["Name", "Symbol", "Date", "Price"])
for price in prices:
    worksheet.append(price)

# Save the Excel file
workbook.save("coinmarketcap_prices_historical.xlsx")

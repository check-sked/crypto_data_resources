import requests
import csv
import datetime

# Mapping of stablecoin input values to the corresponding values fed into the request
STABLECOIN_MAPPING = {
    "USDP": "paxos-standard",
    "usdx": "usdx",
    "USDT": "tether",
    "BUSD": "binance-usd",
    "OUSD": "origin-dollar",
    "GUSD": "gemini-dollar",
    "MUSD": "musd",
    "NUSD": "nusd",
    "UST": "terrausd",
    "DAI": "dai",
    "USDJ": "just-stablecoin",
    "HUSD": "husd",
    "FRAX": "frax",
    "CUSD": "celo-dollar",
    "USDK": "usdk",
    "RSV": "reserve",
    "USDC": "usd-coin",
    "neutrino": "neutrino",
    "TUSD": "true-usd",
    "USDP": "usdp",
}


def create_stablecoin_prices_csv(stablecoin_name, off_peg_threshold):
    # Check if the stablecoin name is valid
    if stablecoin_name not in STABLECOIN_MAPPING:
        print(f"Invalid stablecoin name: {stablecoin_name}")
        return

    # Make a request to the stablecoin prices endpoint
    response = requests.get("https://stablecoins.llama.fi/stablecoinprices")

    # Check that the request was successful
    if response.status_code == 200:
        # The request was successful, so parse the data
        data = response.json()

        # Extract the list of prices
        prices = data

        # Get the corresponding stablecoin value to feed into the request
        stablecoin_value = STABLECOIN_MAPPING[stablecoin_name]

        # Prepare the CSV file name
        csv_file_name = f"{stablecoin_name}_off_peg.csv"

        # Open the CSV file for writing
        with open(csv_file_name, "w", newline="") as csvfile:
            # Create a CSV writer
            writer = csv.writer(csvfile)

            # Write the header row
            writer.writerow(["Date", stablecoin_name, "% off peg"])

            # Write a row for each date
            for date_prices in prices:
                # Convert the Unix timestamp date to a human-readable date
                date = datetime.datetime.fromtimestamp(date_prices["date"]).strftime(
                    "%Y-%m-%d"
                )

                # Get the price for the specified stablecoin
                if stablecoin_value in date_prices["prices"]:
                    price = date_prices["prices"][stablecoin_value]
                else:
                    # Use the previous day's price as the placeholder value
                    price = 0

                # Calculate the "% off peg" value as a percentage
                off_peg = (price - 1) / 1 * 100

                # Check if the stablecoin is off peg by at least the given threshold
                if (off_peg_threshold >= 0 and off_peg >= off_peg_threshold) or (
                    off_peg_threshold < 0 and off_peg <= off_peg_threshold
                ):
                    # Write the data to the CSV file
                    writer.writerow([date, price, off_peg])

        # CSV successfully created
        print(
            f"CSV successfully created for {stablecoin_name}! File name: {csv_file_name}"
        )
    else:
        # There was an error with the request
        print(f"Request failed with status code {response.status_code}")


if __name__ == "__main__":
    stablecoin_name = input("Enter the stablecoin name: ")
    off_peg_threshold = float(input("Enter the % off peg threshold: "))
    create_stablecoin_prices_csv(stablecoin_name, off_peg_threshold)

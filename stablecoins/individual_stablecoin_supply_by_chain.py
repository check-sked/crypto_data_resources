import requests
import csv
import datetime

# Input ID of stablecoin. IDs of each stablecoin can be found in stablecoin_dictionary.py
ID = input("Enter the stablecoin ID: ")

# Choose between 'Circulating' and 'Minted'
value_type = ""
while value_type.lower() not in ["circulating", "minted"]:
    value_type = input("Choose between 'Circulating' and 'Minted': ")

response = requests.get(f'https://stablecoins.llama.fi/stablecoin/{ID}')
data = response.json()

if "chainBalances" in data:
    symbol = data["symbol"]
    print(f"data written to stablecoin_{symbol}_{value_type.lower()}_by_chain.csv")
    with open(f'stablecoin_{symbol}_{value_type.lower()}_by_chain.csv', 'w', newline='') as file:

        # Create a list of unique chain names to use as headers
        chain_names = list(data["chainBalances"].keys())
        header = ["Date"] + [f"{chain_name}_{value_type}" for chain_name in chain_names]
        
        # Write the header to the CSV file
        writer = csv.DictWriter(file, fieldnames=header)
        writer.writeheader()

        # Collect unique dates
        unique_dates = set()
        for chain_name, chain_data in data["chainBalances"].items():
            for date_data in chain_data["tokens"]:
                date = datetime.datetime.fromtimestamp(date_data["date"]).strftime("%Y-%m-%d %H:%M:%S")
                unique_dates.add(date)

        # Initialize an empty dictionary with default values for each chain's selected value type
        combined_data = {}
        for date in unique_dates:
            combined_data[date] = {"Date": date}
            for chain_name in chain_names:
                combined_data[date].update({f"{chain_name}_{value_type}": 0})

        # Update the values in the dictionary with the data
        for chain_name, chain_data in data["chainBalances"].items():
            for date_data in chain_data["tokens"]:
                date = datetime.datetime.fromtimestamp(date_data["date"]).strftime("%Y-%m-%d %H:%M:%S")
                value = date_data[value_type.lower()]["peggedUSD"]
                
                combined_data[date].update({f"{chain_name}_{value_type}": value})

        # Sort the combined data by date
        sorted_data = sorted(combined_data.values(), key=lambda x: x["Date"])

        # Write the sorted data to the CSV file
        for row in sorted_data:
            writer.writerow(row)
else:
    print("ChainBalances field not found in the JSON response")

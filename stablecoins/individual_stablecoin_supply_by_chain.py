import requests
import csv
import datetime

STABLECOIN_MAPPING = {
    "USDT": 1,
    "USDC": 2,
    "USTC": 3,
    "BUSD": 4,
    "DAI": 5,
    "FRAX": 6,
    "TUSD": 7,
    "LUSD": 8,
    "FEI": 9,
    "MIM": 10,
    "USDP": 11,
    "USDN": 12,
    "YUSD": 13,
    "USDD": 14,
    "DOLA": 15,
    "PAI": 16,
    "HUSD": 17,
    "NUSD": 18,
    "GUSD": 19,
    "ALUSD": 20,
    "FLEXUSD": 21,
    "SUSD": 22,
    "OUSD": 23,
    "CUSD": 24,
    "RSV": 25,
    "MUSD": 26,
    "USDK": 27,
    "VAI": 28,
    "TOR": 29,
    "DOC": 30,
    "USDS": 31,
    "USDP": 33,
    "USDB": 34,
    "MAI": 35,
    "USDR": 36,
    "USDJ": 37,
    "STBL": 38,
    "VOLT": 39,
    "RAI": 40,
    "FLOAT": 41,
    "USDX": 42,
    "ZUSD": 43,
    "USX": 44,
    "AUSD": 45,
    "USD+": 46,
    "DEI": 47,
    "BAI": 48,
    "EURT": 49,
    "EUROC": 50,
    "EURS": 51,
    "CEUR": 52,
    "SEUR": 53,
    "USN": 54,
    "AGEUR": 55,
    "PAR": 56,
    "USH": 57,
    "3USD": 58,
    "SIGUSD": 59,
    "HOME": 60,
    "FIAT": 61,
    "PUSD": 62,
    "FUSD": 63,
    "UXD": 64,
    "USDH": 65,
    "FPI": 66,
    "BEAN": 67,
    "USDL": 68,
    "PUSD": 69,
    "DUSD": 70,
    "VST": 71,
    "KUSD": 72,
    "USDTZ": 73,
    "MONEY": 74,
    "UUSD": 75,
    "USDI": 76,
    "EURL": 77,
    "NOTE": 78,
    "HAY": 79,
    "USK": 81,
    "ARUSD": 82,
    "USDW": 83,
    "BOB": 84,
    "USDR": 85,
    "UZD": 86,
    "USDI": 87,
    "IUSD": 88,
    "XAI": 89,
    "RUSD": 90,
    "IBEUR": 91,
    "PINA": 92,
    "DJED": 93,
    "BAOUSD": 94,
    "CMST": 95,
    "CUSD": 96,
    "USP": 97,
    "EUROe": 98,
    "CASH": 99,
    "DSU": 100,
    "EURE": 101,
    "ANONUSD": 102,
    "NXUSD": 103,
    "DAVOS": 104,
    "DCHF": 105,
    "EUSD": 106,
    "CZUSD": 107,
    "d2O": 108,
    "EUSD": 109,
    "crvUSD": 110,
    "DAI+": 111,
    "USDT+": 112,
    "SILK": 113,
    "clevUSD": 114,
    "R": 115,
}


def save_stablecoin_data_to_csv(stablecoin_id, value_type):
    endpoint = f"https://stablecoins.llama.fi/stablecoin/{stablecoin_id}"
    response = requests.get(endpoint)
    data = response.json()

    if "chainBalances" in data:
        symbol = data["symbol"]
        csv_file = f"stablecoin_{symbol}_{value_type.lower()}_by_chain.csv"

        with open(csv_file, mode="w", newline="") as file:
            writer = csv.writer(file)
            chain_names = list(data["chainBalances"].keys())
            header = ["Date"] + [
                f"{chain_name}_{value_type}" for chain_name in chain_names
            ]
            writer.writerow(header)

            unique_dates = set()
            for chain_name, chain_data in data["chainBalances"].items():
                for date_data in chain_data["tokens"]:
                    date = datetime.datetime.fromtimestamp(date_data["date"]).strftime(
                        "%Y-%m-%d %H:%M:%S"
                    )
                    unique_dates.add(date)

            combined_data = {date: {"Date": date} for date in unique_dates}
            for chain_name, chain_data in data["chainBalances"].items():
                for date_data in chain_data["tokens"]:
                    date = datetime.datetime.fromtimestamp(date_data["date"]).strftime(
                        "%Y-%m-%d %H:%M:%S"
                    )
                    value = date_data[value_type.lower()]["peggedUSD"]
                    combined_data[date][f"{chain_name}_{value_type}"] = value

            sorted_data = sorted(combined_data.values(), key=lambda x: x["Date"])

            # Add debug print statements to investigate combined_data
            # print(f"Combined Data: {combined_data}")

            for row in sorted_data:
                # print(f"Row: {row}")
                writer.writerow([row.get(column_name, 0) for column_name in header])

        print(f"Data saved to {csv_file} successfully.")
    else:
        print("ChainBalances field not found in the JSON response.")


if __name__ == "__main__":
    stablecoin_name = input("Enter the stablecoin name: ")
    value_type = ""
    while value_type.lower() not in ["circulating", "minted"]:
        value_type = input("Choose between 'Circulating' and 'Minted': ")

    if stablecoin_name in STABLECOIN_MAPPING:
        stablecoin_id = STABLECOIN_MAPPING[stablecoin_name]
        save_stablecoin_data_to_csv(stablecoin_id, value_type)
    else:
        print("Invalid stablecoin name.")

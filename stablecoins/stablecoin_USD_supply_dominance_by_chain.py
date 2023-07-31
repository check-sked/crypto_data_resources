import requests
import csv
from datetime import datetime

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


def save_stablecoin_supply_dominance_csv(chain, stablecoin):
    # Retrieve the stablecoin ID from the mapping
    stablecoin_id = STABLECOIN_MAPPING.get(stablecoin)
    if stablecoin_id is None:
        print("Invalid stablecoin.")
        return

    # Make requests to the endpoints
    response1 = requests.get(
        f"https://stablecoins.llama.fi/stablecoincharts/{chain}?stablecoin={stablecoin_id}"
    )
    response2 = requests.get(f"https://stablecoins.llama.fi/stablecoincharts/{chain}")

    # Check if the request was successful
    if response1.status_code != 200 or response2.status_code != 200:
        print(
            f"Request failed with status codes: {response1.status_code}, {response2.status_code}"
        )
        return

    # Parse the JSON data
    data1 = response1.json()
    data2 = response2.json()

    # Create an empty list to hold the data
    rows = []

    # Loop through the data and append the "peggedUSD" and date to the list
    for item in data1:
        date = datetime.fromtimestamp(int(item["date"])).strftime("%Y-%m-%d %H:%M:%S")
        peggedUSD = item["totalCirculatingUSD"].get("peggedUSD")
        if not peggedUSD:
            peggedUSD = item["totalCirculatingUSD"].get("peggedEUR")
        if peggedUSD:
            rows.append([date, peggedUSD, ""])

    for item in data2:
        date = datetime.fromtimestamp(int(item["date"])).strftime("%Y-%m-%d %H:%M:%S")
        peggedUSD = item["totalCirculatingUSD"].get("peggedUSD")
        if not peggedUSD:
            peggedUSD = item["totalCirculatingUSD"].get("peggedEUR")
        if peggedUSD:
            for row in rows:
                if row[0] == date:
                    row[2] = peggedUSD

    # Add the "stablecoin_dominance" column
    for row in rows:
        if row[1] and row[2]:
            stablecoin_dominance = (row[1] / row[2]) * 100
            row.append("{:.2f}%".format(stablecoin_dominance))
        else:
            row.append("N/A")

    # Write the data to a CSV file
    filename = f"{chain}_{stablecoin}_USD_supply_dominance.csv"
    with open(filename, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(
            [
                "Date",
                "Individual_Stablecoin_Supply",
                "Total_Chain_Supply",
                "stablecoin_dominance",
            ]
        )
        writer.writerows(rows)

    print(f"Data written to {filename} successfully.")


if __name__ == "__main__":
    chain = input("Enter the chain: ")
    stablecoin = input("Enter the stablecoin: ")
    save_stablecoin_supply_dominance_csv(chain, stablecoin)

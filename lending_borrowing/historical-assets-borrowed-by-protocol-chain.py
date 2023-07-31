import requests
import pandas as pd
from datetime import datetime


def main():
    # Input protocol name
    Protocol_Name = input("Enter lending protocol (Aave, Compound, Venus, etc.): ")

    # Input chain
    chain = input("Enter chain (Ethereum, Optimism, Aptos, etc.): ")

    print("The script is running. Press CTRL + C to kill operation at any time.")

    # Make a GET request to the API endpoint
    response = requests.get(f"https://api.llama.fi/protocol/{Protocol_Name}")

    # Convert the response to a dictionary
    data = response.json()

    # Prepare dictionary to hold final data
    final_data = {}

    # Get TVL data
    tvl_data = data["chainTvls"].get(chain, {}).get("tvl", [])

    # Get borrowed data
    borrowed_data = data["chainTvls"].get(f"{chain}-borrowed", {}).get("tvl", [])

    # Process TVL data
    for item in tvl_data:
        date = datetime.utcfromtimestamp(item["date"]).strftime("%Y/%m/%d")
        if date not in final_data:
            final_data[date] = {"date": date}
        final_data[date][f"{chain}_TVL"] = "${:,.2f}".format(item["totalLiquidityUSD"])

    # Process borrowed data
    for item in borrowed_data:
        date = datetime.utcfromtimestamp(item["date"]).strftime("%Y/%m/%d")
        if date not in final_data:
            final_data[date] = {"date": date}
        final_data[date][f"{chain}_borrowed"] = "${:,.2f}".format(
            item["totalLiquidityUSD"]
        )

    # Create DataFrame from final data
    df = pd.DataFrame(final_data.values())

    # Write the resulting dataframe to a csv file
    df.to_csv(
        f"{Protocol_Name}_{chain}_borrowed_tvl.csv",
        index=False,
        columns=[
            "date",
            f"{chain}_borrowed",
            f"{chain}_TVL",
        ],  # ensure the correct column order
    )
    print(f"data written to {Protocol_Name}_{chain}_borrowed_tvl.csv!")


if __name__ == "__main__":
    main()

import requests
import pandas as pd


def main():
    # Input chain to observe
    Chain = input("Enter a chain: ")

    # Time frame to observe (daily or weekly)
    Time = input("Enter the type (daily or total): ")

    response = requests.get(
        f"https://api.llama.fi/overview/fees/{Chain}?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true&dataType={Time}Revenue"
    )
    data = response.json()

    # Initialize an empty list to store the data
    rows = []

    for protocol in data["protocols"]:
        # Append a new row to the list for each protocol
        row = {
            "protocol_name": protocol["name"],
            "total24h": protocol["total24h"],
            "change_1d": protocol["change_1d"],
            "change_7d": protocol["change_7d"],
            "change_1m": protocol["change_1m"],
        }
        rows.append(row)

    # Create a pandas DataFrame from the list of rows
    df = pd.DataFrame(rows)

    # Reorder the columns to make the protocol name the first column
    df = df[["protocol_name", "total24h", "change_1d", "change_7d", "change_1m"]]

    # Write the DataFrame to a CSV file with Chain name in the filename
    csv_filename = f"{Chain}_{Time}_revenue_breakdown.csv"
    df.to_csv(csv_filename, index=False)
    print(f"Data written to {csv_filename}")


if __name__ == "__main__":
    main()

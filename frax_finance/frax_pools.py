import requests
import csv


def main():
    print("The script is running. Press CTRL + C to kill operation at any time.")

    # Make GET request to Frax API endpoint
    response = requests.get("https://api.frax.finance/pools")
    data = response.json()

    # Sort data by apy in descending order
    data = sorted(data, key=lambda x: x["apy"], reverse=True)

    # Write data to CSV file
    with open("frax_asset_pools.csv", mode="w") as file:
        writer = csv.writer(file)
        headers = [
            "chain",
            "platform",
            "pool_tokens",
            "pool_rewards",
            "liquidity_locked",
            "apy (%)",
            "apy_max (%)",
        ]
        writer.writerow(headers)
        print("data written to frax_asset_pools.csv")
        for pool in data:
            writer.writerow(
                [
                    pool["chain"],
                    pool["platform"],
                    pool["pool_tokens"],
                    pool["pool_rewards"],
                    "${:,.2f}".format(float(pool["liquidity_locked"])),
                    "{:.2%}".format(pool["apy"] / 100),
                    "{:.2%}".format(pool["apy_max"] / 100),
                ]
            )


if __name__ == "__main__":
    main()

import csv
import requests


def main():
    # Input protocol to observe
    Lending_Protocol = input("Enter the lending protocol: ")
    print("The script is running. Press CTRL + C to kill operation at any time.")
    try:
        # Retrieve data from API
        response = requests.get(f"https://api.llama.fi/protocol/{Lending_Protocol}")
        response.raise_for_status()
        data = response.json()

        # Create a dictionary to hold the chain data
        chain_data = {}

        # Iterate through the currentChainTvls data
        for key, value in data["currentChainTvls"].items():
            if "-borrowed" not in key:
                continue
            # Split the key by '-' to get the chain name
            chain = key.split("-")[0]

            # Check if the chain is already in the dictionary
            if chain not in chain_data:
                # If not, add the chain to the dictionary with the value
                chain_data[chain] = value
            else:
                # If it is, add the value to the existing value
                chain_data[chain] += value

        # Add a total column
        chain_data["Total"] = sum(chain_data.values())

        # Write the data to a CSV file
        with open(f"{Lending_Protocol}_assets_borrowed_by_chain.csv", mode="w") as file:
            writer = csv.writer(file)
            writer.writerow(["Chain", "Borrowed Assets"])
            for key, value in chain_data.items():
                writer.writerow(
                    [key, "${:,.2f}".format(value)]
                )  # Format the number as a currency

    except requests.exceptions.HTTPError as errh:
        print("HTTP Error:", errh)
    except requests.exceptions.ConnectionError as errc:
        print("Error Connecting:", errc)
    except requests.exceptions.Timeout as errt:
        print("Timeout Error:", errt)
    except requests.exceptions.RequestException as err:
        print("Something went wrong:", err)


if __name__ == "__main__":
    main()

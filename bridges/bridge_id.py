import requests
import csv


def bridge_info():
    endpoint = "https://bridges.llama.fi/bridges?includeChains=true"

    response = requests.get(endpoint)
    data = response.json()

    csv_file = "bridges.csv"

    with open(csv_file, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "ID", "Chains"])

        bridges = data["bridges"]
        for bridge in bridges:
            name = bridge["name"]
            bridge_id = bridge["id"]
            chains = ", ".join(
                bridge["chains"]
            )  # Convert the list of chains to a single string
            writer.writerow([name, bridge_id, chains])

    print("The script is running. Press CTRL + C to kill operation at any time.")
    print(f"Data saved to {csv_file} successfully.")


if __name__ == "__main__":
    bridge_info()

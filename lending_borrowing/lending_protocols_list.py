import csv
import requests


def main():
    try:
        # Retrieve data from API
        response = requests.get("https://api.llama.fi/protocols")
        response.raise_for_status()
        data = response.json()

        # Sort data alphabetically by name and by chain within name
        data = sorted(data, key=lambda x: x["name"])
        for protocol in data:
            protocol["chains"] = sorted(protocol["chains"])

        with open("protocols_list.csv", mode="w") as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Chain", "Category"])
            print("Data written to protocols_list.csv")

            for protocol in data:
                if (
                    protocol["category"] == "Lending"
                ):  # Only process protocols in the lending category
                    for chain in protocol["chains"]:
                        try:
                            writer.writerow(
                                [protocol["name"], chain, protocol["category"]]
                            )
                        except KeyError:
                            writer.writerow([protocol["name"], chain, ""])

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

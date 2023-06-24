import csv
import requests
import time


def save_historical_tvl_to_csv(chain):
    try:
        # Make a request to the endpoint
        response = requests.get(f"https://api.llama.fi/v2/historicalChainTvl/{chain}")

        # Parse the JSON response
        data = response.json()

        # Write the data to a CSV file
        with open(f"{chain}_tvl.csv", "w", newline="") as csvfile:
            fieldnames = data[0].keys()
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for entry in data:
                # Parse the date using time.strptime and reformat it using time.strftime
                date_time = time.gmtime(int(entry["date"]))
                entry["date"] = time.strftime("%B %d, %Y", date_time)
                writer.writerow(entry)
        print(f"Data written to {chain}_tvl.csv")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
    except ValueError as e:
        print(f"Error: {e}")
    except KeyError as e:
        print(f"Error: {e}")
    except OSError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    # Input chain name
    chain = input("Enter a chain: ")
    save_historical_tvl_to_csv(chain)

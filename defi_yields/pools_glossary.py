import csv
import requests


def get_pools_glossary():
    print("The script is running. Press CTRL + C to kill operation at any time.")

    response = requests.get("https://yields.llama.fi/pools")
    data = response.json()

    data = sorted(data["data"], key=lambda x: (x["chain"], x["project"]))

    with open("pools_glossary.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Chain", "Project", "Symbol", "Pool_ID"])
        for item in data:
            project = item["project"]
            symbol = item["symbol"]
            pool = item["pool"]
            chain = item["chain"]
            writer.writerow([chain, project, symbol, pool])

    print("Data written to pools_glossary.csv")


if __name__ == "__main__":
    get_pools_glossary()

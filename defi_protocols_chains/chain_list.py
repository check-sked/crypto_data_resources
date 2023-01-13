import csv
import requests

def write_to_csv(data):
    with open('chains_list.csv', mode='w') as csv_file:
        fieldnames = ['name']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for item in data:
            writer.writerow({'name': item['name']})

def get_data():
    try:
        url = 'https://api.llama.fi/chains'
        response = requests.get(url)
        response.raise_for_status()
        chains = response.json()
        data = []
        for chain in chains:
            data.append({'name': chain['name']})
        return data
    except requests.exceptions.HTTPError as errh:
        print("Http Error:",errh)
    except requests.exceptions.ConnectionError as errc:
        print("Error Connecting:",errc)
    except requests.exceptions.Timeout as errt:
        print("Timeout Error:",errt)
    except requests.exceptions.RequestException as err:
        print("Something went wrong:",err)

data = get_data()
data = sorted(data, key=lambda x: x['name'].lower())
write_to_csv(data)
print("CSV file 'chains_list.csv' created successfully!")
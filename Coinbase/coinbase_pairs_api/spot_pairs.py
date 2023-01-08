import pandas as pd
import json
import requests

if __name__ == "__main__":
    """Script to query Coinbase API that produces available pairs and related data.

       Results are saved to .xlsx file in root directory.
    """
    # https://docs.cloud.coinbase.com/exchange/reference/exchangerestapi_getproducts -->  DOCUMENTATION
    endpoint = 'https://api.exchange.coinbase.com/products'  # Coinbase endpoint
    response = requests.get(endpoint)
    if response.status_code == 200:  # is request valid based on status code?
        data = json.loads(response.text)  # load response
        # JSON result to Pandas
        data_pd = pd.DataFrame(data)
        data_pd.rename(columns={'id': 'Symbol'}, inplace=True)  # rename one column to be unix
        data_pd.sort_values('Symbol', inplace=True)   # alphabetical sort
        # create Excel file that appears in root directory
        OUTPUT_FILENAME = "Coinbase_Available_Pairs.xlsx"
        data_pd.to_excel(OUTPUT_FILENAME, index=False)
    else:
        print(f"Response didn't work. \n {response.status_code}")  # kick back error if request fails
                                   
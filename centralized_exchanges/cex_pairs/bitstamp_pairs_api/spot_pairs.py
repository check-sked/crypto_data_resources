import pandas as pd
import json
import requests

if __name__ == "__main__":
    """Script to query Bitstamp API that produces available pairs and related data.

       Results are saved to .xlsx file in root directory.
    """
    # https://www.bitstamp.net/api/ -->  DOCUMENTATION
    endpoint = 'https://www.bitstamp.net/api/v2/ticker/'  # Bitstamp endpoint
    response = requests.get(endpoint)
    if response.status_code == 200:  # is request valid based on status code?
        data = json.loads(response.text)  # load response
        # JSON result to Pandas
        data_pd = pd.DataFrame(data)
        # drop columns that aren't needed
        data_pd.drop("timestamp", axis=1, inplace=True)
        data_pd.drop("open", axis=1, inplace=True)
        data_pd.drop("high", axis=1, inplace=True)
        data_pd.drop("low", axis=1, inplace=True)
        #data_pd.drop("last", axis=1, inplace=True)
        data_pd.drop("volume", axis=1, inplace=True)
        data_pd.drop("vwap", axis=1, inplace=True)
        data_pd.drop("bid", axis=1, inplace=True)
        data_pd.drop("ask", axis=1, inplace=True)
        data_pd.drop("percent_change_24", axis=1, inplace=True)
        data_pd.drop("open_24", axis=1, inplace=True)
        # alphabetical sort
        data_pd.sort_values('pair', inplace=True)   
        # create Excel file that appears in root directory
        OUTPUT_FILENAME = "Bitstamp_Available_Pairs.xlsx"
        data_pd.to_excel(OUTPUT_FILENAME, index=False)
    else:
        print(f"Response didn't work. \n {response.status_code}")  # kick back error if request fails
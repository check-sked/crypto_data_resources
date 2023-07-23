# crypto_prices

## Files and Folders Overview

### coin_gecko_prices.py

- Returns historical prices of assets input by user.
- User can also input specific time ranges.
- Both assets and time period require the code to be directly updated. After making updates, _press CTRL + S before running script_. Make sure to keep the ID tags in ' ' marks and within the brackets; also don't forget to include all dashes and other characters in the assets' IDs.
- Refer to [coin_glossary.py](https://github.com/check-sked/crypto_data_resources/blob/main/crypto_prices/coin_glossary.py) for available assets and correct ID tags. The ID tags are the values that should be input into the script. For example: To retrieve the historical price of MATIC, use ID "matic-network" in the script.
- See [here]() for example of file returned.

--

### coin_glossary.py

- Returns all of the assets on [CoinGecko](https://www.coingecko.com/) and their corresponding IDs.
- Use this script to get the IDs that are plugged into [coin_gecko_prices.py]() and to see the assets available for price retreival.
- See [here]() for example of file returned.

--

### cmc_price_current.py

- This script returns price data of assets but uses [CoinMarketCap](https://coinmarketcap.com/) as the source. The returned values are the prices of the selected assets at the time of running the script.
- This script also requires direct edits. After making updates, _press CTRL + S before running script_. Make sure asset names are in " " marks and are separated by commas and contain no spaces between asset names.
- CMC allows you to simply type the name of the asset instead of using ID tags.
- See [here]() for example of file returned.

--

### cmc_price_historical.py

- This script returns historical price data of assets but uses [CoinMarketCap](https://coinmarketcap.com/) as the source.
- This script also requires direct edits. After making updates, _press CTRL + S before running script_. Make sure asset names are in " " marks and are separated by commas and contain no spaces between asset names.
- CMC allows you to simply type the name of the asset instead of using ID tags.
- See [here]() for example of file returned.

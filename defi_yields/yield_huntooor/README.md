# yield_huntoor

## Files and Folders Overview

### pools_search_by_asset.py

- Returns list of pools based on asset input by user.
- Pools are sorted from highest APY to lowest. Pool TVLs are included in the list, in addition to the protocol they can be found on and the chain.
- See [here](https://github.com/check-sked/crypto_data_resources/blob/main/csv_examples/defi_yield/yield_huntooor/WBTC_pools.csv) for example of file returned. This example uses WBTC as input asset.

--

### pools_search.py

- Returns a CSV file cointaining all pools sorted by APY (highest to lowest). The CSV also includes the protocol they can be found on and the chain.
- See [here](https://github.com/check-sked/crypto_data_resources/blob/main/csv_examples/defi_yield/yield_huntooor/all_pools_apy_sorted.csv) for example of file returned.

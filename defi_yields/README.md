# defi_yields_and_pools

## Files and Folders Overview

### pool_apy_tvl_historical.py

- Returns historical APY and TVL of a specified pool.
- User inputs pool id, which can be found in [pools_glossary.py](https://github.com/check-sked/crypto_data_resources/blob/main/defi_yields/pools_glossary.py).
- See [here](https://github.com/check-sked/crypto_data_resources/blob/main/csv_examples/defi_yield/4399e512-4ce8-44cd-97af-13fd893b9f71_data.csv) for example of file returned.

--

### pools_glossary.py

- Returns a CSV file cointaining pools, the assets in them, the project they're connected to, and their IDs that get input in [pool_apy_tvl_historical.py.py](https://github.com/check-sked/crypto_data_resources/blob/main/defi_yields/pool_apy_tvl_historical.py).
- This file should be regenerated on a semi-regular basis to capture all new chains added to the API.
- See [here](https://github.com/check-sked/crypto_data_resources/blob/main/csv_examples/defi_yield/pools_glossary.csv) for example of file returned.

--

### yield_huntoor (Folder)

- Folder contains resources for gathering data on stablecoin / Dollar parity.
- Scripts allow users to observe stablecoin's historical peg fluctuations and choose specific periods of depegging by % disparity.
- See [here](https://github.com/check-sked/crypto_data_resources/tree/main/defi_yields/yield_huntooor) for folder.

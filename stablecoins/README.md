# stablecoins

## Files and Folders Overview

### individual_stablecoin_supply_by_chain.py

- Returns historical stablecoin supply in USD across each chain individually; Stablecoin ticker is input by user.
- User has the option to choose between circulating supply and supply minted through prompts in terminal.
- Refer to map in file or the stablecoin dictionary for acceptable input tickers.
- See [here](https://github.com/check-sked/crypto_data_resources/blob/main/csv_examples/stablecoins/stablecoin_USDT_circulating_by_chain.csv) for example of file returned.

--

### stablecoin_dictionary.py

- Returns list of all available stablecoins, their corresponding ID numbers, and stablecoin type (e.g. pegged to USD).
- The list of stablecoins and IDs returned by this file can also be found in the maps of applicable Python scripts.
- See [here](https://github.com/check-sked/crypto_data_resources/blob/main/csv_examples/stablecoins/stablecoins.csv) for example of file returned.

--

### stablecoin_native_supply_dominance_by_chain.py

- Returns historical stablecoin supply dominance by chain in native units (count of stablecoins in circulation).
- User has the option to choose specific stablecoins and chains through prompts in terminal.
- Refer to map in file or the stablecoin dictionary for acceptable input tickers.
- See [here](https://github.com/check-sked/crypto_data_resources/blob/main/csv_examples/stablecoins/Ethereum_USDC_NATIVE_supply_dominance.csv.csv) for example of file returned.

--

### stablecoin_price.py

- Returns historical prices of all available stablecoins.
- See [here](https://github.com/check-sked/crypto_data_resources/blob/main/csv_examples/stablecoins/stablecoin_prices.csv) for example of file returned.

--

### stablecoin_supply_total.py

- Returns cumulative historical stablecoin supply.
- Result includes the USD denominated value of all stablecoins and the number of native stablecoin units in circulation..
- See [here](https://github.com/check-sked/crypto_data_resources/blob/main/csv_examples/stablecoins/total_stablecoins_all_chains.csv) for example of file returned.

--

### stablecoin_USD_supply_dominance_by_chain.py

- Returns historical stablecoin supply dominance by chain denominated in USD (USD value of stablecoins in circulation).
- User has the option to choose specific stablecoins and chains through prompts in terminal.
- Refer to map in file or the stablecoin dictionary for acceptable input tickers.
- See [here](https://github.com/check-sked/crypto_data_resources/blob/main/csv_examples/stablecoins/Ethereum_USDC_USD_supply_dominance.csv) for example of file returned.

--

### total_stablecoin_supply_by_chain.py

- Returns historical stablecoin supply of a given chain.
- User has the option to input desired chain through prompts in terminal.
- See [here](https://github.com/check-sked/crypto_data_resources/blob/main/csv_examples/stablecoins/Arbitrum_stablecoin_supply.csv) for example of file returned.

--

### off_peg_analyzooor (Folder)

- Folder contains resources for gathering data on stablecoin / Dollar parity.
- Scripts allow users to observe stablecoin's historical peg fluctuations and choose specific periods of depegging by % disparity.
- See [here](https://github.com/check-sked/crypto_data_resources/tree/main/stablecoins/off_peg_analyzooor) for folder.

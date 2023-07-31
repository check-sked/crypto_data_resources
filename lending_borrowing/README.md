# lending_and_borrowing

## Files and Folders Overview

### current_assets_borrowed_by_protocol_chain.py

- Returns table of the current amount of assets borrowed by chain in USD.
- User inputs protocol name via in terminal prompts.
- See [here](https://github.com/check-sked/crypto_data_resources/blob/main/csv_examples/lending_borrowing/Compound_assets_borrowed_by_chain.csv) for example of file returned.

--

### historical_assets_borrowed_by_protocol_chain.py

- Returns historical assets borrowed sorted by protocol and chain.
- User inputs protocol and chain via in terminal prompts. Protocol <> Chain combinations can be found using [lending_protocols_list.py](https://github.com/check-sked/crypto_data_resources/blob/main/lending_borrowing/lending_protocols_list.py).
- See [here](https://github.com/check-sked/crypto_data_resources/blob/main/csv_examples/lending_borrowing/Aave_Arbitrum_borrowed_tvl.csv) for example of file returned.

--

### historical_assets_borrowed_by_protocol.py

- Returns total historical assets borrowed in USD of a protocol across all chains.
- User inputs protocol via in terminal prompts. Protocols can be found using [lending_protocols_list.py](https://github.com/check-sked/crypto_data_resources/blob/main/lending_borrowing/lending_protocols_list.py).
- See [here](https://github.com/check-sked/crypto_data_resources/blob/main/csv_examples/lending_borrowing/Aave_historical_borrowed.csv) for example of file returned.

--

### historical_cumulative_DeFi_assets_borrowed.py

- Returns the cumulative amount of assets borrowed in USD of all protocols across all chains. The results are broken down by protocol.
- Error messages will pop up, this is normal and is used to filter protocols in the API that have empty data dictionaries.
- See [here](https://github.com/check-sked/crypto_data_resources/blob/main/csv_examples/lending_borrowing/cumulative_DeFi_assets_borrowed.csv) for example of file returned.
- **This is a complex request that takes longer than other scripts. In terminal messages will guide you through completion.**

--

### lending_protocols_list.py

- Returns table of protocols and chains available for inputs in the above scripts.
- See [here](https://github.com/check-sked/crypto_data_resources/blob/main/csv_examples/lending_borrowing/protocols_list.csv) for example of file returned.

--

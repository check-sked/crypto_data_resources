# bridge_data

## Files and Folders Overview

### bridge_id.py

- Returns table with bridges, their corresponding IDs, and the chains they are available on.
- This file should be regenerated semi-regularly to capture new bridges and chains added to the API.
- See [here](https://github.com/check-sked/crypto_data_resources/blob/main/csv_examples/bridges/bridges.csv) for example of file returned.

--

### historical_bridge_data.py

- Returns historical bridge data including deposit and withdraw volume (in USD) and counts of deposit and withdrawal transactions.
- User has the option to choose an individual bridge through prompt in terminal.
- Refer to map in file for acceptable chains.
- See [here](https://github.com/check-sked/crypto_data_resources/blob/main/csv_examples/bridges/bridge_volume.csv) for example of file returned.

--

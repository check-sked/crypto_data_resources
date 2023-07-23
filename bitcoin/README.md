# blockchain_com_api

## Files and Folders Overview

### all_blockchain_com_data.py

- Returns any data point in the [_charts section of blockchain.com_](https://www.blockchain.com/explorer/charts).
- Follow these steps to use the script:

1. Choose the chart you want the data of on blockchain.com
2. Copy the name of the chart from the chart's URL (include the dashes). This can be found at the end of the URL of the desired chart. For example, copy **n-transactions-total** from the [Bitcoin Total Number of Transactions](https://www.blockchain.com/explorer/charts/n-transactions-total) chart to get the historical total # of Bitcoin transactions.
3. Run the script and paste the chart name (dashes included) into the first prompt.
4. Choose your timespan. Blockchain.com allows for 3years, 6months, 1year, or all. Note, days are skipped when "all" is selected. This is a limitation imposed by blockchain.com.

- See [here](https://github.com/check-sked/crypto_data_resources/blob/main/csv_examples/bridges/bridge_volume.csv) for example of file returned.

--

# defi_fees_and_revenue

## Files and Folders Overview

### fees_by_protocol.py

- Returns historical fees generated by chain and application + application version type. Each column is summed up for a "total fees" column.
- User inputs desired protocol and can choose between "daily" or "total" fees. Daily breaks down fees on a 24 hour basis, while total populates out the cumulative fees earned by the protocol.
- Refer to [protocol_list_fees.py](https://github.com/check-sked/crypto_data_resources/blob/main/defi_fees_and_revenue/protocols_list_fees.py) for available protocols.
- See [here](https://github.com/check-sked/crypto_data_resources/blob/main/csv_examples/defi_fees_and_revenue/Aave_daily_fees.csv) for example of file returned.

--

### protocol_fees_by_chain.py

- Returns individual fees generated of all protocols on a chain from the last 24 hours; in addition to the accompanying 1-day, 7-day, and 1-month change in fees. Change values are calculated off of the daily fees generated from the spectrum of periods. For example, the 7-day change is 9% if May 7 has 24hr fees of 99 units and May 1 had 24hr fees of 90 units.
- User inputs desired protocol and can choose between "daily" or "total" fees. Daily breaks down fees on a 24 hour basis, while total sums out the cumulative fees earned by the protocol at the time of data request.
- Refer to [protocol_list_fees.py](https://github.com/check-sked/crypto_data_resources/blob/main/defi_fees_and_revenue/protocols_list_fees.py) for available protocols.
- See [here](https://github.com/check-sked/crypto_data_resources/blob/main/csv_examples/defi_fees_and_revenue/Solana_daily_fee_breakdown.csv) for example of file returned.

--

### protocol_revenue_by_chain.py

- Returns individual revenue of all protocols on a chain from the last 24 hours; in addition to the accompanying 1-day, 7-day, and 1-month change in revenue. Change values are calculated off of the daily revenue generated from the spectrum of periods. For example, the 7-day change is 9% if May 7 has 24hr revenue of 99 units and May 1 had 24hr revenue of 90 units.
- User inputs desired protocol and can choose between "daily" or "total" revenue. Daily breaks down revenue on a 24 hour basis, while total sums out the cumulative revenue earned by the protocol at the time of data request.
- Refer to [protocol_list_fees.py](https://github.com/check-sked/crypto_data_resources/blob/main/defi_fees_and_revenue/protocols_list_fees.py) for available protocols.
- See [here](https://github.com/check-sked/crypto_data_resources/blob/main/csv_examples/defi_fees_and_revenue/Arbitrum_daily_revenue_breakdown.csv) for example of file returned.

--

### revenue_by_protocol.py

- Returns historical revenue generated by chain and application + application version type. Each column is summed up for a "total revenue" column.
- User inputs desired protocol and can choose between "daily" or "total" revenue. Daily breaks down fees on a 24 hour basis, while total populates out the cumulative fees earned by the protocol.
- Refer to [protocol_list_fees.py](https://github.com/check-sked/crypto_data_resources/blob/main/defi_fees_and_revenue/protocols_list_fees.py) for available protocols.
- See [here](https://github.com/check-sked/crypto_data_resources/blob/main/csv_examples/defi_fees_and_revenue/Compound_daily_revenue.csv) for example of file returned.

--

### protocol_list_fees.py

- Returns table of all protocols available to generate fee and revenue data from.
- **Only protocols from this list can be applied to the fees and revenue scripts.**
- This file should be regenerated on a semi-regular basis to capture all new protocols added to the API.
- See [here](https://github.com/check-sked/crypto_data_resources/blob/main/csv_examples/defi_fees_and_revenue/protocols_list_fees.csv) for example of file returned.

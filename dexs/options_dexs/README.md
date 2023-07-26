# options_dex_volumes

## Files and Folders Overview

### options_dex_name_volume.py

- Returns name of options DEX, chain, and change in volume over 1-day, 7-day, and 30-day periods.
- Change cells represent % change based on time period. For example -32.15 is the equivalent of -32.15% change over the specified period.
- See [here](https://github.com/check-sked/crypto_data_resources/blob/main/csv_examples/dexs/options_dex_names_volumes.csv) for example of file returned.

--

### options_dex_volume_by_protocol.py

- Returns historical TVL of a specified DeFi category/ sector across all chains (e.g. historical cumulative TVL of Lending sector).
- Results are broken down by protocol and summed up for a total TVL value.
- User inputs desired category and duration of analysis. Note, the dates are sorted in descending order in the file.
- Refer to [Protocols](#protocols) for available options DEXs.
- See [here](https://github.com/check-sked/crypto_data_resources/blob/main/csv_examples/dexs/Premia_daily_Notional_Volume.csv) for example of file returned.

## Protocols

**Options DEXs Available**

- Hegic
- Lyra
- Premia
- Thales

# defi_total_value_locked

## Files and Folders Overview

### category_tvl_by_chain.py

- Returns historical TVL of a specified DeFi category/ sector of a specific chain (e.g. historical TVL of Lending sector on Ethereum).
- Results are broken down by protocol and summed up for a total TVL value.
- User inputs desired category, chain, and duration of analysis. Note, the dates are sorted in descending order in the file.
- Refer to [Categories](#categories) and [Chains](#chains) for available sectors and chains. Also refer to [chain_list.py](https://github.com/check-sked/crypto_data_resources/blob/main/defi_protocols_chains/chain_list.py) for additional new chains added to API.
- See [here](https://github.com/check-sked/crypto_data_resources/blob/main/csv_examples/defi_tvl/Ethereum_CDP_TVL.csv) for example of file returned.
- **This is a complex request that uses multiple API endpoints. Some sector - chain combinations may take some time to fully render. In terminal messages will guide you through completion.**

--

### category_tvl.py

- Returns historical TVL of a specified DeFi category/ sector across all chains (e.g. historical cumulative TVL of Lending sector).
- Results are broken down by protocol and summed up for a total TVL value.
- User inputs desired category and duration of analysis. Note, the dates are sorted in descending order in the file.
- Refer to [Categories](#categories) for available sectors.
- See [here](https://github.com/check-sked/crypto_data_resources/blob/main/csv_examples/defi_tvl/RWA_TVL.csv) for example of file returned.
- **This is a complex request that uses multiple API endpoints. Some sectors may take some time to fully render. In terminal messages will guide you through completion.**

--

### chain_tvl.py

- Returns complete historical TVL of a specified chain from inception to time of request.
- User inputs desired chain.
- See [here](https://github.com/check-sked/crypto_data_resources/blob/main/csv_examples/defi_tvl/Solana_tvl.csv) for example of file returned.

--

### defi_llama_tvl.py

- Returns combined historical TVL of all chains from DeFi inception to time of request _(calculated by [DeFiLlama](https://defillama.com/))_.
- See [here](https://github.com/check-sked/crypto_data_resources/blob/main/csv_examples/defi_tvl/historical_tvl.csv) for example of file returned.

--

### protocol_tvl_by_chain.py

- Returns historical TVL of a specified protocol broken down by each chain it exists on.
- User inputs desired protocol via in terminal prompt.
- Refer to [protocols_list.py](https://github.com/check-sked/crypto_data_resources/blob/main/defi_protocols_chains/protocols_list.py) for list of available protocols.
- See [here](https://github.com/check-sked/crypto_data_resources/blob/main/csv_examples/defi_tvl/Uniswap_tvl_data.csv) for example of file returned.

--

### protocol_tvl_by_token.py

- Returns historical TVL of a specified protocol broken down by token.
- User inputs desired protocol via in terminal prompt.
- Refer to [protocols_list.py](https://github.com/check-sked/crypto_data_resources/blob/main/defi_protocols_chains/protocols_list.py) for list of available protocols.
- See [here](https://github.com/check-sked/crypto_data_resources/blob/main/csv_examples/defi_tvl/Aave_TVL_by_Token.csv) for example of file returned.
- **This is a complex request that may take some time to fully render. In terminal messages will guide you through completion.**
- **Note: there are some inconsistencies in the JSON results of DeFiLlama's API endpoint for TVL token data. Some coins produce $ amounts and some do raw token amount. Make sure to confirm results.**

--

### protocol_tvl.py

- Returns complete historical TVL of a specified protocol from inception to time of request.
- User inputs desired protocol.
- Refer to [protocols_list.py](https://github.com/check-sked/crypto_data_resources/blob/main/defi_protocols_chains/protocols_list.py) for list of available protocols.
- See [here](https://github.com/check-sked/crypto_data_resources/blob/main/csv_examples/defi_tvl/Radiant_TVL.csv) for example of file returned.

--

### tvl_all_chains.py

- Returns complete historical TVL of all chains. Results are sorted by chain.
- See [here](https://github.com/check-sked/crypto_data_resources/blob/main/csv_examples/defi_tvl/tvl_all_chains.csv) for example of file returned.
- **This is a complex request that may take some time to fully render. In terminal messages will guide you through completion.**

## Categories

**TVL Categories Available**

- Algo-Stables
- Bridge
- CDP
- CEX
- Chain
- Cross Chain
- Derivatives
- Dexes
- Farm
- Gaming
- Indexes
- Insurance
- Launchpad
- Lending
- Leveraged Farming
- Liquid Staking
- Liquidity manager
- NFT Lending
- NFT Marketplace
- Options
- Options Vault
- Oracle
- Payments
- Prediction Market
- Privacy
- Reserve Currency
- RWA
- RWA Lending
- Services
- Staking Pool
- Synthetics
- Uncollateralized Lending
- Yield
- Yield Aggregator

## Chains

**TVL Chains Available**

**A**

- Acala
- Algorand
- Aptos
- Arbitrum
- Arbitrum Nova
- Astar
- Aurora
- Avalanche

**B**

- Bifrost
- Binance
- Bitcoin
- Bitcoincash
- Bitgert
- Bitindi
- Bittorrent
- Boba
- Boba_Avax
- Boba_Bnb
- Bone

**C**

- Callisto
- Canto
- Carbon
- Cardano
- Celo
- Chihuahua
- CLV
- Comdex
- Concordium
- Conflux
- CORE
- Cosmos
- Coti
- Crab
- Crescent
- Cronos
- CSC
- Cube

**D**

- DefiChain
- Dexit
- DFK
- Doge
- Dogechain

**E**

- Echelon
- Elastos
- Elrond
- Empire
- Energi
- EnergyWeb
- ENULS
- EOS
- EOS EVM
- Equilibrium
- Ergo
- Ethereum
- EthereumClassic
- EthereumPoW
- Europa
- Everscale
- Evmos

**F**

- Fantom
- Filecoin
- Findora
- Flare
- Flow
- FunctionX
- Fuse
- Fusion

**G**

- Genshiro
- GoChain
- Godwoken
- GodwokenV1
- Goerli
- Grove

**H**

- Harmony
- Heco
- Hedera
- Heiko
- Hoo
- HPB
- Hydra

**I**

- Icon
- ICP
- Injective
- Interlay
- IoTeX

**J**

- Juno

**K**

- Kadena
- Kardia
- Karura
- Kava
- Kekchain
- Kintsugi
- Klaytn
- Kucoin
- Kujira
- Kusama

**L**

- Lachain
- Lamden
- Libre
- Litecoin
- Loop
- Lung

**M**

- Map
- Meter
- Metis
- Migaloop
- Milkomeda
- Milkomeda A1
- Mixin
- Moonbeam
- Moonriver
- MultiVAC
- MUUCHAIN

**N**

- Nahmii
- Near
- NEO
- Neutron
- Nova Network
- Nuls

**O**

- Oasis
- Oasys
- Obyte
- OKExChain
- Omax
- Ontology
- OntologyEVM
- Onus
- Optimism
- Orai
- Osmosis

**P**

- Palm
- Parallel
- Persistence
- Pokt
- Polis
- Polkadot
- Polygon
- Polygon zkEVM
- Proton
- Pulse

**Q**

- Quasar
- Quicksilver

**R**

- Rangers
- REI
- REIchain
- Rollux
- Ronin
- RSK

**S**

- Secret
- Shiden
- Sifchain
- smartBCH
- Solana
- Songbird
- Sora
- Stacks
- Stafi
- Starcoin
- Stargaze
- Starknet
- Stellar
- Step
- Stride
- Sui
- SXnetwork
- Syscoin

**T**

- Telos
- Terra
- Terra2
- Tezos
- Theta
- Thorchain
- ThunderCore
- Tlchain
- Tombchain
- TomoChain
- TON
- Tron

**U**

- Ubiq
- Ultron
- Umee

**V**

- VeChain
- Velas
- Vision
- Vite

**W**

- Wanchain
- Waves
- Wax
- WEMIX

**X**

- xDai
- XDC
- XPLA

**Z**

- Zeniq
- Zilliqa
- zkSync Era
- ZYX

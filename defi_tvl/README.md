# defi_total_value_locked

## Files and Folders Overview

### category_tvl_by_chain.py

- Returns historical TVL of a specified DeFi category/ sector of a specific chain (e.g. historical TVL of Lending sector on Ethereum).
- Results are broken down by protocol and summed up for a total TVL value.
- User inputs desired category, chain, and duration of analysis. Note, the dates are sorted in descending order in the file.
- Refer to [Categories](#categories) and [Chains](#chains) for available sectors and chains.
- See [here](https://github.com/check-sked/crypto_data_resources/blob/main/csv_examples/defi_tvl/Ethereum_CDP_TVL.csv) for example of file returned.
- **This is a complex request that uses multiple API endpoints. Some sector - chain combinations may take some time to fully render. In terminal messages will guide you through completion."**

--

### category_tvl.py

- Returns historical TVL of a specified DeFi category/ sector across all chains (e.g. historical cumulative TVL of Lending sector).
- Results are broken down by protocol and summed up for a total TVL value.
- User inputs desired category and duration of analysis. Note, the dates are sorted in descending order in the file.
- Refer to [Categories](#categories) for available sectors.
- See [here](https://github.com/check-sked/crypto_data_resources/blob/main/csv_examples/defi_tvl/RWA_TVL.csv) for example of file returned.
- **This is a complex request that uses multiple API endpoints. Some sector - chain combinations may take some time to fully render. In terminal messages will guide you through completion."**

--

### chain_tvl.py

- Returns complete historical TVL of a specified chain from inception to time of request.
- User inputs desired chain.
- See [here](https://github.com/check-sked/crypto_data_resources/blob/main/csv_examples/defi_tvl/Solana_tvl.csv) for example of file returned.

--

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

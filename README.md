# crypto-data-resources

![License](https://img.shields.io/badge/license-ISC-blue.svg)

## Table of Contents

- [Description](#description)
- [Data](#data)
- [Installation](#installation)
- [Usage](#usage)
- [Have-Questions-or-Want-to-Conntect?](#questions)

---

## Description

The crypto-data-resources repository is a data resource for crypto analysts and those curious in understanding crypto on a more granular level. It offers easily manipulatable resources for observing and visualizing the most important facets of the blockchain world and the pieces of infrastructure that comprise it.

The repository covers data on:

1. Stablecoins
2. Ethereum Layer2
3. DeFi (including TVL of dapps and chains, liquidity pools and yields, lending and borrowing, application and protocol level fees and revenues, and more)
4. Asset level trading volumes, prices and market caps
5. The Bitcoin network (including hash, on-chain transfer volume, and more)
6. The visualization and animation of the data above

Among a wide variety of other topics.

---

## Data

_The data is sourced from the most notable data platforms, DeFi protocols, and exchanges._

<a href="https://www.coinbase.com/"><img src="./assets/coinbase.webp" width="200"></a>

<a href="https://defillama.com/"><img src="./assets/defi_llama.png" width="200"></a>

<a href="https://www.blockchain.com/en/"><img src="./assets/blockchain.png" width="200"></a>

<a href="https://frax.finance/"><img src="./assets/frax.png" width="200"></a>

<a href="https://www.coingecko.com/"><img src="./assets/CoinGecko.avif" width="200"></a>

<a href="https://coinmarketcap.com/"><img src="./assets/cmc.png" width="200"></a>

<a href="https://www.binance.com/en"><img src="./assets/binance.jpeg" width="200"></a>

<a href="https://www.bitstamp.net/"><img src="./assets/bitstamp.jpeg" width="200"></a>

---

## Installation

_Instructions for installation project and setting up the development environment:_

Take the following steps to get your environment up and running:

_Mac Users_

1. Install Homebrew:
   `$ /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"`
2. Install Python: `$ brew install python`
3. Confirm that Python was installed and check your version: `python --version`

_Linux Users_

If you are using **Ubuntu 16.10 or newer**, open your command line prompt and run the following:

1. `$ sudo apt-get update`
2. `$ sudo apt-get install python3.6`

If you are using **another version of Ubuntu**, open your command line prompt and run the following:

1. `$ sudo apt-get install software-properties-common`
2. `$ sudo add-apt-repository ppa:deadsnakes/ppa`
3. `$ sudo apt-get update`
4. `$ sudo apt-get install python3.8`

If you are using **another Linux distrubution**, you likely already have Python pre-installed. If not, use your distribution’s package manager. For example on Fedora, you would use dnf in the command line:

1. `$ sudo dnf install python3`

_Windows Users_

Windows users can refer to this **[link](https://www.dataquest.io/blog/installing-python-on-windows/)** for instructions on installing Python.

_Libraries_

Each script requires its own set of libraries that must be installed to successfully retreive the data. The most consistently used ones include:

- [requests](https://pypi.org/project/requests/)
- [datetime](https://docs.python.org/3/library/datetime.html)
- [csv](https://docs.python.org/3/library/csv.html)
- [json](https://docs.python.org/3/library/json.html)
- [pandas](https://pandas.pydata.org/)

To install the libraries above, or any of the required ones, run `pip install [LIBRARY NAME]` in your environment once it is up and running. If you are using Python3, run `pip3 install [LIBRARY NAME]`

---

## Usage

_How to use the resources:_

Consult the READMEs for each individual resource to use any of the scripts contained in this repository. Once you have the script ready to go, simply run it to produce Excel or CSV files with the desired data.

Linked in each README is the documentation for corresponding the API. Refer to these links to use the scripts for your tailored needs.

---

## Questions?

Got questions or want to connect? Reach me through the following channels:

GitHub: [@check-sked](https://api.github.com/users/check-sked)

Twitter: [@Check-Sked](https://twitter.com/Check_Sked)

Newsletter and Other Content: [Medium](https://medium.com/@torusresearch)

<img src="./assets/pfp.png" alt="drawing" width="200"/>

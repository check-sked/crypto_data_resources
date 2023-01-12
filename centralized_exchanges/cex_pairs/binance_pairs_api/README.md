# binance_api

## Description

These Python scripts pull all of the active trading pairs on Binance and those with margin enabled. The documentation for the Binance API used can be found at https://binance-docs.github.io/apidocs/spot/en/#change-log.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)

## Installation

_Instructions for installation project and setting up the development environment:_

To use the script, you must first install Python if it's not on your machine and install Pandas, Requests, and Six (if applicable) modules. This can all be done from the command line of your Mac by following the steps below.

1. Install Homebrew: `$ /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"`
2. Install Python: `$ brew install python`
3. Confirm that Python was installed and check your version: `python --version`
4. Install Pandas: `pip3 install pandas`
5. Install Requests: `pip3 install requests`
6. Install Binance Client: `pip3 install python-binance`
7. Some users may also have to install the Six module: `pip3 install six`

**Note, if you aren't using Python3 then use the `pip` command instead of `pip3` when installing modules**

## Usage

_How to use the application:_

To use either of the scripts, open the `index.py` or `margin_pairs.py` files in your code editor of choice and run it. The .xlsx file containing all active trading pairs or those with margin enabled will then appear in the root directory.

## Contributing

_Take the following steps to contribute to the project._

If you would like to make adjustments or enhancements to the script, clone the repository to your local machine and share with Sked.

## Questions?

Got questions? Reach me through the following channels:

GitHub: [@check-sked](https://api.github.com/users/check-sked)

Twitter: [@Check-Sked](https://twitter.com/Check_Sked)

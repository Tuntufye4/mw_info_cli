# mw_info_cli
A command line tool for generating mw info 


## Installation

```
git clone https://github.com/Tuntufye4/mw_info_cli.git

```

Then:

```
pip install -e .

```

## Example Testing Commands

```

mwinfo health-info --district Lilongwe

mwinfo district-info --region Northern

mwinfo demographics-info --district Chitipa

mwinfo demographics-info --region Southern

mwinfo agriculture-info --crop Maize

mwinfo agriculture-info --fish Tilapia

mwinfo currency --amount 5000 --from MWK --to USD

```

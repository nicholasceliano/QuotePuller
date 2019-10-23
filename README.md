# QuotePuller
Gets quotes data from AlphaVantage API. Pulls Quote Symbols/Types from local GNUCash instance and insert into price table

1. Create /storedProcs in GNUcash database
2. Create and complete config.json in project root directory as shown below
3. Run python3 app.py from console to load current quotes into database

Config.json
{
    "gnucash": {
		"host": "",
		"user": "",
		"password": "",
		"database": ""
	},
	"alphaVantageAPIUri": "",
	"alphaVantageAPIKey": ""
}

Install locally:
- sudo pip install -e /home/pi/Documents/git/QuotePuller

Run locally
- open command and type command 'quotepuller'
#!/usr/bin/python3
import json, os
from services.quotes import Quotes
from services.mySqlDatabase import MySqlDatabase
from models.securities import Securities

config = json.load(open(os.path.join(os.path.split(os.path.abspath(__file__))[0], 'config.json')))

spResults = MySqlDatabase(config["gnucash"]).storedProc('getAllStockValues')

securities = Securities([], [])

for a in spResults:
	if a[1] == 1: # Commodity Indicator
		securities.commodities.append(a[0])
	elif a[1] == 0: # Non-Commodity
		securities.stocks.append(a[0])
	
quoteData = Quotes(config).getBatchQuotes(','.join(securities.stocks))

for q in securities.commodities:
	commodityData = Quotes(config).getCommodityQuote(q)
	quoteData.append(commodityData)

for	q in quoteData:
	print('{0}:\t{1}  \t{2}'.format(q.symbol, round(q.price, 3), q.date.strftime('%m/%d/%Y %I:%M %p')))
	
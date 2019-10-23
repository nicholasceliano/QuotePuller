
import requests, json
from quotepuller.models.securityRecord import SecurityRecord

class Quotes:
	def __init__(self, config):
		self.apiUri = config["alphaVantageAPIUri"]
		self.apiKey = config["alphaVantageAPIKey"]

	def getBatchQuotes(self, symbols):
		r = requests.get('{0}?function=BATCH_STOCK_QUOTES&symbols={1}&apikey={2}'.format(self.apiUri, symbols, self.apiKey))
		jsonResp = r.json()

		quoteData = []
		for q in jsonResp['Stock Quotes']:
			quoteData.append(SecurityRecord(q['1. symbol'], q['2. price'], q['4. timestamp']))

		return quoteData

	def getCommodityQuote(self, symbol):
		r = requests.get('{0}?function=CURRENCY_EXCHANGE_RATE&from_currency={1}&to_currency=USD&apikey={2}'.format(self.apiUri, symbol, self.apiKey))
		jsonResp = r.json()
		q = jsonResp['Realtime Currency Exchange Rate']

		commodityData = SecurityRecord(q['1. From_Currency Code'], q['5. Exchange Rate'], q['6. Last Refreshed'])
		
		return commodityData
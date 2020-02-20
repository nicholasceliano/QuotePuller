
import requests, json, time
from quotepuller.models.securityRecord import SecurityRecord

class Quotes:
	def __init__(self, config):
		self.apiUri = config["alphaVantageAPIUri"]
		self.apiKey = config["alphaVantageAPIKey"]
		self.sleepTime = 60 / config["alphaVantageReqPerMin"]

	def getQuotes(self, symbols):
		quoteData = []
		symbolsList = symbols.split(',')
		
		for q in symbolsList:
			r = requests.get('{0}?function=GLOBAL_QUOTE&symbol={1}&apikey={2}'.format(self.apiUri, q, self.apiKey))
			jsonResp = r.json()
			quote = jsonResp['Global Quote']
			quoteData.append(SecurityRecord(quote['01. symbol'], quote['05. price'], quote['07. latest trading day'], False))
			percentComplete = round(len(quoteData) / len(symbolsList) * 100, 2)
			self.printOutput(percentComplete, quote['01. symbol'])
			time.sleep(self.sleepTime)

		return quoteData

	def getCommodityQuote(self, symbol):
		r = requests.get('{0}?function=CURRENCY_EXCHANGE_RATE&from_currency={1}&to_currency=USD&apikey={2}'.format(self.apiUri, symbol, self.apiKey))
		jsonResp = r.json()
		q = jsonResp['Realtime Currency Exchange Rate']

		commodityData = SecurityRecord(q['1. From_Currency Code'], q['5. Exchange Rate'], q['6. Last Refreshed'], True)
		self.printOutput(100.0, q['1. From_Currency Code'])

		return commodityData

	def printOutput(self, percentComplete, symbol):
		print('{0}% - Successfully inserted {1}.'.format(percentComplete, symbol))
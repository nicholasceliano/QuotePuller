
import requests, json, time, csv
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
			print(jsonResp)
			quote = jsonResp['Global Quote']
			quoteData.append(SecurityRecord(quote['01. symbol'], quote['05. price'], quote['07. latest trading day']))
			time.sleep(self.sleepTime)

		return quoteData

	def getCommodityQuote(self, symbol):
		r = requests.get('{0}?function=CURRENCY_EXCHANGE_RATE&from_currency={1}&to_currency=USD&apikey={2}'.format(self.apiUri, symbol, self.apiKey))
		jsonResp = r.json()
		q = jsonResp['Realtime Currency Exchange Rate']

		commodityData = SecurityRecord(q['1. From_Currency Code'], q['5. Exchange Rate'], q['6. Last Refreshed'])
		
		return commodityData
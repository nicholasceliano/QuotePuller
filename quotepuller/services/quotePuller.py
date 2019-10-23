from quotepuller.models.securities import Securities
from quotepuller.models.gnucashStockValue import GnucashStockValue

class QuotePuller:
	gnucashStockValues = []

	def __init__(self, gnucash, mysql, quotes):
		self.gnucash = gnucash
		self.mysql = mysql
		self.quotes = quotes

	def loadQuotes(self):
		securities = self.__getTickerSymbolsFromGnuCash__()
		quoteData = self.__getSecuritiesDataFromAPI__(securities)
		self.__insertQuotesIntoGnucash__(quoteData)

	def __getTickerSymbolsFromGnuCash__(self):
		securities = Securities([], [])

		spResults = self.mysql.getStoredProc('getAllStockValues')
		for a in spResults:
			self.gnucashStockValues.append(GnucashStockValue(a))

		for a in self.gnucashStockValues:
			if a.isCommodity == 1: # Commodity Indicator
				securities.commodities.append(a.stockName)
			elif a.isCommodity == 0: # Non-Commodity
				securities.stocks.append(a.stockName)

		return securities

	def __getSecuritiesDataFromAPI__(self, securities):
		quoteData = self.quotes.getBatchQuotes(','.join(securities.stocks))

		for q in securities.commodities:
			commodityData = self.quotes.getCommodityQuote(q)
			quoteData.append(commodityData)

		return quoteData

	def __insertQuotesIntoGnucash__(self, quoteData):
		if (len(quoteData) > 0):
			currency_guid = self.gnucash.getCurrencyGUID()
			for q in quoteData:
				stockValueRec = [x for x in self.gnucashStockValues if x.stockName == q.symbol][0]
				self.gnucash.insertPriceRecord(stockValueRec.commodity_guid, currency_guid, q.date, q.price, q.symbol)
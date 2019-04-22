import requests, json, uuid
from models.gnucashPrice import GnucashPrice

class GNUCash:
	def __init__(self, mysql):
		self.mysql = mysql

	def insertPriceRecord(self, commodity_guid, currency_guid, date, price, symbol):
		priceObj = GnucashPrice(commodity_guid, currency_guid, date, price)
		insertResp = self.mysql.insertStoredProc('insertPrice', (priceObj.guid, priceObj.commodity_guid, priceObj.currency_guid, priceObj.date, priceObj.source, priceObj.type, priceObj.value_num, priceObj.value_denom))
		if (insertResp == True):
			print('{0}:\t{1}  \t{2} - Sucessfully Inserted'.format(symbol, price, priceObj.date))
		else:
			print('{0}:\t{1}  \t{2} - Error Inserting: {3}'.format(symbol, price, priceObj.date, insertResp))

	def getCurrencyGUID(self):
		return self.mysql.query_fetch_one("select distinct guid from commodities where namespace = 'CURRENCY' and mnemonic = 'USD'")

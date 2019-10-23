class GnucashStockValue:
	def __init__(self, spResult):
		self.stockName = spResult[0]
		self.commodity_guid = spResult[1]
		self.isCommodity = spResult[2]
		self.stockQty = spResult[3]
		self.stockVal = spResult[4]
		self.lastPriceDate = spResult[5]
		self.lastPriceVal = spResult[6]
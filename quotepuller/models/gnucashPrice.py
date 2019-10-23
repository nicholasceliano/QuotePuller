import uuid
from fractions import Fraction

class GnucashPrice:

	def __init__(self, commodity_guid, currency_guid, date, price):
		priceFrac = self.__calcPriceFraction__(price)

		self.guid = uuid.uuid4().hex
		self.commodity_guid = commodity_guid
		self.currency_guid = currency_guid
		self.date = date.strftime('%Y-%m-%d %H:%M:%S')
		self.source = 'user:price-editor'
		self.type = 'last'
		self.value_num = priceFrac.numerator
		self.value_denom = priceFrac.denominator

	def __calcPriceFraction__(self, price):
		num = self.__calcValueNum__(price)
		demon = self.__calcValueDemon(price)

		simplifiedFrac = Fraction(num, demon)

		return simplifiedFrac

	def __calcValueNum__(self, price):
		strPrice = str(price).replace('.','')

		if (len(strPrice) >= 10):
			strPrice = strPrice[0:10]
		else:
			for x in range(10 - len(strPrice)):
				strPrice = strPrice + '0'

		return int(strPrice)

	def __calcValueDemon(self, price):
		decimalIndex = str(price).index('.')
		denom = '1'

		for x in range(10 - decimalIndex):
			denom = denom + '0'

		return int(denom)
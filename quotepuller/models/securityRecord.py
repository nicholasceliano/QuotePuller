from decimal import Decimal
from datetime import datetime

class SecurityRecord:
	def __init__(self, symbol, price, date):
		self.symbol = symbol
		self.price = Decimal(price)
		self.date = datetime.strptime(date, '%Y-%m-%d')
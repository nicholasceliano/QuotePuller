import mysql.connector

class MySqlDatabase:
	def __init__(self, config):
		self.host = config["host"]
		self.user = config["user"]
		self.password = config["password"]
		self.database = config["database"]

	def __db(self): 
		return mysql.connector.connect(
			host=self.host,
			user=self.user,
			password=self.password,
			database=self.database
		)

	def storedProc(self, storedProcName):
		db = self.__db()
		cursor = db.cursor()
		cursor.callproc(storedProcName, args=())
		d = ''
		for result in cursor.stored_results():
			d = result.fetchall()

		return d
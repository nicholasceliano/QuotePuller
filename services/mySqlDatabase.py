from mysql.connector import MySQLConnection, Error

class MySqlDatabase:
	def __init__(self, config):
		self.host = config["host"]
		self.user = config["user"]
		self.password = config["password"]
		self.database = config["database"]

	def __db(self): 
		return MySQLConnection(
			host=self.host,
			user=self.user,
			password=self.password,
			database=self.database
		)

	def getStoredProc(self, storedProcName, procArgs=()):
		try:
			db = self.__db()
			cursor = db.cursor()

			cursor.callproc(storedProcName, procArgs)
			d = ''
			for result in cursor.stored_results():
				d = result.fetchall()

			return d
		except Error as error:
			print(error)
		finally:
			cursor.close()
			db.close()

	def insertStoredProc(self, storedProcName, procArgs=()):
		try:
			db = self.__db()
			cursor = db.cursor()
			cursor.callproc(storedProcName, procArgs)
			
			db.commit()

			return True
		except Error as error:
			return error
		finally:
			cursor.close()
			db.close()

	def query_fetch_one(self, query):
		try:
			db = self.__db()
			cursor = db.cursor()
			cursor.execute(query)
			d = ''
			d = cursor.fetchone()

			return d[0]
		except Error as error:
			print(error)
		finally:
			cursor.close()
			db.close()
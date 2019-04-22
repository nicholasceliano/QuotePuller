#!/usr/bin/python3
import json, os
from services.mySqlDatabase import MySqlDatabase
from services.gnucash import GNUCash
from services.quotes import Quotes
from services.quotePuller import QuotePuller

config = json.load(open(os.path.join(os.path.split(os.path.abspath(__file__))[0], 'config.json')))
mysqlDatabase = MySqlDatabase(config["gnucash"])
gnucash = GNUCash(mysqlDatabase)
quotes = Quotes(config)

QuotePuller(gnucash, mysqlDatabase, quotes).loadQuotes()
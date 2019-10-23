#!/usr/bin/python3
import json, os
from quotepuller.services.mySqlDatabase import MySqlDatabase
from quotepuller.services.gnucash import GNUCash
from quotepuller.services.quotes import Quotes
from quotepuller.services.quotePuller import QuotePuller

def main():
    config = json.load(open(os.path.join(os.path.split(os.path.abspath(__file__))[0], 'config.json')))
    mysqlDatabase = MySqlDatabase(config["gnucash"])
    gnucash = GNUCash(mysqlDatabase)
    quotes = Quotes(config)

    QuotePuller(gnucash, mysqlDatabase, quotes).loadQuotes()
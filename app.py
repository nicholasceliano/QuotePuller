import sys, requests, json
from bs4 import BeautifulSoup
from decimal import Decimal

config = json.load(open('config.json'))
baseUrl = config["quoteUrl"]
quoteList = config["quoteList"]
#quoteList = ['GIB', 'xauusd=X', 'IJR']
quoteResults = []

def deleteLastLine():
    sys.stdout.write('\x1b[1A')
    sys.stdout.write('\x1b[2K')

def displayStatus():
    percentDone = str(round((idx / len(quoteList)) * 100))
    deleteLastLine()
    print ('Loading...' + percentDone + '%')

def getQuote(symbol):    
    url = baseUrl + q 
    r = requests.get(url = url, params = {})

    soup = BeautifulSoup(r.text, 'html.parser')
    quoteDiv = soup.find('div', {'id': 'quote-header-info'})
    quoteValue = quoteDiv.find_all('span')[1].text.replace(',', '')

    quoteValDec = Decimal(quoteValue)
    quoteValue = round(quoteValDec, 2)

    quoteResults.append('%s: %s' % (q, quoteValue))

for idx, q in enumerate(quoteList):
    displayStatus()

    try:
        getQuote(q)
    except:
        print('Error loading quote for %s' % (q))

deleteLastLine()
print(*quoteResults, sep = '\n')
import requests
from bs4 import BeautifulSoup

#getting info from Yahoo finance 

url = 'https://finance.yahoo.com/quote/AAPL/history?period1=1435363200&period2=1593216000&interval=1mo&filter=history&frequency=1mo'

response = requests.get(url)
soup = BeautifulSoup(response.text)

soup.find_all('HistoricalPriceStore')
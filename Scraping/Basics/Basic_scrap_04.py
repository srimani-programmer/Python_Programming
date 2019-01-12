# Assignment03 ---> Scraping the mit website

import requests
import bs4

requestVariable = requests.get('http://web.mit.edu/')

soupContent = bs4.BeautifulSoup(requestVariable.text,'lxml')

contentVar = soupContent.select('body')

print(contentVar[0].getText())
# Assignment02 ---> Getting information from mee seva

import requests
import bs4

requestVariable = requests.get('http://ap.meeseva.gov.in/')

soupVariable = bs4.BeautifulSoup(requestVariable.text,'lxml')

contentVariable = soupVariable.select('head')

print(contentVariable)
# Assignment02 ---> Intermediate website

import requests
import bs4

requestVariable = requests.get('https://telanganaepass.cgg.gov.in/')

soupVar = bs4.BeautifulSoup(requestVariable.text,'lxml')

contentVar = soupVar.select('frameset')

print(contentVar)
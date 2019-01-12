# Assignment01 ---> Getting the information from webpage

import requests
import bs4

requestVariable = requests.get('https://en.wikipedia.org/wiki/Artificial_intelligence')

soupVariable = bs4.BeautifulSoup(requestVariable.text,'lxml')

for content in soupVariable.select('.mw-headline'):
    print(content.text)
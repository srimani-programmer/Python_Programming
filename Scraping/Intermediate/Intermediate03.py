# Assignment03 ---> Working with hackerrank

import requests
import bs4

requestVariable = requests.get('https://www.hackerrank.com/')

soupVariable = bs4.BeautifulSoup(requestVariable.text,'lxml')

for content in soupVariable.select('div'):
    print(content.text)
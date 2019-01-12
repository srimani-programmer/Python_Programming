# Getting Data from the website using web scraping

import requests
import bs4

requestVariable = requests.get('http://www.sriindugroup.org/')

#print(type(requestVariable))

#Getting the website data
#print(requestVariable.text)

beautyVariable = bs4.BeautifulSoup(requestVariable.text,'lxml')

soupContent = beautyVariable.select('div')

print(soupContent[0].getText())


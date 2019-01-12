# Assignment02 --> working with learn code online.in

import requests
import bs4

requestVariable = requests.get('https://www.learncodeonline.in/')

soupVariable = bs4.BeautifulSoup(requestVariable.text,'lxml')

for content in soupVariable.select('#navbar'):
    print(content.text)
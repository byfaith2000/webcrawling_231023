from bs4 import BeautifulSoup
from urllib.request import urlopen

import ssl
context = ssl._create_unverified_context()


html = urlopen('http://www.pythonscraping.com/pages/page1.html', context=context)
bsObj = BeautifulSoup(html, 'html.parser')
print(bsObj)
print()
print(bsObj.find('h1').text)
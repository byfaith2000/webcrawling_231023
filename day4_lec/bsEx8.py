from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen('http://en.wikipedia.org/wiki/Kevin_Bacon')
bsObj = BeautifulSoup(html, 'html.parser')
for link in bsObj.findAll('a', href=re.compile(r'^http://')):
    if 'href' in link.attrs:
        print(link['href'])
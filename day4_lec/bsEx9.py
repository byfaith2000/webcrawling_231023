from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

pages = set()

def getLinks(pageUrl):
    try:
        html = urlopen('https://en.wikipedia.org/'+pageUrl)
        bsObj = BeautifulSoup(html, 'html.parser')
        allInfo = bsObj.findAll('a', href=re.compile(r'^/wiki/'))
        print(bsObj.h1.get_text())
        print(bsObj.find(id='mw-content-text').findAll('p')[0])
        print(bsObj.find(id='ca-edit').find('span').find('a').attrs['href'])
    except Exception:
        pass

    for link in allInfo:
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                newPage = link.attrs['href']
                print(newPage)
                pages.add(newPage)
                getLinks(newPage)


getLinks('')
import re
from bs4 import BeautifulSoup

myencoding = 'utf-8'
myparser = 'html.parser'
filename = 'css01.html'

html = open(filename, encoding=myencoding)
bsObj = BeautifulSoup(html, myparser)
#print(bsObj)

h1 = bsObj.select_one('div#cartoon > h1').string
print('h1=', h1)
print()

li_list = bsObj.select('div#cartoon > ul > li')
for li in li_list:
    print('li = ',li.text)
print(end='\n\n')

choice = lambda x : print(bsObj.select_one(x).text)
choice('#item5')
choice('li#item4')
choice('ul > li#item3')
choice('#itemlist #item2')
choice('#itemlist > #item1')
choice('ul#itemlist > li#item1')
choice('li[id="item1"]')
print()
choice('li:nth-of-type(3)')
choice('li:nth-of-type(4)')
print()

mytag = bsObj.select_one('div#cartoon > ul.elements')
print(mytag)
print()

print(bsObj.select('#vegatables > li[class="us"]'))
print(bsObj.select('#vegatables > li.us'))
print()

result = bsObj.select('a[href$=".com"]')
#print(result)

for item in result:
    print(item['href'])
print()

result = bsObj.select('a[href*="daum"]')
print(result)
print()

cond = {'id':'ko', 'class':'cn'}
print(bsObj.find('li', cond))
print()

print(bsObj.find(id='vegatables').find('li', cond))

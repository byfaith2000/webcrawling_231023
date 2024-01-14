from bs4 import BeautifulSoup
from urllib.request import urlopen

def hollystore_info(result):
    for page in range(1, 11):
        holly_url = 'https://www.hollys.co.kr/store/korea/korStore2.do?pageNo={}&sido=&gugun=&store='.format(page)
        #print(holly_url)
        html = urlopen(holly_url)
        bsObj = BeautifulSoup(html, 'html.parser')
        #print(bsObj)
        tag_body = bsObj.find('tbody')
        #print(tag_body)
        for store in tag_body.findAll('tr'):
            #print(store)
            store_td = store.findAll('td')
            store_sido = store_td[0].text
            store_name = store_td[1].text
            store_address = store_td[3].text
            store_phone = store_td[5].text
            result.append([store_name, store_sido, store_address, store_phone])

result = []
hollystore_info(result)

for sdata in result:
    print(sdata)
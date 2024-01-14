import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from bs4 import BeautifulSoup
from urllib.parse import quote_plus

s = Service('chromedriver.exe')
driver = webdriver.Chrome(service=s)

keyword = quote_plus('무선청소기')
total_page = 10
prod_data_total = []

def get_serach_page_url(keyword, page):
    return 'https://search.danawa.com/dsearch.php?query={}&volumeType=allvs&page={}&limit=40&sort=saveDESC&list=list&boost=true&tab=goods'.format(keyword, page)

def get_prod_items(prod_items):
    prod_data = []
    for prod_item in prod_items:
        try:
            title = prod_item.select('p.prod_name > a')[0].text.strip()
        except:
            title = ''
        try:
            spec_list = prod_item.find('div', {'class': 'spec_list'}).text
        except:
            spec_list = ''
        try:
            price = prod_item.select('li.rank_one > p.price_sect > a > strong')[0].text.strip().replace(',','')
        except:
            price = ''
        prod_data.append([title, spec_list, price])
    return prod_data

for page in range(1, total_page+1):
    url = get_serach_page_url(keyword, page)
    driver.get(url)
    time.sleep(4)

    html = driver.page_source
    bsObj = BeautifulSoup(html, 'html.parser')

    prod_items = bsObj.select('div.main_prodlist > ul.product_list > li.prod_item')
    prod_item_list = get_prod_items(prod_items)
    prod_data_total = prod_data_total + prod_item_list

#print(prod_data_total)
data = pd.DataFrame(prod_data_total,
                    columns=['상품명', '스펙목록', '가격'])
data.to_csv('./files/danawa_crawling_result.csv', index=False, encoding='ms949')
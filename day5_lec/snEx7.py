from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

s = Service('chromedriver.exe')

def search_coffeeBeanStrore_info(result):
    cb_url = 'https://www.coffeebeankorea.com/store/store.asp'
    driver = webdriver.Chrome(service=s)

    for i in range(30):
        driver.get(cb_url)
        time.sleep(2)

        try:
            driver.execute_script('storePop2(%d)'%i)
            time.sleep(2)
            html = driver.page_source
            bsObj = BeautifulSoup(html, 'html.parser')
            store_name_h2 = bsObj.select('div.store_txt > h2')
            store_name = store_name_h2[0].text
            #print(store_name)
            store_info = bsObj.select('div.store_txt > table.store_table > tbody > tr > td')
            store_address = store_info[2].text
            store_phone = store_info[3].text
            result.append([store_name, store_address, store_phone])
        except:
            continue


result = []
search_coffeeBeanStrore_info(result)
#print(result)

import pandas as pd

frame = pd.DataFrame(result, columns=['매장 이름', '매장 주소', '매장 전화번호'])
print(frame)
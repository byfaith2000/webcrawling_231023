from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from bs4 import BeautifulSoup

s = Service('chromedriver.exe')
driver = webdriver.Chrome(service=s)
url = 'https://search.danawa.com/dsearch.php?query=%EB%AC%B4%EC%84%A0%EC%B2%AD%EC%86%8C%EA%B8%B0&originalQuery=%EB%AC%B4%EC%84%A0%EC%B2%AD%EC%86%8C%EA%B8%B0&checkedInfo=N&volumeType=allvs&page=1&limit=40&sort=saveDESC&list=list&boost=true&tab=goods&addDelivery=N&mode=simple&isInitTireSmartFinder=N&recommendedSort=Y&defaultUICategoryCode=10325109&defaultPhysicsCategoryCode=72%7C80%7C81%7C0&defaultVmTab=3162&defaultVaTab=951386&isZeroPrice=Y&quickProductYN=N'
driver.get(url)
time.sleep(2)
html = driver.page_source
bsObj = BeautifulSoup(html, 'html.parser')
#print(bsObj)

prod_items = bsObj.select('div.main_prodlist > ul.product_list > li.prod_item')
#print(prod_items)

title = prod_items[0].select('p.prod_name > a')[0].text.strip()
print(title)

spec_list = prod_items[0].find('div', {'class':'spec_list'}).text
print(spec_list)

price = prod_items[0].select('li.rank_one > p.price_sect > a > strong')[0].text.strip().replace(',','')
print(price)
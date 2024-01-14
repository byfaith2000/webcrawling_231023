from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

chrome_options = Options()
chrome_options.add_experimental_option('detach', True)

s = Service('chromedriver.exe')
driver = webdriver.Chrome(service=s, options=chrome_options)
driver.get('https://www.naver.com')

input_element = driver.find_element(By.NAME, 'query')
input_element.send_keys('python')
input_element.send_keys(Keys.RETURN)


from bs4 import BeautifulSoup

html = driver.page_source

bsObj = BeautifulSoup(html, 'html.parser')

tags = bsObj.select('ul.lst_type > li > a')

for i in tags:
    print(i)

driver.quit()

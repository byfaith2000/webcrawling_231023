from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

s = Service('chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get('https://www.naver.com')
time.sleep(1)

login_btn = driver.find_element(By.CLASS_NAME, 'MyView-module__naver_logo____Y442')
login_btn.click()
time.sleep(1)

tag_id = driver.find_element(By.NAME, 'id')
tag_pw = driver.find_element(By.NAME, 'pw')

tag_id.clear()
time.sleep(1)

tag_id.click()

import pyperclip

pyperclip.copy('id')

from selenium.webdriver.common.keys import Keys
tag_id.send_keys(Keys.CONTROL, 'v')
time.sleep(1)

tag_pw.click()
pyperclip.copy('pw')
tag_pw.send_keys(Keys.CONTROL, 'v')
time.sleep(1)

login_btn = driver.find_element(By.ID, 'log.login')
login_btn.click()

driver.get('https://order.pay.naver.com/home')
html = driver.page_source

from bs4 import BeautifulSoup

bsObj = BeautifulSoup(html, 'html.parser')

while True:
    pass
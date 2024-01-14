from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

s = Service('chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get('https://nid.naver.com/nidlogin.login')

time.sleep(2)

from selenium.webdriver.common.by import By

id_input = driver.find_element(By.ID, 'id')
id_input.send_keys('lims')

pw_input = driver.find_element(By.ID, 'pw')
pw_input.send_keys('adfdfdfd')

lg_btn = driver.find_element(By.XPATH, '//*[@id="log.login"]')
lg_btn.click()
while True:
    pass
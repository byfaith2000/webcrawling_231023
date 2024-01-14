from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

s = Service('chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get('http://www.danawa.com')
time.sleep(3)

from selenium.webdriver.common.action_chains import ActionChains

def mouseOverElement(title):
    element = driver.find_element(By.LINK_TEXT, title)
    ActionChains(driver).move_to_element(element).perform()
    return element

mouseOverElement('가전·TV')
mouseOverElement('냉장고')
mouseOverElement('냉동고')
mouseOverElement('뚜껑형').click()

time.sleep(4)





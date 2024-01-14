from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

s = Service('chromedriver.exe')

url = 'https://www.jolse.com/'
driver = webdriver.Chrome(service=s)
driver.get(url)

def mouseOverElement(title):
    element = driver.find_element(By.LINK_TEXT, title)
    ActionChains(driver).move_to_element(element).perform()
    return element

mouseOverElement('SKINCARE').click()
time.sleep(4)
mouseOverElement('Toners & Mists').click()

def get_item_name_price_in_page():
    item_list = []

    html = driver.page_source
    bsObj = BeautifulSoup(html, 'html.parser')
    items = bsObj.findAll('ul', {'class':'prdList grid5'})[1].findAll('li')
    for item in items:
        try:
            div_tag = item.find('div', {'class':'description'})
            strong_tag = div_tag.find('strong', {'class':'name'})
            name = strong_tag.findAll('span')[2].text
            price = div_tag.find('li').findAll('span')[1].text
            item_list.append([name, price])
        except:
            continue
    return item_list


def page_search(start, end):
    all_item_list = []
    page_url = driver.current_url + '?page='
    for page in range(start, end+1):
        cur_url = page_url + str(page)
        driver.get(cur_url)

        time.sleep(3)

        page_item_list = get_item_name_price_in_page()
        for item in page_item_list:
            all_item_list.append([item[0], item[1]])
    return all_item_list

total_item_list = []
total_item_list = page_search(1, 5)

for item in total_item_list:
    print(item[0], item[1], sep=',')

driver.quit()
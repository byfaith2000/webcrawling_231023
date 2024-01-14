from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

chrom_options = Options()
chrom_options.add_experimental_option('detach', True)

s = Service('chromedriver.exe')
driver = webdriver.Chrome(service=s, options=chrom_options)
driver.get('https://ww.google.com')

driver.quit()


# while(True):
#     pass
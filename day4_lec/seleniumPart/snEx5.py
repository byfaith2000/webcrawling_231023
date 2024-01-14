from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import os

import urllib.request
import urllib
from bs4 import BeautifulSoup

chrome_options = Options()
chrome_options.add_experimental_option('detach', True)

s = Service('chromedriver.exe')
driver = webdriver.Chrome(service=s, options=chrome_options)
driver.get('https://korean.visitkorea.or.kr/detail/rem_detail.do?cotid=be3db10c-b642-409c-81cc-c4cdecb5bd8b&temp=')
time.sleep(3)

file_dir = 'imgs'
dir_name = 'photoFolder'

now = time.localtime()
f_name = '%04d-%02d-%02d-%02d-%02d-%02d' % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
os.makedirs(file_dir + f_name+'-'+dir_name)
os.chdir(file_dir + f_name+'-'+dir_name)
f_result_dir = file_dir + f_name +'-'+dir_name

#print(f_result_dir)

def scroll_down(driver):
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    time.sleep(2)

scroll_down(driver)

file_no = 0
count = 1
img_src2 = []

html = driver.page_source
bsObj = BeautifulSoup(html, 'html.parser')
img_srcs = bsObj.find('div', {'class':'box_txtPhoto'}).findAll('img')
#print(img_srcs)

for isrc in img_srcs:
    temp = isrc['src']
    img_src2.append(temp)
    count += 1

#print(img_src2)

for i in range(0, len(img_src2)):
    try:
        urllib.request.urlretrieve(img_src2[i], str(file_no) + '.jpg')
    except:
        continue

    file_no += 1
    time.sleep(0.5)
    print(f'{file_no}번째 이미지 저장')

print(f'총 저장 건수는 {file_no}건 입니다.')
print(f'파일 저장 경로: {f_result_dir} 입니다.')
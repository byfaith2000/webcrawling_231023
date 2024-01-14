from urllib.request import urlopen
import re


url = 'https://finance.naver.com/item/main.nhn?code=066570'
html = urlopen(url)
html_content = str(html.read().decode('ms949'))
#print(html_content)

stock_result = re.findall(r'(\<dl class=\"blind\"\>)([\s\S]+?)\</dl\>', html_content)
#print(stock_result)
#print(len(stock_result))

info_stock = stock_result[0]
#print(info_stock)

stock_index = info_stock[1]
#print(stock_index)

index_list = re.findall(r'(\<dd\>)([\s\S]+?)\</dd\>', stock_index)
#print(index_list)

for index in index_list:
    print(index[1])
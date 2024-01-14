import requests
from bs4 import BeautifulSoup
from urllib.parse import quote_plus


endPoint = 'http://apis.data.go.kr/B552657/ErmctInsttInfoInqireService/getParmacyListInfoInqire?'
serviceKey = 'h7PvuK310drat11a7ERQSJonH49PTTDAddUaRqw5LLxGFDpyWk1NEgT5HPt6CKC4FzYL2BuTbSsUmvuEaqmoUw%3D%3D'

Q0 = quote_plus('서울특별시')
ORD = 'NAME'
pageNo = '1'
numOfRows = '5000'
pageSize = '10'
parameter = 'serviceKey='+serviceKey+'&Q0='+Q0+'&ORD='+ORD+'&pageNo='+pageNo+'&numOfRows='+numOfRows+'&pageSize='+pageSize

url = endPoint + parameter
#print(url)

result = requests.get(url)
bsObj = BeautifulSoup(result.content, 'lxml')
items = bsObj.findAll('item')

count = 0
for item in items:
    tag_item = item.find('dutytime1c')
    if(tag_item != None):
        close_time = int(tag_item.text)
        if(close_time > 2100):
            count += 1
print('월요일 9시 이후까지 운영하는 약국의 수:', count)
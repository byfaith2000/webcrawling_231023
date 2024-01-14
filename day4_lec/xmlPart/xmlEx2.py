import requests
from bs4 import BeautifulSoup
from urllib.parse import quote_plus


endPoint = 'http://apis.data.go.kr/B552657/ErmctInsttInfoInqireService/getParmacyListInfoInqire?'
serviceKey = 'h7PvuK310drat11a7ERQSJonH49PTTDAddUaRqw5LLxGFDpyWk1NEgT5HPt6CKC4FzYL2BuTbSsUmvuEaqmoUw%3D%3D'

Q0 = quote_plus('서울특별시')
#print(Q0)
Q1 = quote_plus('강남')
QN = quote_plus('삼성약국')
QT = 4
ORD = 'NAME'
pageNo = '1'
numOfRows = '10'
parameter = 'serviceKey='+serviceKey+'&Q0='+Q0+'&Q1='+Q1+'&QN='+QN+'&ORD='+ORD+'&pageNo='+pageNo+'&numOfRows='+numOfRows
url = endPoint + parameter
#print(url)

result = requests.get(url)
#print(result)
bsObj = BeautifulSoup(result.content, 'lxml')
#print(bsObj)

for item in bsObj.findAll('dutyname'):
    print(item.text)
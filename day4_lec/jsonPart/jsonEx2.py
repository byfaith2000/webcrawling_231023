from urllib.request import urlopen
import json

from_date = '2010-01-01'
to_date = '2023-07-30'
url = 'http://www.krei.re.kr:18181/chart/main_chart/index/kind/W/sdate/'+from_date+'/edate/'+to_date
#print(url)

text = urlopen(url)
json_obj = json.load(text)
#print(json_obj)

pieces = []
for item in json_obj:
    print(f'date:{item["date"]},  price:{item["settlement"]}')
    pieces.append(float(item['settlement']))

import matplotlib.pyplot as plt

plt.plot(pieces)
plt.ylabel('price')
plt.show()

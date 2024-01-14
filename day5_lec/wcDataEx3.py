import pandas as pd

data = pd.read_csv('./files/danawa_crawling_result.csv', encoding='ms949')
#data.info()
print()

#print(data.head(10))
print()

#print(data['스펙목록'][0])
spec_list = data['스펙목록'][0].split(' / ')
#print(spec_list)

category = spec_list[0]
#print(category)

use_time_spec = None
suction_spec = None
for i, spec in enumerate(spec_list):
    if '사용시간' in spec:
        use_time_spec = spec.strip()
    elif '흡입력' in spec:
        suction_spec = spec.strip()
#print(use_time_spec)
#print(suction_spec)

category_list = []
use_time_list = []
suction_list = []

for spec_data in data['스펙목록']:
    if not isinstance(spec_data, str):
        continue
    spec_list = spec_data.split(' / ')
    category = spec_list[0].strip()
    category_list.append(category)

    use_time_value = None
    suction_value = None

    for i, spec in enumerate(spec_list):
        if '사용시간' in spec:
            use_time_value = spec.split('사용시간:')[1].strip()
        elif '흡입력' in spec:
            suction_value = spec.split('흡입력:')[1].strip()

    use_time_list.append(use_time_value)
    suction_list.append(suction_value)

print(category_list)
print(use_time_list)
print(suction_list)

def convert_time_minute(time):
    try:
        if '시간' in time:
            hour = time.split('시간')[0]
            if '분' in time:
                minute = time.split('시간')[-1].split('분')[0]
            else:
                minute = 0
        else:
            hour = 0
            minute = time.split('분')[0]
        return int(hour) * 60 + int(minute)
    except:
        return None

new_use_time_list = []

for time in use_time_list:
    value = convert_time_minute(time)
    new_use_time_list.append(value)
print(new_use_time_list)

def get_suction(value):
    try:
        value = value.upper()
        if 'AW' in value or 'W' in value:
            result = int(value.replace('A','').replace('W',''))
        elif 'PA' in value:
            result = int(value.replace('PA','')) / 100
        else:
            result = None
        return result
    except:
        return None

new_suction_list = []
for power in suction_list:
    value = get_suction(power)
    new_suction_list.append(value)
print(new_suction_list)
print()

print(data['상품명'][0])

company_list = []
product_list = []

for title in data['상품명']:
    if not isinstance(title, str):
        continue
    title_info = title.split(' ', 1)
    if len(title_info) == 1:
        company_name = None
        product_name = None
    else:
        company_name = title_info[0]
        product_name = title_info[1]

    company_list.append(company_name)
    product_list.append(product_name)

print(company_list)
print(product_list)

pd_data = pd.DataFrame()
pd_data['카테고리'] = category_list
pd_data['회사명'] = company_list
pd_data['제품'] = product_list
pd_data['가격'] = pd.Series(data['가격'].dropna().values)
pd_data['사용시간'] = new_use_time_list
pd_data['흡입력'] = new_suction_list

pd_data_final = pd_data[pd_data['카테고리'].isin(['핸디스틱청소기'])]
print(pd_data_final.head(10))
pd_data_final.to_csv('./files/danawa_final.csv', index=False)
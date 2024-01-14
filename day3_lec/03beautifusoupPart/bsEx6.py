from bs4 import BeautifulSoup

html = open('fruits.html', 'r', encoding='utf-8')
bsObj = BeautifulSoup(html, 'html.parser')
#print(bsObj)

body = bsObj.find('body')
print(body)
print()

body2 = bsObj.select_one('body')
#print(body2)


ptag = body.find('p')
print('1번째 ptag : ', ptag['class'])
ptag['class'][1] = 'white'
print('1번째 ptag : ', ptag['class'])
ptag['id'] = 'apple'
print()
print(body)
print()

idx = 0
print('children attr 항목')
for child in body.children:
    idx += 1
    print(str(idx) + '번째 요소 : ', child)
print()

mydiv = bsObj.find('div')
print(mydiv)
print()
print(mydiv.parent)
print()

mytag = bsObj.find('p', attrs={'class':'hard'})
print(mytag)
print()

print(mytag.parent)
print(mytag.find_parents())
print()

for p in mytag.find_parents():
    print(p.name)
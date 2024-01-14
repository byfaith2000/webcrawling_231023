import re

r1 = re.compile('Hello')
fobj1 = re.search(r1, 'good Hello World')
print(fobj1)
print(fobj1.span())
print(fobj1.group())
print(fobj1.group(0))
print()

fobj2 = re.search(r'Hello', 'good Hello World')
print(fobj2)
print()


fobj3 = re.search('Hello', 'good Hello World')
print(fobj3)
print()

fobj4 = re.match('good', 'good Helllo World')
print(fobj4)
print()

fobj4 = re.match('Hello', 'good Helllo World')
print(fobj4)
print()

fobj2 = re.search(r'Hello', 'good Hello World Hello')
print(fobj2)
print()

fobj5 = re.findall(r'Hello', 'good Hello World Hello')
print(fobj5)
print()

fobj6 = re.findall(r'a+b*', 'aaa cc bbb aabb')
print(fobj6)
print()

fobj7 = re.findall(r'^good', 'good Hello World good')
print(fobj7)
print()

fobj8 = re.findall(r'[0-9]+', 'Hello 3234good Hello 422 5 world')
print(fobj8)
print()

fobj9 = re.findall(r'h{2}', 'Hello 2332hhgood Hello 32 ddhhh2')
print(fobj9)
print()

fobj9 = re.findall(r'h{2,3}', 'Hello 2332hhgood Hello 32 ddhhh2')
print(fobj9)
print()

fobj10 = re.findall(r'[0-9]{2,3}-[0-9]{3,4}-[0-9]{4}', 'hello tel:010-7878-8989 good day phone:017-789-8989, local:02-787-8989')
print(fobj10)

fobj10 = re.findall(r'\d{2,3}-\d{3,4}-\d{4}', 'hello tel:010-7878-8989 good day phone:017-789-8989, local:02-787-8989')
print(fobj10)
print()

fobj11 = re.findall(r'[a-zA-Z]+', 'hello tel:010-7878-8989 good day Phone:017-789-8989, local:02-787-8989')
print(fobj11)

fobj11 = re.findall(r'[a-zA-Z0-9_]+', 'hello tel:010-7878-8989 good day Phone:017-789-8989, local:02-787-8989')
print(fobj11)

fobj11 = re.findall(r'\w+', 'hello tel:010-7878-8989 good day Phone:017-789-8989, local:02-787-8989')
print(fobj11)

fobj11 = re.findall(r'\W+', 'hello tel:010-7878-8989 good day Phone:017-789-8989, local:02-787-8989')
print(fobj11)










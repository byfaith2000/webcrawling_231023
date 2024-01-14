import re

rstr1 = re.sub(r'apple|orange', 'fruit', 'apple box orange box')
print(rstr1)
print()

rstr2 = re.sub(r'나의|내', '그의' ,'나의 물건에 손대지 마시오')
print(rstr2)
print()

def mutiTen(m):
    n = int(m.group())
    return str(n*10)

rstr3 = re.sub(r'[0-9]+', mutiTen, '32, function533 9082 fruit 7')
print(rstr3)
print()

rstr4 = re.sub(r'([a-z]+) ([0-9]+)', '\\2 \\1 \\1', 'hello 3232')
print(rstr4)
print()

rstr5 = re.sub(r'(\{\s*)\"(\w+)\"\:\s*\"(\w+)\"(\s*\})', '<\\2>\\3</\\2>', '{ "name": "kim"}')
print(rstr5)
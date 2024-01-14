import re

robj1 = re.match(r'([0-9]+) ([0-9]+)', '3232 4343 good')
print(robj1)
print(robj1.group(0))
print(robj1.group(1))
print(robj1.group(2))
print(robj1.groups())
print()

robj2 = re.match(r'(?P<func>[a-zA-Z_][a-zA-Z0-9_]+)\((?P<arg>\w+)\)', 'print(value2)')
print(robj2)
print(robj2.group(0))
print(robj2.group(1))
print(robj2.group(2))
print(robj2.group('func'))
print(robj2.group('arg'))
print()


fobj = re.findall(r'b.d', 'bad bed b@d beed')
print(fobj)
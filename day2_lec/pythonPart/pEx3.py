str1 = '    python    '
print('*', str1, '*')
print('*', str1.strip(), '*')
print('*', str1.lstrip(), '*')
print('*', str1.rstrip(), '*')
print()

str2 = ',.python.'
print(str2.strip(',.'))
print(str2.lstrip(',.'))
print()

str3 = 'it is a good day'
print(str3.split())
str4 = '2023/10/24'
print(str4.split('/'))
print()

print(str3.split(' ', 1))
print(str3.split(' ', 2))


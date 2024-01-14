#
# value = 100
# print(value)
# print(type(value))
# print()
#
# value2 = 3232.324
# value3 = int(value2)
# print(value3)
# value4 = float(value3)
# print(value4)

# value = int(input('정수를 입력하세요:'))
# print(value)
# print(value + 200)

# value1, value2 = 232, 532
# print(value1, value2, sep='/', end=' ')
# print('안녕하세요')

data = [221, 'abc', True, 634.34]
print(data)
data1 = [[1,2,3], [4,5,6]]
print(data1)
data2 = [[1,2,3], [4,5], [6,7,8,9]]
print(data2)
print(data2[0])
print(data2[2])
print(data2[-1])

data3 = [10,80,60,90,40,30,20]
print(data3[2:5])
print(data3[4:])
print(data3[-3:])
print()

sdata1 = 'abcdefg'
print(sdata1[3])
print(sdata1[1:5])
print()

ldata1 = [10, 40, 60]
ldata2 = [40, 90, 100]
print(ldata1 + ldata2)

tdata1 = 10, 20
tdata2 = 50, 90
print(tdata1 + tdata2)

str1 = 'hello '
str2 = 'world'
print(str1 + str2)
print()

ldata3 = [10, 20]
print(ldata3 * 3)

a = [0,0]
b = [1,1]
c = a * 2 + b * 3
print(c)

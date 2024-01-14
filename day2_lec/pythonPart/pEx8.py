ldata1 = ['red', 'green', 'blue']
result = ''
for l in ldata1:
    result += l
print(result)
print()
print(''.join(ldata1))
print('-'.join(ldata1))
print(','.join(ldata1))
print()

data1 = []
for i in range(10):
    data1.append(i)
print(data1)

data2 = [i for i in range(10)]
print(data2)
print()

data1 = []
for i in range(10):
    if i % 2 == 0:
        data1.append(i)
print(data1)

data2 = [i for i in range(10) if i % 2 == 0]
print(data2)
print()


data1 = []
for i in range(10):
    if i % 2 == 0:
        data1.append(i)
    else:
        data1.append(10)
print(data1)

data2 = [i if i % 2 == 0 else 10 for i in range(10)]
print(data2)
print()

str1 = 'have a good day'
data4 = [[w.upper(), w.lower(), len(w)] for w in str1.split()]
print(data4)
print()

for i, d in enumerate(['kim', 'lee', 'choi'], start=3):
    print(i, d)
print()

data5 = {i:j for i, j in enumerate(str1.split())}
print(data5)
print()

ldata1 = ['kim', 'lee', 'choi']
ldata2 = [20,10,50]
ldata3 = ['seoul', 'busan', 'incheon']

for n, a, ad in zip(ldata1, ldata2, ldata3):
    print(n, a, ad)
def add(x, y):
    return x + y

print(add(10,20))

add2 = lambda x, y : x + y
print(add2(10,20))

def calc(cf, a, b):
    result = cf(a, b)
    print('result:',result)

calc(add, 10, 70)

calc(lambda x, y : x + y, 10,70)

ldata2 = [('kim', 40), ('lee', 10), ('choi', 30)]
ldata2.sort(key=lambda x : x[-1])
print(ldata2)































def f2(a, b):
    return a + 10 * 2 + b
def add(a, b):
    return a + b

print(add(10,20))
print(add(3232.323,20))
print(add(3232.323,875.656546))
print()


def print_info(name, age):
    print('name:{} age:{}'.format(name, age))


print_info('김가', 30)
print_info(name='lee', age=50)
print_info(age=50, name='lee')
print()

def print_info2(name, age=0):
    print('name:{} age:{}'.format(name, age))

print_info2('choi', 10)
print_info2('choi')
print()

data = 20, 50
print(data)
print(data[0], data[1])
print(*data)
print()

def add2(*arg):
    result = 0
    for i in arg:
        result += i
    return result

print(add2(10,20,30))
print(add2(10,20,30,40))
print(add2(10,20,30,40,50))
print()

def insa():
    print('안녕하세요')
insa()
print(insa)
fvalue = insa
fvalue()

def multiply(a, b):
    return a * b

flist = [add, multiply]
print(flist[1](10,20))

def calc(cf, a, b):
    rvalue = cf(a, b)
    print('result:', rvalue)

calc(add, 50, 90)
calc(multiply, 50, 90)

ldata = [5,2,3,9]
ldata.sort()
print(ldata)
print()

ldata2 = [('kim', 40), ('lee', 10), ('choi', 30)]

def f1(x):
    return x[1]
ldata2.sort(key=f1)
print(ldata2)



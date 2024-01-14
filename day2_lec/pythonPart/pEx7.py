ddata1 = {'name':'kim', 'age':30, 'address':'seoul'}
print(ddata1)

print(dict([('name','kim'), ('age',30), ('address','seoul')]))
print(dict(name='kim', age=30, address='seoul'))
print(ddata1['age'])

print(ddata1.keys())
print()
for k in ddata1.keys():
    print(k)
print()

print(ddata1.values())
print()

print(ddata1.items())

for k, v in ddata1.items():
    print(k, v, sep=':')
print()

def print_info(name, age, address):
    print(f'name={name}, age={age}, address={address}')

print_info(name='lee', age=40, address='incheon')
print_info(name=ddata1['name'], age=ddata1['age'], address=ddata1['address'])
print_info(**ddata1)
print()

def print_info2(**data):
    for k, v in data.items():
        print(k, v, sep='=', end=' ')
print_info2(name='lee', address='busan')
print()
print_info2(name='lee', address='busan', age=30)
print()
print_info2(name='lee', address='busan', age=30, height=180)




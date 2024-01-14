a = (5, 33, 77)
b = (44,823,11)
c = (10,50,90)

result1 = [sum(data) for data in zip(a, b, c)]
print(result1)

result2 = [x + y + z for x, y, z in zip(a, b, c)]
print(result2)
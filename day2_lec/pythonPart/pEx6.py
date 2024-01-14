sdata1 = {3,1,6,8,3,6,4,2,7,1}
print(sdata1)
print()

ldata = ['lee', 'choi', 'kim', 'hyo', 'oh', 'kim']
sdata2 = set(ldata)
print(sdata2)
print()

sdata3 = {1,2,3,4}
sdata4 = {3,4,5,6}

print(set.union(sdata3, sdata4))
print(sdata3.union(sdata4))
print(sdata3 | sdata4)
print()

print(set.intersection(sdata3, sdata4))
print(sdata3 & sdata4)
print()

print(sdata3.difference(sdata4))
print(sdata3 - sdata4)
print()

print(sdata3.symmetric_difference(sdata4))
print(sdata3 ^ sdata4)
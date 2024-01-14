import pandas as pd
import numpy as np

s1 = pd.Series([3,4,5,6])
print(s1)
print()

s1 = pd.Series([3,4,5,6], index=['a','b','c','d'])
print(s1)
print()

print(s1.index)
print()
print(type(s1.values))
print()

print(s1['c'])
s1['d'] = 100
print()
print(s1)
print()

print(s1 * 3)
print()
print(s1 > 5)
print()

print(np.sqrt(s1))
print()

ddata = {'one':100, 'two':500, 'three':900}
print(ddata)
print()
print(pd.Series(ddata))
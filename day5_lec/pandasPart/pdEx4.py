import numpy as np
import pandas as pd

frame1 = pd.DataFrame(np.arange(8).reshape(2,4),
                      columns=['d','a','b','c'],
                      index=['three','one'])
print(frame1)
print()

print(frame1.sort_index())
print()

print(frame1.sort_index(axis=1))
print()

print(frame1.sort_index(axis=1, ascending=False))
print()

frame2 = pd.DataFrame({'first':[4,7,-3,1],
                       'second':[0,1,0,1]})
print(frame2)
print()

print(frame2.sort_values(by='first'))
print()
print(frame2.sort_values(by='second'))
print()
print(frame2.sort_values(by=['second', 'first']))
print()


frame4 = pd.DataFrame(np.random.randn(1000, 3),
                      columns=['first','second','third'])
print(frame4)
print()
print(frame4.mean())
print()
print(frame4.std())
print()
print(frame4.describe())
print()

frame4.info()
print()

print(frame4.head(15))
print()
print(frame4.tail(10))








import pandas as pd

frame1 = pd.read_csv('ex1.csv')
print(frame1)
print()

frame2 = pd.read_csv('ex2.csv', header=None)
print(frame2)
print()

frame3 = pd.read_csv('ex2.csv', names=['one','two','three','four','insa'])
print(frame3)
print()

frame3 = pd.read_csv('ex2.csv', names=['one','two','three','four','insa'], index_col='insa')
print(frame3)
print()

frame3 = pd.read_csv('ex2.csv', names=['one','two','three','four','insa'], index_col=4)
print(frame3)
print()

frame4 = pd.read_csv('ex4.csv', skiprows=[0,2,3])
print(frame4)
print()

frame4.to_csv('savefile1.csv')
frame4.to_csv('savefile2.csv', index=False)
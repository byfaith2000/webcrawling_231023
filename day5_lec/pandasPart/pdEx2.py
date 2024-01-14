import pandas as pd

frame1 = pd.DataFrame([[3,2,1], [5,6,7]])
print(frame1)
print()

frame2 = pd.DataFrame([[3,2,1], [5,6,7]],
                      index=['one', 'two'],
                      columns=['first','second','third'])
print(frame2)
print()
print(frame2.index)
print(frame2.columns)
print()

ldata = [('kim',180,80), ('lee',160,45), ('choi',170,70), ('hyo',150,40)]
frame2 = pd.DataFrame(ldata, columns=['name','height','weight'])
print(frame2)
print()

ddata = {'city': ['seoul','busan','incheon'],
         'pop':[1000,500,300],
         'area':[200,300,400]}
print(ddata)
print()

frame3 = pd.DataFrame(ddata, index=['one','two','three'])
print(frame3)
print()
print(frame3['city'])
print()
print(frame3.city)
print()
print(frame3.loc['two'])
print()
print(frame3.loc['two','pop'])
print()
print(frame3.iloc[1:2,:])
print()







import numpy as np

data1 = [3, 1, 5, 8, 4.2, 9]
print(data1)

arr1 = np.array(data1)
print(arr1)
arr2 = np.array(data1, dtype=np.int32)
print(arr2)
print(type(arr2))

data2 = [[1,2,3], [4,5,6]]
print(data2)
print()

arr3 = np.array(data2)
print(arr3)
print(arr3.shape)
print()

arr3 = np.arange(1, 10, 2)
print(arr3)
print(type(arr3))
print()

arr4 = np.linspace(-3, 3, 5)
print(arr4)
print()

arr5 = np.zeros([3,4])
print(arr5)
print()

arr6 = np.ones([3,4])
print(arr6)
print()

arr7 = np.empty([3,4])
print(arr7)
print()

arr8 = np.full([3,4], 100)
print(arr8)
print()














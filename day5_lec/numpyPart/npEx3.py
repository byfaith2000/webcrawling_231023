import numpy as np

arr1 = np.arange(10)
print(arr1)
print()
print(np.sqrt(arr1))
print()
print(np.exp(arr1))
print()
print(np.cos(arr1))
print()

arr2 = np.array([[2,7,5,9],
                 [7,4,9,1],
                 [8,7,6,5]])
print(arr2)
print()

print(arr2.mean())
print(arr2.sum())
print(arr2.std())
print()

print(arr2.mean(axis=0))
print(arr2.mean(axis=1))
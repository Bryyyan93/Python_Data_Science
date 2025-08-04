import numpy as np
a = [1,2,3,4,5]

x = np.array(a)
print(type(x))
print(x.shape)
print(x.dtype)
print(x.mean())

print(np.dot(np.array([1,-1]),np.array([1,1])))


arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([2, 1, 2, 3, 4, 5])

print(np.multiply(arr1, arr2))

u = np.array([1, 0])
v = np.array([0, 1])

print(np.subtract(u,v))

arr1 = np.array([1, 2, 3])
arr2 = np.array([8, 9, 10])

print(np.add(arr1, arr2))
print(np.subtract(arr1, arr2))
print(np.multiply(arr1, arr2))
print(np.divide(arr1, arr2))
print(np.dot(arr1, arr2))


arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([6, 7, 8, 9, 10])

even = []
odd = []

even = np.array(even)

for i in arr1:
    if i % 2 == 0:
        print(i, "even")
        even = [i]
    else:
        print(i, "odd")
        odd = [i]
print(even)
print(odd)
for i in arr2:
    if i % 2 == 0:
        print(i, "even")
    else:
        print(i, "odd")     


a=np.array([1,1])

b=np.array([1,0])



print("aqui: ", np.dot(a,b))
print(int(3.2))

A=((11,12),[21,22])
print(A[0][1])

print('1,2,3,4'.split(','))
import numpy as np
# arr= np.array([
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ])
# print(arr)
# print(arr.shape)
# print(arr.ndim)
# print(arr.dtype)
# print(arr[:,1])
# print(arr[-1][-1])


# print(arr.sum())
# print(arr.mean())
# print(arr.max())
# print(arr.min())


# arr_copy=arr.copy()
# arr_copy[arr_copy>5]=0
# print(arr_copy)


# print(arr.sum(axis=0))
# print(arr.sum(axis=1))

# # broad casting in numpy

# arr1=np.array([
#  [1,2,3],
#  [4,5,6],
#  [7,8,9]
# ])
# print(arr1 * 18)
# print(arr1 + 5)

# print( arr1>5)
# print ( arr1[arr1 >5])
# print ( arr1[arr1 % 2 ==0])


# # fancy indexing 

# print(arr1[0:2])
# print(arr1[:,0:2])
# print(arr1[1:,1:])
# print(arr1[:2,1:])

# print(arr1[[0,2],[1,2]])


# arr = np.array([1,2,3,4,5,6])

# print(arr.reshape(-1,1))


# -1 means choose urself automatically see how many columns needed like here 1 so it rearranges itself

arr = np.arange(1,13)

print(arr)

print(arr.reshape(3,4))
print(arr.reshape(4,3))

print(np.zeros((2,2)))
print(np.ones((2,5)))
print(np.arange(1,5))
print(np.linspace(0,10,5))


a=np.zeros((2,2))
b=np.ones((2,2))
print(a+b)
print(np.arange(1,11).reshape(2,5))
print(np.linspace(0,100,5))



A = np.array([
    [1,2],
    [3,4]
])

B = np.array([
    [5,6],
    [7,8]
])

print(A.T)

print(np.dot(
    np.array([1,2,3]),
    np.array([4,5,6])
))

print(A @ B)


print(np.random.rand(3,3))
np.random.seed(42) # for fixing random ness
print(np.random.randint(
    1,100,size=(3,3)
))


print(arr.mean())

print(arr.std())

print(arr.var())

print(arr.max())

print(arr.min())

print(np.concatenate((A,B),axis=0))

print(np.vstack((A,B)))

print(np.hstack((A,B)))

print(A.flatten())



flatt=A.ravel() #this does not create a copy


print(flatt)
flatt[0]=99
print(flatt)
print(flatt.shape)
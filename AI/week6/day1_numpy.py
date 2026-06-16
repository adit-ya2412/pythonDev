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
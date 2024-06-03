import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])
arr_reshaped = arr.reshape((2, 3))  # 将一维数组重塑为 2x3 的二维数组
print(arr_reshaped)
# 输出:
# [[1 2 3]
#  [4 5 6]]

arr.resize((2, 3))
print(arr)
# 输出:
# [[1 2 3]
#  [4 5 6]]

arr = np.array([[1, 2, 3], [4, 5, 6]])
arr_raveled = arr.ravel()
print(arr_raveled)  # [1 2 3 4 5 6]

arr_flattened = arr.flatten()
print(arr_flattened)  # [1 2 3 4 5 6]

arr = np.array([[1, 2, 3], [4, 5, 6]])
arr_transposed = arr.transpose()
print(arr_transposed)
# 输出:
# [[1 4]
#  [2 5]
#  [3 6]]


arr = np.array([[6, 4, 5], [3, 1, 2]])
arr_sorted = np.sort(arr, axis=0)
print(arr_sorted)  # 输出: [[3 1 2]
                   #       [6 4 5]]
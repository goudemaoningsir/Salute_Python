import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

print("############################# 加 #############################")
result = arr1 + arr2  # [5, 7, 9]
print(result)
print("############################# 减 #############################")
result = arr1 - arr2  # [-3 -3 -3]
print(result)
print("############################# 乘 #############################")
result = arr1 * arr2  # [ 4 10 18]
print(result)
print("############################# 除 #############################")
result = arr1 / arr2  # [0.25 0.4  0.5 ]
print(result)
print("############################# 平方根 #############################")
result = np.sqrt(arr1)  # [1.0, 1.41421356, 1.73205081]
print(result)
print("############################# 指数运算 #############################")
result = np.exp(arr1)  # [2.71828183, 7.3890561, 20.08553692]
print(result)
print("############################# 对数运算 #############################")
result = np.log(arr1)  # [0.0, 0.69314718, 1.09861229]
print(result)
print("############################# 三角函数 #############################")
result = np.sin(arr1)  # [0.84147098, 0.90929743, 0.14112001]
print(result)

print("############################# 广播机制 #############################")
arr1 = np.array([1, 2, 3])
arr2 = np.array([[1], [2], [3]])
print(arr1)
print(arr2)
result = arr1 + arr2
# result:
# [[2, 3, 4],
#  [3, 4, 5],
#  [4, 5, 6]]
print(result)

result = arr1 + 5  # [6, 7, 8]
print(result)

print("############################# 统计函数 #############################")
arr = np.array([1, 2, 3, 4, 5])
min_val = np.min(arr)  # 1
max_val = np.max(arr)  # 5
print(min_val, max_val)

total = np.sum(arr)  # 15
print(total)

mean = np.mean(arr)  # 3.0
print(mean)

median = np.median(arr)  # 3.0
print(median)

std_dev = np.std(arr)  # 1.41421356
variance = np.var(arr)  # 2.0
print(std_dev)
print(variance)

print("############################# 高级统计函数 #############################")
arr = np.array([1, 2, 3, 4, 5])
cumsum = np.cumsum(arr)  # [1, 3, 6, 10, 15]
print(cumsum)

cumprod = np.cumprod(arr)  # [1, 2, 6, 24, 120]
print(cumprod)
percentile_50 = np.percentile(arr, 50)  # 3.0
print(percentile_50)

print("############################# 多维数组统计 #############################")
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
sum_axis_0 = np.sum(arr2, axis=0)  # [5, 7, 9]
sum_axis_1 = np.sum(arr2, axis=1)  # [6, 15]
print(sum_axis_0)
print(sum_axis_1)

mean_axis_0 = np.mean(arr2, axis=0)  # [2.5, 3.5, 4.5]
mean_axis_1 = np.mean(arr2, axis=1)  # [2.0, 5.0]
print(mean_axis_0)
print(mean_axis_1)
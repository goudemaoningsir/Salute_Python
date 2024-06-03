import pandas as pd

# 从列表创建Series
data = [1, 2, 3, 4, 5]
s = pd.Series(data)
print(s)

# 指定索引创建Series
index = ['a', 'b', 'c', 'd', 'e']
s = pd.Series(data, index=index)
print(s)

# 从字典创建Series
data = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
s = pd.Series(data)
print(s)

# 从标量创建Series
s = pd.Series(5, index=index)
print(s)

print(s[0])     # 通过位置访问元素
print(s['a'])   # 通过标签访问元素

# 切片
print(s[:3])    # 获取前三个元素

# 算术运算
s1 = pd.Series([1, 2, 3, 4, 5], index=index)
s2 = pd.Series([10, 20, 30, 40, 50], index=index)
print(s1 + s2)  # 对应位置元素相加

# 应用函数
print(s.apply(lambda x: x ** 2))  # 对每个元素应用平方函数
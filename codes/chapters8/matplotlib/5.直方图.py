import matplotlib.pyplot as plt

# 数据
data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]

# 创建直方图
plt.hist(data, bins=5)

# 显示图表
plt.show()
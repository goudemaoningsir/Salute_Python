import matplotlib.pyplot as plt

# 数据
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

# 修改线条样式
plt.plot(x, y, linestyle='--')  # 虚线

# 修改标记样式
plt.plot(x, y, marker='o')  # 圆点标记

# 修改线条颜色
plt.plot(x, y, color='red')  # 红色线条

# 修改线条和标记的颜色和样式
plt.plot(x, y, color='green', linestyle='--', marker='^', markerfacecolor='blue', markersize=10)

# 显示图表
plt.show()
import matplotlib.pyplot as plt

# 数据
x = [1, 2, 3, 4, 5]
y1 = [1, 4, 9, 16, 25]
y2 = [1, 2, 3, 4, 5]

# 创建图表
plt.figure()

# 第一个子图
plt.subplot(1, 2, 1)
plt.plot(x, y1)
plt.title("Plot 1")

# 第二个子图
plt.subplot(1, 2, 2)
plt.plot(x, y2)
plt.title("Plot 2")

# 显示图表
plt.show()
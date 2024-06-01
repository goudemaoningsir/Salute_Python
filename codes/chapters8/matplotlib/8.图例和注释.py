import matplotlib.pyplot as plt

# 数据
x = [1, 2, 3, 4, 5]
y1 = [1, 4, 9, 16, 25]
y2 = [1, 2, 3, 4, 5]

# 创建图表
plt.plot(x, y1, label='y = x^2')
plt.plot(x, y2, label='y = x')

# 添加图例
plt.legend()

# 显示图表
plt.show()

################################# 注释
# 数据
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

# 创建图表
plt.plot(x, y)

# 添加注释
plt.annotate('Square of 3', xy=(3, 9), xytext=(4, 15),
             arrowprops=dict(facecolor='black', shrink=0.05))

# 显示图表
plt.show()
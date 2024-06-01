import matplotlib.pyplot as plt

# 数据
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

# 创建折线图
plt.plot(x, y)

# 添加标题、轴标签和网格
plt.title("Sample Line Plot")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.grid(True)

# 保存图表为PNG文件
plt.savefig("line_plot.png")
# 保存图表为PDF文件
plt.savefig("line_plot.pdf")

# 显示图表
plt.show()
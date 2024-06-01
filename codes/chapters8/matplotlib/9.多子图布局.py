import matplotlib.pyplot as plt

# 数据
x = [1, 2, 3, 4, 5]
y1 = [1, 4, 9, 16, 25]
y2 = [1, 2, 3, 4, 5]

# 创建图表
fig, (ax1, ax2) = plt.subplots(1, 2)

# 第一个子图
ax1.plot(x, y1)
ax1.set_title('Plot 1')

# 第二个子图
ax2.plot(x, y2)
ax2.set_title('Plot 2')

# 显示图表
plt.show()


import matplotlib.gridspec as gridspec

# 数据
x = [1, 2, 3, 4, 5]
y1 = [1, 4, 9, 16, 25]
y2 = [1, 2, 3, 4, 5]
y3 = [2, 3, 4, 5, 6]
y4 = [3, 4, 5, 6, 7]

# 创建图表
fig = plt.figure()
gs = gridspec.GridSpec(2, 2)

# 第一个子图
ax1 = fig.add_subplot(gs[0, 0])
ax1.plot(x, y1)
ax1.set_title('Plot 1')

# 第二个子图
ax2 = fig.add_subplot(gs[0, 1])
ax2.plot(x, y2)
ax2.set_title('Plot 2')

# 第三个子图
ax3 = fig.add_subplot(gs[1, 0])
ax3.plot(x, y3)
ax3.set_title('Plot 3')

# 第四个子图
ax4 = fig.add_subplot(gs[1, 1])
ax4.plot(x, y4)
ax4.set_title('Plot 4')

# 显示图表
plt.show()
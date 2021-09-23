import matplotlib.pyplot as plt
import numpy as np
# import seaborn

# 折线图
# 生成x数据 从0-10平均分成500份
x = np.linspace(0, 10, 500)
plt.plot(x, np.sin(x))
plt.show()

# 柱状图
x = [0, 1, 2, 3, 4, 5]
plt.bar(x, [1, 4, 5, 6, 3, 2])
plt.show()

# 散点图
plt.scatter(x, [1, 4, 5, 6, 3, 2])
plt.show()

# 盒图
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 20]
plt.boxplot(x)
plt.show()

# 子图 2行2列 14位置放子图
figure = plt.figure()
ax1 = figure.add_subplot(2, 2, 1)
ax2 = figure.add_subplot(2, 2, 4)
plt.show()

# 其他方法
# 解决中文字体问题
plt.rcParams['font.sans-serif'] = ['FangSong']
plt.rcParams['axes.unicode_minus'] = False
# xy轴标签
x = np.linspace(0, 10, 500)
plt.plot(x, np.sin(x))
plt.xlabel("x")
plt.ylabel("sinx")
# xy轴刻度标签
plt.xticks(rotation=45)
plt.yticks(rotation=45)
plt.show()

# seaborn绘制
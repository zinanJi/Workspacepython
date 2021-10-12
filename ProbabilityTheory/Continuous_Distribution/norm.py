from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np
import seaborn

seaborn.set()

# 正态分布
# 因为我们研究的对象具有同质性，所以其特征往往是趋同的，即存在一个基准；
# 但由于个体变异的存在（当然变异不会太大），这些特征又不是完全一致，所以会以一定的幅度在基准的上下波动，
# 从而形成了中间密集，两侧稀疏的特征。
# 均值可取实数轴上的任意数值，决定正态曲线的具体位置；标准差决定曲线的“陡峭”或“扁平”程度
# 标准差越大，正态曲线越扁平；标准差越小，正态曲线越陡峭。 
# 标准差越小，意味着大多数变量值离均数的距离越短，因此大多数值都紧密地聚集在均数周围

# subplots返回的值的类型为元组，其中包含两个元素：第一个为一个画布，第二个是子图
fig, ax = plt.subplots(1, 1)

# loc specifies the mean,scale specifies the standard deviation.
norm0 = norm(loc=0, scale=1)
norm1 = norm(loc=1, scale=2)

# 产生-10到10的等差数列，个数为1000
x = np.linspace(-10, 10, 1000)

# 生成折线图 lw是宽度，alpha是透明度
ax.plot(x, norm0.pdf(x), color='red', lw=5, alpha=0.6, label='loc=0, scale=1')
ax.plot(x, norm1.pdf(x), color='blue', lw=5, alpha=0.6, label='loc=1, scale=2')

# 生成图例 loc 是摆放位置 frameon 是绘制图例框架
ax.legend(loc='best', frameon=False)

plt.show()


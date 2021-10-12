from scipy.stats import binom
import matplotlib.pyplot as plt
import seaborn

seaborn.set()

fig, ax = plt.subplots(3, 1)
params = [(10, 0.25), (10, 0.5), (10, 0.8)]
x = range(0, 11)
for i in range(len(params)):
    # 生成服从指定参数n,p的二项分布随机变量
    binom_rv = binom(n=params[i][0], p=params[i][1])
    # 分别进行pmf绘制
    ax[i].set_title('n={},p={}'.format(params[i][0], params[i][1]))
    ax[i].plot(x, binom_rv.pmf(x), 'bo', ms=8)
    ax[i].vlines(x, 0, binom_rv.pmf(x), colors='b', lw=3)
    ax[i].set_xlim(0, 10)
    ax[i].set_ylim(0, 0.35)
    ax[i].set_xticks(x)
    ax[i].set_yticks([0, 0.1, 0.2, 0.3])
plt.tight_layout()
plt.show()

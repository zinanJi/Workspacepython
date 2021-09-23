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
    # 进行10万次模拟采样，并归一化频数绘制成图，将其作为概率的近似
    rvs = binom_rv.rvs(size=100000)

    ax[i].hist(rvs, bins=11, density=True, stacked=True)
    ax[i].set_title('n={},p={}'.format(params[i][0], params[i][1]))
    ax[i].set_xlim(0, 10)
    ax[i].set_ylim(0, 0.4)
    ax[i].set_xticks(x)
    print('rvs{}:{}'.format(i, rvs))
plt.tight_layout()
plt.show()

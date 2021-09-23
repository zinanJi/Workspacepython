from scipy.stats import geom
import numpy as np
import matplotlib.pyplot as plt
import seaborn

seaborn.set()

x = range(1, 21)
# 生成服从p=0.5的几何分布随机变量
geom_rv = geom(p=0.5)
geom_rvs = geom_rv.rvs(size=100000)

plt.hist(geom_rvs, bins=20, density=True, stacked=True)
plt.gca().axes.set_xticks(x)

mean, var, skew, kurt = geom_rv.stats(moments='mvsk')
E_sim = np.mean(geom_rvs)
S_sim = np.std(geom_rvs)
V_sim = S_sim * S_sim

print('mean={},var={}'.format(mean, var))
print('E_sim={},V_sim={}'.format(E_sim, V_sim))

plt.show()
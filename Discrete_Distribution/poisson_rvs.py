from scipy.stats import poisson
import numpy as np
import matplotlib.pyplot as plt
import seaborn

seaborn.set()

lambda_ = 2

x = range(0, 11)
# 生成服从λ=2的泊松分布随机变量,并采样
data = poisson.rvs(mu=lambda_, size=100000)
plt.figure()

plt.hist(data, density=True, stacked=True)
plt.gca().axes.set_xticks(x)

mean = np.mean(data)
var = np.square(np.std(data))

print('mean={},var={}'.format(mean, var))

plt.show()
from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np
import seaborn
seaborn.set()

norm_rv = norm(loc=2, scale=2)
norm_rvs = norm_rv.rvs(size=100000)
x = np.linspace(-10, 10, 1000)
# 曲线图
plt.plot(x, norm_rv.pdf(x), 'r', lw=5, alpha=0.6, label="`$\\mu$=2,$\\sigma=2$`")
# 折线图
plt.hist(norm_rvs, density=True, stacked=True, bins=50, alpha=0.6, edgecolor='k')
plt.legend()
plt.show()

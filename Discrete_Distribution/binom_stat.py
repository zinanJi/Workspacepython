from scipy.stats import binom
import numpy as np

binom_rv = binom(n=10, p=0.25)
# 用函数包中的方法计算分布的各个理论统计值
# mean - 均值， var - 方差， skew - 偏度， kurt - 峰度, moments?
mean, var, skew, kurt = binom_rv.stats(moments='mvsk')

# 采样得到的样本数据计算出均值和方差
binom_rvs = binom_rv.rvs(size=100000)
E_sim = np.mean(binom_rvs)
S_sim = np.std(binom_rvs)
V_sim = S_sim * S_sim

# 通过公式直接计算出来的理论值
calmean = 10 * 0.25
calvar = 10 * 0.25 * 0.75

# 三种方法比较验证出采样样本数据计算值和理论值基本上相等
print('mean={},var={}'.format(mean, var))
print('E_sim={},V_sim={}'.format(E_sim, V_sim))
print('E=np={},V=np(1-p)={}'.format(calmean, calvar))

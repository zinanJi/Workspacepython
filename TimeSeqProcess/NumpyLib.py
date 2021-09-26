import numpy as np

# 将日期编码成 64 位的整数，让日期数组非常的紧凑，提升向量运算的效率。
date = np.array('2021-09-27', dtype=np.datetime64)
print(date)

# 基于datetime64，向量化计算
# eg. 想获得从 2021 年 9 月 27 日起，连续 12 天的日期所组成的数组
print(date + np.arange(12))

# 选择时间精度，numpy自动判断，也可显式指定
print(np.datetime64('2021-09-27'))
print(np.datetime64('2021-09-27 12:00'))
print(np.datetime64('2021-09-27 12:00', 'ns'))

# 不足：缺少了很多 datetime 和 dateutil 中具备的方便易用的函数方法。

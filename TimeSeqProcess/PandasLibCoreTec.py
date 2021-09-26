from pandas_datareader import data
import matplotlib.pyplot as plt
import pandas as pd
import seaborn

seaborn.set()

stock_code = '0700.hk'
start_date = '2000-01-01'
end_date = '2019-05-01'

stock_info = data.get_data_yahoo(stock_code, start_date, end_date)
print(stock_info.head())
print(type(stock_info))

# 重采样和频率转换
# resample & asfreq
# 用于解决频率采样的问题
# resample 是以数据累计为基础，获取的不是指定频率下某个时间点的数值，而是整个重采样频率周期内的统计值（均值、和等等）。
# asfreq 强调数据的选择，获取的就是指定频率下具体时间点对应的数值。
stock_info['Close'].plot(color='b', alpha=0.5, style='-')
stock_info['Close'].resample('BA').mean().plot(color='r', alpha=0.5, style=':')
stock_info['Close'].asfreq('BA').plot(color='g', alpha=0.5, style='--')
plt.legend(['original', 'resample', 'asfreq'], loc='upper left')
plt.show()

# 缺失值的处理
# 股票按自然天重采样就会有缺失值NaN
print(stock_info['Close'].asfreq('D'))
stock_info['Close'].asfreq('D').plot(marker='o')
plt.show()
# 向前填充：让缺失值等于前一个时间点的值
# 向后填充：让缺失值等于后一个时间点的值
fig, ax = plt.subplots(2, sharex=True)
stock_info['Close'].asfreq('D').plot(ax=ax[0], marker='o')
stock_info['Close'].asfreq('D', method='bfill').plot(ax=ax[1],
                                                     color='g',
                                                     alpha=0.5,
                                                     style='--o')
stock_info['Close'].asfreq('D', method='ffill').plot(ax=ax[1],
                                                     color='r',
                                                     alpha=0.5,
                                                     style='-o')
plt.legend(['back-fill', 'forward-fill'])
plt.show()

# 时间的迁移方法.shift()
# 将时间序列整体向前移动，方便计算指定周期的数据差值。
fig, ax = plt.subplots(2, sharex=True)

tencent = stock_info['Close'].asfreq('D', method='ffill')
tencent.plot(ax=ax[0], color='r', alpha=0.5)
tencent.shift(365).plot(ax=ax[1], color='b', alpha=0.5)

plt.show()

# 移动时间窗口.rolling()
# 可用于连续观测指定大小的时间窗口内数据的统计值
rolling = tencent.rolling(365)
data = pd.DataFrame({'original': tencent,
                     'rolling-mean': rolling.mean(),
                     'rolling-std': rolling.std()})

data.plot(style=['-','--',':'])
plt.show()
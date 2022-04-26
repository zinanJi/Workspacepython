import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdate
import numpy as np
from datetime import datetime

data = pd.read_csv("F:/data/handled/data3.csv",
                   header=0,
                   encoding="ANSI")


plt.rcParams['font.sans-serif'] = 'Simhei'  #设置中文
fig1 = plt.figure(figsize=(8, 8))  #设置长宽，建立窗口
data['SJSJ']= pd.to_datetime(data.SJSJ)
xs = data['SJSJ'].astype(str)
data = data.set_index(['SJSJ'])
print(data)
xs = [datetime.strptime(d, '%Y-%m-%d').date() for d in xs]
ax1 = fig1.add_subplot(1, 1, 1)
ax1.xaxis.set_major_formatter(mdate.DateFormatter('%Y-%m-%d'))  # 设置时间标签显示格式
plt.xticks(pd.date_range(xs[1], xs[-1]))

plt.plot(xs, data.ZXYGZ, color='k', label='ZXYGZ')
plt.plot(xs, data.ZXYGF, color='b', label='ZXYGF')
plt.plot(xs, data.ZXYGG, color='r', label='ZXYGG')

plt.legend(loc=0)

plt.grid(True)
plt.show()
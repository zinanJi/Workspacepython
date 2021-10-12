import pandas as pd
import numpy as np
from datetime import datetime

date = pd.to_datetime('27/09/2021')
print(type(date))
print(date)
print(date.strftime('%y-%m-%d,%A'))

# timedelta_64表示时间间隔，作向量化运算
print(pd.to_timedelta(np.arange(12), 'D'))
print(type(pd.to_timedelta(np.arange(12), 'D')))
print(date + pd.to_timedelta(np.arange(12), 'D'))

# 时间序列的基本表示
# 时间序列的索引数据是时间/日期类型的数据
index = pd.DatetimeIndex([
    '2019-9-1', '2019-10-1', '2020-9-1', '2020-10-1', '2021-9-1', '2021-10-1'
])
data = pd.Series([1, 2, 3, 4, 5, 6], index=index)
print(data)
# 三种索引方式
# 查看某个具体时间点对应的值
print(data['2021-9-1'])
# 查看时间区间内的取值
print(data['2019-10-1':'2021-9-1'])
# 查看某个指定年份的取值
print(data['2020'])

# 时间戳数据类型及索引结构Timestamp & DatetimeIndex
# pandas提供了Timestamp类型数据，在 numpy.datetime64 的基础上构建，又兼具了原生datetime类型的易用性
# 传入时间序列，会返回一个DatetimeIndex时间索引类型
dates = pd.to_datetime(
    ['20210927', '28/09/2021', '2021-09-29',
     datetime(2021, 9, 30)])
print(type(dates))
print(dates)

# 可指定起止日期时间和频率，一次性生成有规律的时间序列 freq为频率，默认指定为天'D',可设置为小时'H'
dates1 = pd.date_range('2021/9/1', '2021/10/1')
dates2 = pd.date_range('2021/9/1', '2021/9/2', freq='H')

print(dates1)
print(dates2)

# 可指定起始时间和周期（和频率）
dates1 = pd.date_range('2021/9/1', periods=5)
dates2 = pd.date_range('2021/9/1', periods=8, freq='H')

print(dates1)
print(dates2)

# 时间周期数据及索引结构 Period & PeriodIndex
# 生成一个从2021年9月开始，以月为频率的时间构造器
prd = pd.Period('2021-9', freq='M')
print(prd, type(prd))
print(prd + 1)
print(prd - 5)

# 生成索引PeriodIndex
dates = pd.to_datetime(
    ['2021-9-27', '20210928', '29/9/2021',
     datetime(2021, 9, 30)])
# 直接将DatetimeIndex转换成了PeriodIndex，索引中的每一个数据元素都是 Period 类型。
pnd = dates.to_period('D')
print(pnd)
print(type(pnd))
print(pnd[1])
print(type(pnd[1]))

# 调用 pd.period_range() 方法处理有规律的周期序列
prng = pd.period_range('2019-9-27', '2020-9-27', freq='M')
print(prng, type(prng))

# 利用pd.period_range()生成的索引构造一个Series对象
ts = pd.Series(np.random.rand(len(prng)), index=prng)
print(ts)

# 时间增量数据及索引结构 Timedelta & TimedeltaIndex
# 基于numpy.timedelta64
dates = pd.date_range('2021/09/27', periods=5)
delta = dates - dates[0]
print(delta, type(delta[0]))

deltas = pd.timedelta_range(0, periods=5, freq='H')
print(deltas)

# 实际上还有很多非常实用的时间频率，比如月末（M）、季末（Q）、年末（A）,
# 所有的频率前加 B，就自动变成了工作日的月末（BM）、季末（BQ）和年末（BA）
# 后缀再加上S则相应的变成了月初（MS）、季初（QS）、年初（AS）
# 以此类推还可以在前面再加 B，限定在工作日。
print(pd.date_range('2021-9-1', periods=10, freq='B'))
print(pd.date_range('2021-9-1', periods=7, freq='BMS'))
# 时分秒按需进行自定义
print(pd.timedelta_range(0, periods=9, freq='1H30T'))

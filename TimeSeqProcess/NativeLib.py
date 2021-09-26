from datetime import datetime
from dateutil import parser

# 生成日期类型的对象
date = datetime(year=2021, month=9, day=27)
print(date)

# 文本日期的自动解析
sdate1 = '2021-9-27'
sdate2 = '27/9/2021'
sdate3 = '2021/9/27'

date1 = parser.parse(sdate1)
date2 = parser.parse(sdate2)
date3 = parser.parse(sdate3)

print(date1)
print(date2)
print(date3)

# 提取日期中的要素信息
now = datetime.now()
print(now)
print(now.strftime("DATE:%Y-%m-%d %A TIME:%H:%M:%S"))

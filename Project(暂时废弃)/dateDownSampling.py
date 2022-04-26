import pandas as pd
import numpy as np


def read():
    BM = pd.read_csv("C:/Jzn/project/DataSet/Legit_csv/ST_KH_JL_BM.csv",
                     header=0,
                     encoding="ANSI",
                     dtype={
                         'CLDBS': np.float32,
                         'SJSJ': np.str_,
                         'ZXYGZ': np.float32,
                         'ZXYGF': np.float32,
                         'ZXYGP': np.float32,
                         'ZXYGG': np.float32,
                         'ZXWGZ': np.float32,
                         'ZXYGJ': np.float32,
                         'FXYGZ': np.float32,
                         'FXYGF': np.float32,
                         'FXYGP': np.float32,
                         'FXYGG': np.float32,
                         'FXYGJ': np.float32,   
                         'FXWGZ': np.float32,
                     },)

    CLD = pd.read_csv("C:/Jzn/project/DataSet/Legit_csv/ST_KH_JL_CLD.csv",
                      header=0,
                      usecols=["CLDBS", "YHBH"],
                      dtype={
                          'CLDBS': np.float32,
                      })

    DA = pd.read_csv(
        "C:/Jzn/project/DataSet/Legit_csv/ST_KH_DA.csv",
        header=0,
        usecols=["YHBH"],
    )
    return BM, CLD, DA


def data_generator(BM, CLD, DA):
    """ # 得到一个用户
    # BM left join CLD
    merge1 = pd.merge(left=BM, right=CLD, on="CLDBS")
    print(merge1.head())
    # left join DA
    merge2 = pd.merge(left=merge1, right=DA, on="YHBH")
    print(merge2.head())
    # merge2.to_csv(r'data.csv',encoding="ANSI")

    # BM.pivot(index='CLDBS', columnsC:/Jzn/project='SJSJ', values='3-voltage')
    merge2["SJSJ"] = pd.to_datetime(merge2.SJSJ)
    print(merge2.head(10)) """

    # 发生异常: ValueError
    # Index contains duplicate entries, cannot reshape
    # data = merge2.pivot(index='YHBH', columns='SJSJ', values='ZXYGZ')

    # 处理DA用户编号，去重+全采样+重索引
    DA = DA.drop_duplicates('YHBH').sample(frac=1).reset_index(drop=True)
    print("YHBH have dropped duplicates")
    # 处理CLD
    count = 0
    preparedData = pd.DataFrame()
    preparedIndex = pd.DataFrame()
    for i, YHBH in DA['YHBH'].items():
        # 保证一个用户对应一个测量点,总共16354个
        YH_CLD = CLD.loc[CLD['YHBH'] == YHBH].drop_duplicates('YHBH')
        CLDBS = YH_CLD['CLDBS']
        if not CLDBS.empty:
            count += 1
        else:
            continue
        if count > 1000:
            break
        """ data = BM.loc[BM['CLDBS'] == CLDBS.iloc[0]].loc[:, 'SJSJ':'FXWGZ'].T
        data.columns = data.iloc[0].values
        data = data.drop(axis=0, index='SJSJ') """

        BM["SJSJ"] = pd.to_datetime(BM.SJSJ)
        data = BM.loc[BM['CLDBS'] == CLDBS.iloc[0]]
        data['CLDBS'] = CLDBS.iloc[0]
        data = data.drop_duplicates('SJSJ').sort_values(by='SJSJ')

        # 处理缺省值

        # 处理成每日数据，设置时间为n天，从1.1到x.x，若少于则丢弃

        data = data.groupby(data.SJSJ.dt.date).agg({
            'ZXYGZ': 'mean',
            'ZXYGF': 'mean',
            'ZXYGP': 'mean',
            'ZXYGG': 'mean',
            'ZXWGZ': 'mean',
            'ZXYGJ': 'mean',
            'FXYGZ': 'mean',
            'FXYGF': 'mean',
            'FXYGP': 'mean',
            'FXYGG': 'mean',
            'FXYGJ': 'mean',
            'FXWGZ': 'mean',
            'CLDBS': 'median'
        }).reset_index(drop=False).head(30)

        if not data.empty:

            # 不为连续时间段
            data['date'] = (data['SJSJ'] -
                            data['SJSJ'].shift(1)) == pd.Timedelta('1d')
            print(data)
            print(len(data['date']) - data['date'].sum())
            if len(data['date']) - data['date'].sum() != 1:
                count -= 1
                break

            print("data " + str(count) + " have changed")
            preparedIndex = pd.concat([preparedIndex, YH_CLD], axis=0)
            """ print(preparedData.shape)
            print(data.shape) """
            preparedData = pd.concat([preparedData, data], axis=0)
        else:
            count -= 1
    print("end")
    print("involve " + str(count) + " data")
    print("writting...")
    preparedIndex.to_csv(r'link.csv', encoding="ANSI")
    preparedData.to_csv(r'data.csv', encoding="ANSI")
    print("finished")
    return preparedData


BM, CLD, DA = read()
preparedData = pd.DataFrame()
BM["SJSJ"] = pd.to_datetime(BM.SJSJ)
grouping = BM.groupby('CLDBS')
count = 0
for CLDBS, group in grouping:
    count += 1
    group['SJSJ'] = pd.to_datetime(group['SJSJ'])
    group = group.drop_duplicates(['SJSJ']).sort_values(by=['SJSJ'])
    group = group.set_index(['SJSJ'])
    # print(group)
    group.resample('D').mean()
    """ group = group.fillna(method='ffill')
    group = group.fillna(method='bfill')
    group = group.fillna(0) """
    # preparedData = pd.concat([preparedData, group], axis=0)
    print("writting...")
    preparedData.to_csv('F:/data/data' + str(count) + '.csv', encoding="ANSI")
    print(str(count)+"finished")
""" print("writting...")
preparedData.to_csv('F:/data/data1.csv', encoding="ANSI")
print("finished") """
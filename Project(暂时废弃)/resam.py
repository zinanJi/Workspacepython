import pandas as pd
import numpy as np

BM = pd.read_csv("F:/data/data18.csv",
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
                 })

BM["SJSJ"] = pd.to_datetime(BM.SJSJ)
BM = BM.drop_duplicates(['SJSJ']).sort_values(by=['SJSJ'])

# print(group)
BM = BM.groupby(BM.SJSJ.dt.date).mean().reset_index(drop=False)
BM = BM.set_index(['SJSJ'])
BM = BM.fillna(method='ffill')
BM = BM.fillna(method='bfill')
BM = BM.fillna(0)
print("writting...")
print(BM)
BM.to_csv('F:/data/data18-1.csv', encoding="ANSI")
print("finished")
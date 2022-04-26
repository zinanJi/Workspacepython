import pandas as pd
import numpy as np

BM = pd.read_csv("C:/Jzn/project/DataSet/Legit_csv/test.csv",
                 header=0,
                 encoding="UTF8",
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

sampleBM = pd.read_csv("C:/Jzn/project/DataSet/Legit_csv/ST_KH_JL_BM.csv",
                       header=0,
                       encoding="UTF8",
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
                       },
                       nrows=100000)
""" BM["SJSJ"] = pd.to_datetime(BM.SJSJ)
BM.set_index('SJSJ') """
""" data = BM.loc[:, 'SJSJ':'FXWGZ'].T
data.columns = data.iloc[0].values
# print(data.columns)
data = data.drop(axis=0, index='SJSJ') """
sampleBM['SJSJ'] = pd.to_datetime(sampleBM['SJSJ'])
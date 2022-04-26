import pandas as pd
# import numpy as np

DA = pd.read_csv("C:/Jzn/project/DataSet/Legit_csv/ST_KH_DA.csv",
                 header=0,
                 usecols=["YHBH"])

# 处理DA，根据用户编号去重+随机采样（打乱顺序）+重索引
DA1 = DA.drop_duplicates(['YHBH'])
""" print(DA1.index)
print(DA1) """
DA2 = DA.drop_duplicates(['YHBH']).reset_index(drop=True)
""" print(DA2.index)
print(DA2) """
# 打乱后的数据index也是乱的，用reset_index重新加一列index，drop=True表示丢弃原有index一列
DA3 = DA.drop_duplicates(['YHBH']).sample(frac=1).reset_index(drop=True)
""" print(DA3.shape)
print(DA3.index) """

CLD = pd.read_csv(
    "C:/Jzn/project/DataSet/Legit_csv/ST_KH_JL_CLD.csv",
    header=0,
    usecols=["CLDBS", "YHBH"],
)
count = 0

for i, YHBH in DA3['YHBH'].items():
    # 保证一个用户对应一个测量点,总共16354个
    CLDBS = CLD.loc[CLD['YHBH'] == YHBH].drop_duplicates('YHBH')['CLDBS']
    if not CLDBS.empty:
        count += 1
print(count)



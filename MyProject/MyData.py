# pytorch中加载数据的顺序是：
# ①创建一个dataset对象
# ②创建一个dataloader对象
# ③循环dataloader对象，将data,label拿到模型中去训练

from torch.utils.data import Dataset, DataLoader
import pandas as pd
import torch
import numpy as np

seq_len = 1

# 定义dataset类才能创建dataset对象
# 至少包含3个函数：
# __init__: 传入数据，或者加载数据
# __len__: 返回这个数据集有多少个item
# __getitem__:返回一条训练数据，并将其转化为Tensor


class Mydata(Dataset):  # 继承torch.utils.data.Dataset
    # 重构__init__
    # 定义参数csv_file, 创建对象的时候传入文件路径
    # 可定义参数flag，创建对象的时候区分训练集、测试集、验证集  assert flag in ['train', 'test', 'valid']
    def __init__(self, csv_file):
        super().__init__()
        self.data = pd.read_csv(
            './Project(暂时废弃)/data9.csv', header=0).reset_index()
        # 处理后的源数据结构应该是(data, CLD_index, seq_len, n_feature) todo
        # header = 0 首行为列名

        # 待废弃：把SJSJ临时处理成int
        self.data['SJSJ'] = pd.to_datetime(self.data.SJSJ)
        self.data['SJSJ'] = self.data['SJSJ'].apply(
            lambda x: x.strftime('%Y%m%d'))
        self.data = self.data[:].astype(float)

        # 打印数据shape
        print("X.shape:{}\n".format(self.data.shape))

        # print("X.index.values:{}\n".format(self.data.index.values))
        # print("X.column.values:{}\n".format(self.data.columns.values))

    # 重构__len__
    # __getitem__的index的取值范围是根据len的返回值确定的
    # 若__len__的返回值是4
    # 则这个index会在0，1，2，3这个范围内。
    def __len__(self):
        print(int(len(self.data) / seq_len))
        return int(len(self.data) / seq_len)

    # 重构__getitem__
    # dataLoader加载的时候会调用到它
    # 我们需要返回一个二维表作为每一个模型的样本输入
    def __getitem__(self, index):
        # 取seq_len行数据，从第二列到最后一列
        item = self.data.iloc[index * seq_len:(index + 1) * seq_len, :]
        # 将样本数据转化为Tensor数据类型
        item = np.array(item)
        item = torch.tensor(item)

        return item


# 测试用例
if __name__ == '__main__':

    ds = Mydata('./Project/data9.csv')

    dataloader = DataLoader(ds,
                            batch_size=1,
                            shuffle=False,)
    for i_batch, batch_data in enumerate(dataloader):
        if i_batch == 1:
            print(i_batch)
            print(batch_data.shape)
            print(batch_data)

print("finished loading")

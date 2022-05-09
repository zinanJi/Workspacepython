from torch.utils.data import DataLoader, Dataset
import pandas as pd
import torch
import numpy as np


def show_dataset():
    data = pd.read_csv('./Project/data9.csv', header=0)
    n = data.shape[0]
    print(n)
    print(data.index)
    # 获取行用 data.loc[]/data.iloc[]
    # 获取列用 data[]
    print(data.iloc[0])


class MyData(Dataset):
    def __init__(self, root_dir, csv_file, transform=None) -> None:
        super().__init__()
        self.root_dir = root_dir
        self.transform = transform
        # self.dataName = os.listdir(self.root_dir)
        self.data = pd.read_csv(csv_file, header=0).reset_index()

        self.data['SJSJ'] = pd.to_datetime(self.data.SJSJ)
        self.data['SJSJ'] = self.data['SJSJ'].apply(
            lambda x: x.strftime('%Y%m%d'))
        # print(self.data)
        self.data = self.data.drop(['CLDBS'], axis=1)
        self.data = self.data[:].astype(float)
        # self.data = self.data.set_index(['SJSJ'])
        max_value = self.data.max()
        min_value = self.data.min()
        # print(max_value)
        # print(min_value)
        self.data = (self.data - min_value) / (max_value - min_value + 1e-6)
        print(self.data)

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):

        item = self.data.iloc[index, 1:]
        # print(item)
        item = item.tolist()
        item = np.array(item)
        item = torch.from_numpy(item)
        return item


if __name__ == '__main__':
    # show_dataset()
    ds = MyData('root', './Project/data9.csv')
    """ print(len(ds))
    print(ds[0])
    print(ds) """

    dataloader = DataLoader(ds,
                            batch_size=4,         # 一次几行数据
                            shuffle=False,)
    for i_batch, batch_data in enumerate(dataloader):
        """ print(i_batch)
        print(batch_data.shape)
        print(batch_data)
 """

print("finished loading")

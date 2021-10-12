import pandas as pd
import numpy as np
import matplotlib as plt

# SOM网络只有输入层和输出（竞争）层，高维=>低维，同时保持样本相对距离
# SOM网络包含初始化、竞争、迭代三块内容

# 初始化过程
# 1. 归一化数据集
# 2. 设计竞争层结构。一般根据预估的聚类簇数进行设置。比如要分成4类，那我可以将竞争层设计为2*2，1*4，4*1
# 3. 预设竞争层神经元的权重结点。
#    一般我们会根据输入数据的维度和竞争层预估的分类数来设置权重节点，若输入为二维数据，最终聚类为4类，则权重矩阵就是2*4
# 4. 初始化邻域半径、学习率

# 竞争过程
# 1. 随机选择样本，根据权重节点计算到竞争层每个神经元节点的距离。一般我们选择欧式距离公式求距离
# 2. 选择优胜节点，通过竞争，选择距离最小的神经元节点作为优胜节点

# 迭代过程
# 1. 圈定出优胜邻域内的所有节点。根据邻域半径，圈定出距离小于邻域半径的节点，形成优胜邻域。
# 2. 对优胜邻域内的节点权重进行迭代更新。更新的思想是越靠近优胜节点，更新幅度越大；越远离优胜节点，更新幅度越小
#    故我们需要对不同的节点增加一个更新约束，一般可以高斯函数求得。
# 最后重复竞争、迭代步骤，直至迭代结束


class SOMnet(object):
    # 归一化函数
    def normalize(self, data):
        data[u'好瓜'] = data[u'好瓜'].map({'是': 1, '否': 0})
        return data

    def train(self, dataset, m, n):
        self.dataset = dataset  # 输入数据集
        # 初始化过程
        dataset = self.normalize(dataset)  # 归一化数据集
        n_samples, n_feature = dataset.shape  # 载入数据集
        # 设计竞争层结构
        self.gridLocation = self.init_grid(m, n)
        self.gridDist = self.calgridDist(self.gridLocation)

        # 预设竞争层神经元的权重结点
        w = np.random.rand((m * n, n_feature))  # ?

        # 确定迭代次数，不小于样本数的5倍
        if self.steps < 5 * n_samples:
            self.steps = 5 * n_samples

        # 重复竞争迭代过程
        for i in range(self.steps):
            # 竞争过程
            # 随机选择样本计算距离
            data = dataset[np.random.randint(0, n_samples, 1)[0], :]  # ?
            dataDist = [self.edist(data, w[row])
                        for row in range(len(w))]  # 列表生成式，for语句在后
            # 找到优胜节点
            winnerPointIdx = dataDist.index(min(dataDist))

            # 迭代过程
            # 确定学习率和邻域半径，并保存
            Rate, Round = 0
            # 圈定优胜邻域内的所有节点
            winnerRoundIdx = np.nonzero(
                self.gridDist[winnerPointIdx] < Round)[0]
            # 对优胜邻域内的节点权重进行迭代更新
            w[winnerRoundIdx] = w[winnerRoundIdx] + Rate * (data -
                                                            w[winnerRoundIdx])

        self.w = w
        self.normDataset = dataset

    # 根据训练出来的权重，将数据集进行聚类。
    def cluster(self, X):
        pass


# 读取数据集
trainSet = pd.read_csv('MachineLearning/watermelon_3_alpha.csv', delimiter=",")

som_self = SOMnet()
som_self.train(trainSet, 2, 1)
som_self_cluster = som_self.cluster(trainSet)
# 画图验证聚类结果
for cc in set(som_self_cluster):
    plt.scatter(trainSet[som_self_cluster == cc, 0],
                trainSet[som_self_cluster == cc, 1])
plt.show()

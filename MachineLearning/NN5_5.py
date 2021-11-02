import numpy as np


def dataSet():
    # 西瓜数据集离散化
    # 原数据一列表示一个样本，需要转置
    x = [[2, 3, 3, 2, 1, 2, 3, 3, 3, 2, 1, 1, 2, 1, 3, 1, 2],
         [1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 1, 2, 2, 2, 1, 1],
         [2, 3, 2, 3, 2, 2, 2, 2, 3, 1, 1, 2, 2, 3, 2, 2, 3],
         [3, 3, 3, 3, 3, 3, 2, 3, 2, 3, 1, 1, 2, 2, 3, 1, 2],
         [1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 1, 1, 2, 3, 2],
         [1, 1, 1, 1, 1, 2, 2, 1, 1, 2, 1, 2, 1, 1, 2, 1, 1],
         [0.697, 0.774, 0.634, 0.668, 0.556, 0.403, 0.481, 0.437, 0.666, 0.243, 0.245, 0.343, 0.639, 0.657, 0.360,
          0.593, 0.719],
         [0.460, 0.376, 0.264, 0.318, 0.215, 0.237, 0.149, 0.211, 0.091, 0.267, 0.057, 0.099, 0.161, 0.198, 0.370,
          0.042, 0.103]]
    x = np.array(x).T  # 样本属性集合，转置后的数据集⾏表示一个样本，列表示⼀个属性
    y = [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    y = np.array(y).T
    return x, y


def sigmod(x):
    return 1.0 / (1.0 + np.exp(-x))


# 参数为隐层神经元数目
def bpstand(hideNum):
    X, Y = dataSet()
    # v的下标是dh，二维矩阵，样本属性×隐层数目
    V = np.matrix(np.random.rand(len(X.T), hideNum))
    alpha = np.matrix(np.random.rand(1, hideNum))
    W = np.matrix(np.random.rand(hideNum, len(Y)))
    theta = np.matrix(np.random.rand(1, len(Y)))

    # 设置学习率
    rate = 0.1
    # 设置循环条件
    error = 0.001
    maxTrainNum = 1000000
    trainNum = 0
    loss = 10

    while(loss > error) and (trainNum < maxTrainNum):
        for k in range(X.shape[0]):  # 每个样本
            b = sigmod(X[k, :].dot(V) - alpha)
            y_estimate = sigmod(b.dot(W) - theta)
            loss = sum((y_estimate - Y[k]).dot((y_estimate - Y[k]).T)) * 0.5
            g = y_estimate.dot((1-y_estimate).T).dot(Y[k]-y_estimate)
            W += rate * b.T.dot(g)
            theta -= rate*g
            e = b.dot((1-b).T)*g.dot(W.T)
            V += rate * X[k].reshape(1, X[k].size).T.dot(e)
            alpha -= rate * e
            trainNum += 1

    print("总训练次数：", trainNum)
    print("最终损失：", loss)
    print("V：", V)
    print("alpha:", alpha)
    print("W：", W)
    print("theta:", theta)


def bpAccum(hideNum):
    X, Y = dataSet()
    # v的下标是dh，二维矩阵，样本属性×隐层数目
    V = np.matrix(np.random.rand(len(X.T), hideNum))
    alpha = np.matrix(np.random.rand(1, hideNum))
    W = np.matrix(np.random.rand(hideNum, len(Y)))
    theta = np.matrix(np.random.rand(1, len(Y)))

    # 设置学习率
    rate = 0.1
    # 设置循环条件
    error = 0.001
    maxTrainNum = 1000000
    trainNum = 0
    loss = 10

    while(loss > error) and (trainNum < maxTrainNum):
        for k in range(X.shape[0]):  # 每个样本
            b = sigmod(X[k, :].dot(V) - alpha)
            y_estimate = sigmod(b.dot(W) - theta)
            loss += sum((y_estimate - Y[k]).dot((y_estimate - Y[k]).T)) * 0.5
            trainNum += 1
        loss /= k
        g = y_estimate.dot((1-y_estimate).T).dot(Y[k]-y_estimate)
        W += rate * b.T.dot(g)
        theta -= rate*g
        e = b.dot((1-b).T)*g.dot(W.T)
        V += rate * X[k].reshape(1, X[k].size).T.dot(e)
        alpha -= rate * e
    
    print("总训练次数：", trainNum)
    print("最终损失：", loss)
    print("V：", V)
    print("alpha:", alpha)
    print("W：", W)
    print("theta:", theta)


if __name__ == '__main__':
    bpAccum(5)

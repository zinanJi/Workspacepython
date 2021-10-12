import numpy as np
import pandas as pd

dataset = pd.read_csv('MachineLearning/watermelon_3.csv', delimiter=",")

# according to P54--3.2
# process the dataset


# 定义激活函数
def sigmoid(x):
    return 1.0 / (1.0 + np.exp(-x))


# standard BP
# train_X,train_Y ———— 训练集
# numb ———— 隐层神经元个数
# inta ———— 学习率
def BP(train_X, train_Y, numb, inta):
    # 在(0,1)范围内随机初始化网络中所有连接权和阈值
    # 随机生成输入层到隐层的连接权 （.T为转置操作，len获取train_X的列数）
    v = np.matrix(np.random.rand(len(train_X.T), numb))
    # 随机生成隐层到输出层的连接权
    w = np.matrix(np.random.rand(numb, len(train_Y.T)))
    # 输出层神经元阈值
    thita = np.matrix(np.random.rand(len(train_Y.T)))
    # 隐层神经元阈值
    garma = np.matrix(np.random.rand(numb))

    temp = 0

    for i in range(len(train_X)):

        # 根据当前参数和式(5.3)计算当前样本的输出y_estimate
        # 隐层神经元的输入
        alpha = train_X[i].dot(v)
        # 隐层神经元的输出
        b = sigmoid(alpha)
        # 输出神经元的输入
        beta = b.dot(w)
        # 输出神经元的输出，求出y的估计值
        y_estimate = sigmoid(beta - thita)

        # 根据式(5.10)计算输出层神经元的梯度g
        g = y_estimate.dot((1 - y_estimate).T).dot(train_Y[i] - y_estimate)

        # 根据式(5.15)计算隐层神经元的梯度项e
        e = b.dot((1 - b).T).dot(g).dot(w.T)

        # 均方误差
        E = 1 / 2 * (y_estimate - train_Y[i]).dot((y_estimate - train_Y[i]).T)

        # 根据式(5.11)-(5.14)更新连接权w,v和阈值thita,garma
        if E > temp:
            w = w + inta * (b.T).dot(g)
            thita = thita - inta * g
            v = v + inta * (train_X[i].T).dot(e)
            garma = garma - inta * e
            temp = E

    return w, v, thita, garma


# 随机生成训练集x和y
x = np.matrix(np.random.rand(3, 4))
y = np.matrix(np.random.rand(3, 2))
print('x', x)
print('y', y)


def predict(X):
    alpha = X.dot(v)
    b = sigmoid(alpha)
    beta = b.dot(w)
    y_estimate = sigmoid(beta - thita)
    return y_estimate


# 调用BP函数
w, v, thita, garma = BP(x, y, 4, 0.01)
print('w', w)
print('v', v)
print('thita', thita)
print('garma', garma)
print('y_estimate', predict(x))

# MINST官网下载下来的4个压缩包放在工程的MNIST_data目录下
from tensorflow.contrib.learn.python.learn.datasets.mnist import read_data_sets

# 即可解析数据集
mnist = read_data_sets("MNIST_data/", one_hot=True)

print(mnist)
import torch
import torch.nn as nn


# https://blog.csdn.net/xieyan0811/article/details/103317103

# 全连接层则起到将学到的特征表示映射到样本的标记空间的作用。换句话说，就是把特征整合到一起（高度提纯特征），方便交给最后的分类器或者回归。
# nn.Linear()

connected_layer = nn.Linear(in_features=64 * 64 * 3, out_features=1)

input = torch.randn(1, 64, 64, 3)
print(input)

input = input.view(1, 64 * 64 * 3)
print(input)
print(input.shape)

output = connected_layer(input)
print(output)

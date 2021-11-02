import numpy as np
import torch

arr = np.ones((3, 3))
print("ndarray的数据类型：", arr.dtype)

# 创建存放在GPU的数据
# t = torch.tensor(arr, device='cuda')

t = torch.tensor(arr)
print(t)

x = torch.empty(5, 3)  # 创建一个5x3的未初始化的Tensor
print(x)

x = torch.rand(5, 3)  # 创建一个5x3的随机初始化的Tensor
print(x)

x = torch.zeros(5, 3, dtype=torch.long)  # 创建一个5x3的long型全0的Tensor
print(x)

x = torch.tensor([5.5, 3])  # 直接根据数据创建
print(x)

x = x.new_ones(5, 3,
               dtype=torch.float64)  # 返回的tensor默认具有相同的torch.dtype和torch.device
print(x)

x = torch.randn_like(x, dtype=torch.float)  # 指定新的数据类型
print(x)

# 返回的torch.Size其实就是一个tuple, 支持所有tuple的操作
print(x.shape)
print(x.size())

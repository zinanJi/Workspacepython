import torch
import numpy as np

# Tensor转NumPy
# 使用numpy()将Tensor转换成NumPy数组:
a = torch.ones(5)
b = a.numpy()
print(a, b)

a += 1
print(a, b)
b += 1
print(a, b)

# NumPy转Tensor
# 使用from_numpy()将NumPy数组转换成Tensor:
a = np.ones(5)
b = torch.from_numpy(a)
print(a, b)

a += 1
print(a, b)
b += 1
print(a, b)

# 直接用torch.tensor()将NumPy数组转换成Tensor，需要注意的是该方法总是会进行数据拷贝，返回的Tensor和原来的数据不再共享内存
c = torch.tensor(a)
a += 1
print(a, c)

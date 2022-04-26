import torch
from torch.autograd import Variable

input = torch.randn(32, 35, 256)

# 更改维度为[32, 256, 35]
input = input.permute(0, 2, 1)
input = Variable(input)
print(input.shape)
conv1 = torch.nn.Conv1d(in_channels=256, out_channels=100, kernel_size=2)

output = conv1(input)
print(output.size())

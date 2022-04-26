import torch
import torch.nn as nn

rnn = nn.LSTM(5, 6, 2, bidirectional=False)  # input_size = 5, hidden_size=6, num_layer=1
input = torch.randn(1, 3, 5)  # seq_len=1,batch_size=3, input_size=5

h0 = torch.randn(2, 3, 6)  # 初始化的隐层张量h
c0 = torch.randn(2, 3, 6)  # 初始化的细胞状态张量c

# output是最后一层lstm的每个向量对应隐藏层的输出,其与层数无关，只与序列长度相关
output, (hn, cn) = rnn(input, (h0, c0))
print("output is")
print(output)
print("hn is")
print(hn)
print("cn is")
print(cn)

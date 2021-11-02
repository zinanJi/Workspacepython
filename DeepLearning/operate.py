import torch

x = torch.ones(5, 3)
y = torch.rand(5, 3)
print(x + y)
print(torch.add(x, y))

#   指定输出
res = torch.empty(5, 3)
torch.add(x, y, out=res)
print(res)

#   inplace版本
#   PyTorch操作inplace版本都有后缀_, 例如x.copy_(y), x.t_()
#   add x to y
y.add_(x)
print(y)

# index
# 索引出来的结果与原数据共享内存，也即修改一个，另一个会跟着修改。
y = x[0, :]
y += 1
print(y)
print(x[0, :])

# 用view()改变Tensor形状,但是也是共享data的
# view仅仅是改变了对这个张量的观察角度，内部数据并未改变
x = torch.rand(5, 3)
y = x.view(15)
z = x.view(-1, 5)
print(y)
print(z)
print(x.size(), y.size(), z.size())

# reshape()可以改变形状，但是此函数并不能保证返回的是其拷贝
# 推荐先用clone创造一个副本然后再使用view
# 使用clone还有一个好处是会被记录在计算图中，即梯度回传到副本时也会传到源Tensor
x_cp = x.clone().view(15)
x -= 1
print(x)
print(x_cp)

# item(), 它可以将一个标量Tensor转换成一个Python number
x = torch.randn(1)
print(x)
print(x.item())

# broadcasting 广播机制：形状不同的Tensor做运算时，先适当复制元素使两个Tensor形状相同后再按元素运算
x = torch.arange(1, 3).view(1, 2)
print(x)
y = torch.arange(1, 4).view(3, 1)
print(y)
print(x + y)

# 内存开销：y = x + y 会开新内存
x = torch.tensor([1, 2])
y = torch.tensor([3, 4])
id_before = id(y)
y = y + x
print(id(y) == id_before)

# 索引替换，指定结果到原来的y的内存
x = torch.tensor([1, 2])
y = torch.tensor([3, 4])
id_before = id(y)
y[:] = y + x
print(id(y) == id_before)

# out参数、+=、add_也可以指定结果到原来的y的内存
torch.add(x, y, out=y)  # y += x, y.add_(x)
print(id(y) == id_before)  # True

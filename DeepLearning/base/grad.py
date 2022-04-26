from torch.autograd import Variable
import torch


# 对于梯度的解释：表示某一函数在该点处的方向导数沿着该方向取得最大值，即函数在该点处沿着该方向此变化最快，变化率最大。
# 微分其实可以认为是函数的变化率。
# 梯度实际上就是多变量微分的一般化。
# f(x,y,z)=3x+6y+9z, 梯度就是<3,6,9>

# 定义三个Variable变量
# Tensor张量默认不需要求导，可以通过 tensor.requires_grad 来检查一个张量是否需要求导。
x = Variable(torch.Tensor([1, 2, 3]), requires_grad=True)
w = Variable(torch.Tensor([2, 3, 4]), requires_grad=True)
b = Variable(torch.Tensor([3, 4, 5]), requires_grad=True)

# 构建计算图，一个一元二次方程
y = w * x * x + b

# 自动求导，计算梯度
# backward(variables, grad_variables=None, retain_graph=None, create_graph=False) 
# 先求和，再偏导 ysum = w1x1^2+b1 + w2x2^2+b2 + w3x3^2+b3
# grad_variables[1,1,1]作用可理解为在求梯度时的权重
y.backward(torch.Tensor([1, 1, 1]))

print(x.grad)
print(w.grad)
print(b.grad)

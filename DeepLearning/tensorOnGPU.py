import torch


# 用方法to()可以将Tensor在CPU和GPU（需要硬件支持）之间相互移动。
x = torch.tensor([1, 2])
if torch.cuda.is_available():
    device = torch.device("cuda")
    y = torch.ones_like(x, device=device)   # 直接创建一个在GPU上的Tensor
    x = x.to(device)    # 等价于 .to("cuda")
    z = x + y
    print(z)
    print(z.to("cpu", torch.double))  # to()还可以同时更改数据类型


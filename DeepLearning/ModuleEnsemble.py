from typing import Counter
import torch
import torchvision
import torchvision.transforms as transforms
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import matplotlib.pyplot as plt
import numpy as np

import os

os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

# 超参数
LR = 0.001
BATCH_SIZE = 100
EPOCH = 100

transform_train = transforms.Compose([
    transforms.RandomCrop(32, padding=4),
    transforms.RandomHorizontalFlip(),
    transforms.ToTensor(),
    transforms.Normalize((0.4914, 0.4822, 0.4465), (0.2023, 0.1994, 0.2010))
])

transform_test = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.4914, 0.4822, 0.4465), (0.2023, 0.1994, 0.2010))
])

trainset = torchvision.datasets.CIFAR10(root='./data',
                                        train=True,
                                        download=False,
                                        transform=transform_train)

trainloader = torch.utils.data.DataLoader(trainset,
                                          batch_size=128,
                                          shuffle=True,
                                          num_workers=2)

testset = torchvision.datasets.CIFAR10(root='./data',
                                       train=False,
                                       download=False,
                                       transform=transform_test)

testloader = torch.utils.data.DataLoader(testset,
                                         batch_size=100,
                                         shuffle=True,
                                         num_workers=2)

classes = ('plane', 'car', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse',
           'ship', 'truck')


class CNNNet(nn.Module):
    def __init__(self) -> None:
        super(CNNNet, self).__init__()
        self.conv1 = nn.Conv2d(in_channels=3,
                               out_channels=16,
                               kernel_size=5,
                               stride=1)
        self.pool1 = nn.MaxPool2d(kernel_size=2, stride=2)
        self.conv2 = nn.Conv2d(in_channels=16,
                               out_channels=36,
                               kernel_size=3,
                               stride=1)
        self.pool2 = nn.MaxPool2d(kernel_size=2, stride=2)
        self.fc1 = nn.Linear(1296, 128)
        self.fc2 = nn.Linear(128, 10)

    def forward(self, x):
        x = self.pool1(F.relu(self.conv1(x)))
        x = self.pool2(F.relu(self.conv2(x)))
        x = x.view(-1, 36 * 6 * 6)
        x = F.relu(self.fc2(F.relu(self.fc1(x))))
        return x


class Net(nn.Module):
    def __init__(self) -> None:
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(3, 16, 5)
        self.pool1 = nn.MaxPool2d(2, 2)
        self.conv2 = nn.Conv2d(16, 36, 5)
        self.pool2 = nn.MaxPool2d(2, 2)
        self.aap = nn.AdaptiveAvgPool2d(1)
        self.fc3 = nn.Linear(36, 10)

    def forward(self, x):
        x = self.pool1(F.relu(self.conv1(x)))
        x = self.pool2(F.relu(self.conv2(x)))
        x = self.aap(x)
        x = x.view(x.shape[0], -1)
        x = self.fc3(x)
        return x


class LeNet(nn.Module):
    def __init__(self) -> None:
        super(LeNet, self).__init__()
        self.conv1 = nn.Conv2d(3, 6, 5)
        self.conv2 = nn.Conv2d(6, 16, 5)
        self.fc1 = nn.Linear(16 * 5 * 5, 120)
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 10)

    def forward(self, x):
        out = F.relu(self.conv1(x))
        out = F.max_pool2d(out, 2)
        out = F.relu(self.conv2(out))
        out = F.max_pool2d(out, 2)
        out = out.view(out.size(0), -1)
        out = F.relu(self.fc1(out))
        out = F.relu(self.fc2(out))
        out = self.fc3(out)
        return out


if __name__ == '__main__':
    device = torch.device("cpu")
    net1, net2, net3 = CNNNet(), Net(), LeNet()

    mlps = [net1.to(device), net2.to(device), net3.to(device)]
    optimizer = optim.Adam([{
        "params": mlp.parameters()
    } for mlp in mlps],
                           lr=LR)
    loss_function = nn.CrossEntropyLoss()

    for ep in range(EPOCH):
        for img, label in trainloader:
            img, label = img.to(device), label.to(device)
            optimizer.zero_grad()
            for mlp in mlps:
                mlp.train()
                out = mlp(img)
                loss = loss_function(out, label)
                loss.backward()
            optimizer.step()

        pre = []
        vote_correct = 0
        mlps_correct = [0 for i in range(len(mlps))]
        for img, label in testloader:
            img, label = img.to(device), label.to(device)
            for i, mlp in enumerate(mlps):
                mlp.eval()
                out = mlp(img)
                _, prediction = torch.max(out, 1)
                pre_num = prediction.cpu().numpy()
                mlps_correct[i] += (pre_num == label.cpu().numpy()).sum()

                pre.append(pre_num)
            arr = np.array(pre)
            pre.clear()
            result = [
                Counter(arr[:, i]).most_common(1)[0][0]
                for i in range(BATCH_SIZE)
            ]
            vote_correct += (result == label.cpu().numpy()).sum()
        print("epoch:" + str(ep) + "集成模型的正确率" +
              str(vote_correct / len(testloader)))
        for idx, correct in enumerate(mlps_correct):
            print("模型" + str(idx) + "的正确率为：" + str(correct / len(testloader)))

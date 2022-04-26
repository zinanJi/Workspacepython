import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from MyDataLoader import MyData


class CAE_Encoder(nn.Module):
    def __init__(self, n_features) -> None:
        super(CAE_Encoder, self).__init__()
        self.conv1 = nn.Conv1d(in_channels=n_features,
                               out_channels=8,
                               kernel_size=1,
                               stride=1)
        # self.pool1 = nn.MaxPool1d(kernel_size=1, stride=1)
        self.conv2 = nn.Conv1d(in_channels=8,
                               out_channels=4,
                               kernel_size=1,
                               stride=1)
        # self.pool2 = nn.MaxPool1d(kernel_size=1, stride=1)

    def forward(self, x):
        x = self.conv1(x)
        print("conv1.size:")
        print(x.size())
        x = F.relu(x)
        # x = self.pool1(x)
        x = self.conv2(x)
        print("conv2.size:")
        print(x.size())
        x = F.relu(x)
        # x = self.pool2(x)
        # print(x)
        # 计算MMD
        # x = F.relu(self.fc2(F.relu(self.fc1(x))))
        return x


class CAE_Decoder(nn.Module):
    def __init__(self, n_features) -> None:
        super().__init__()
        self.dconv1 = nn.ConvTranspose1d(in_channels=4,
                                         out_channels=8,
                                         kernel_size=1,
                                         stride=1)
        self.unpool1 = nn.MaxUnpool1d(kernel_size=1, stride=1)
        self.dconv2 = nn.ConvTranspose1d(in_channels=8,
                                         out_channels=n_features,
                                         kernel_size=1,
                                         stride=1)
        self.unpool2 = nn.MaxUnpool1d(kernel_size=1, stride=1)

    def forward(self, x):
        x = self.dconv1(x)
        x = F.relu(x)
        # x = self.unpool1(x)
        x = self.dconv2(x)
        x = F.relu(x)
        # x = self.unpool2(x)
        return x

# 定义train和test


def train(encoder, decoder, device, trainloader,
          criterion, enc_optimizer, dec_optimizer, epoch):
    device = torch.device("cuda:0")
    for epoch in range(10):
        running_loss = 0.0
        for i, data in enumerate(trainloader, 0):
            # print(data)
            data = data.T
            # print(data)
            data = data.unsqueeze(1)
            # print(data)
            data = data.permute(2, 0, 1)
            # print(data)
            data = data.type(torch.FloatTensor)
            print(data.shape)
            inputs = data.to(device)
            
            enc_optimizer.zero_grad()
            dec_optimizer.zero_grad()
            z = encoder(inputs)
            # print(z)
            x_recon = decoder(z)
            # print(x_recon)
            loss = criterion(x_recon, inputs)
            loss.backward()
            enc_optimizer.step()
            dec_optimizer.step()

            running_loss += loss.item()
            if i % 690 == 689:
                print('[%d,%5d] loss: %.3f' %
                      (epoch + 1, i + 1, running_loss / 690))
                running_loss = 0.0

    print('Finished Training')
    torch.save(encoder.state_dict(), 'pytorch_cae_encoder.ckpt')
    torch.save(decoder.state_dict(), 'pytorch_cae_decoder.ckpt')


def test():
    print("test")


# 主函数读取数据，构建模型对象，调用train和test
if __name__ == '__main__':
    device = torch.device("cuda:0")
    encoder = CAE_Encoder(13).to(device)
    decoder = CAE_Decoder(13).to(device)

    criterion = nn.MSELoss()
    enc_optimizer = optim.SGD(encoder.parameters(), lr=0.001, momentum=0.9)
    dec_optimizer = optim.SGD(decoder.parameters(), lr=0.001, momentum=0.9)


    
    trainset = MyData('root', './Project(暂时废弃)/data9.csv')

    trainloader = torch.utils.data.DataLoader(trainset,
                                              batch_size=1,         # 一次几行数据
                                              shuffle=False,)

    testset = MyData('root', './Project(暂时废弃)/data8.csv')

    testloader = torch.utils.data.DataLoader(
        testset, batch_size=1, shuffle=False)

    num_epochs = 10

    for epoch in range(0, num_epochs):
        train(encoder, decoder, device, trainloader,
              criterion, enc_optimizer, dec_optimizer, epoch)
    test(encoder, decoder, device, testloader)

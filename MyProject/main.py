import torch
import MyData
import torch.nn as nn

# 参数声明
batch_size = 1
num_epochs = 10
csv_dir = './Project(暂时废弃)/data9.csv'

# 主函数读取数据，构建模型对象，循环训练
if __name__ == '__main__':
    # 构造Dataset对象
    trainset = MyData(csv_dir)
    # 创建一个dataloader对象
    trainloader = torch.utils.data.DataLoader(trainset,
                                              batch_size=1,         # 一次几行数据
                                              shuffle=False,)

    device = torch.device("cuda:0")

    # 创建模型对象
    encoder = Enc().to(device)
    decoder = Dec().to(device)
    lstm = lstm().to(device)

    # 定义损失函数为MSELoss
    criterion = nn.MSELoss()

    # 初始化模型参数的优化器
    enc_optimizer = torch.optim.SGD(
        encoder.parameters(), lr=0.001, momentum=0.9)
    dec_optimizer = torch.optim.SGD(
        decoder.parameters(), lr=0.001, momentum=0.9)
    lstm_optimizer = torch.optim.RMSprop(
        lstm.parameters(), lr=0.001, momentum=0.9)

    # 设置超参数epoch，模型对全部数据完成一次训练的过程为1个epoch
    num_epochs = 10

    # 模型训练阶段 todo：可抽象为函数
    # model.train,作用是启用batch normalization和drop out
    encoder.train()
    decoder.train()
    lstm.train()

    # 循环dataloader对象，将data拿到模型中去逐步迭代训练数据
    for epoch in range(0, num_epochs):
        z_next = 0
        for i, inputs in enumerate(trainloader):
            # 每一轮patch开始前设置zero_grad清除一次梯度
            enc_optimizer.zero_grad()
            dec_optimizer.zero_grad()

            inputs = inputs.to(device)

            # 通过输入得到编码模型的输出
            z = encoder(inputs)
            # todo：z需要作为LSTM模型的输入
            z_predict = lstm(z)
            # 通过z解码得到重建输出
            x_recon = decoder(z)

            # 计算损失 todo：需要加上lstm预测损失
            if i == 0:
                loss = criterion(x_recon, inputs)
            else:
                loss = criterion(x_recon, inputs) + \
                    criterion(z_next, z_predict)

            # 反向传播
            loss.backward()

            # 更新模型参数
            enc_optimizer.step()
            dec_optimizer.step()

            z_next = z

            # 每隔10个batch_sie输出一次loss
            # len(train_datasets) // batch_size的含义是表示有多少个batch_size
            # 上面循环中i的范围应该是从0到len(train_datasets) // batch_size-1
            if (i + 1) % 10 == 0:
                print('Epoch:[%d/%d],Step:[%d/%d],Loss:%.4f' % (epoch + 1,
                      num_epochs, i + 1, len(trainset) // batch_size, loss.item()))

        # 每次跑完一次epoch都保存一下模型
        torch.save(encoder.state_dict(), 'pytorch_cae_encoder.ckpt')
        torch.save(decoder.state_dict(), 'pytorch_cae_decoder.ckpt')
        torch.save(lstm.state_dict(), 'pytorch_lstm.ckpt')

    # 模型测试阶段 todo
    # model.eval()
    encoder.eval()
    decoder.eval()
    lstm.eval()

import torch
from MyData import MyDataSet
import torch.nn as nn
import Conv1DCAE
import lstm
import dataUtils
import numpy as np
import pandas
from prepare import prepare_data
from train import train_model

# 参数声明
BATCH_SIZE = 8
num_epochs = 10
csv_dir = './Project(暂时废弃)/data9.csv'
lr = 6e-4


# 主函数读取数据，构建模型对象，循环训练
def main():
    # 当数组元素比较多的时候，如果输出该数组，那么会出现省略号, 设置不显示省略号
    np.set_printoptions(suppress=True, threshold=np.inf)

    cspg_da, cspg_bm, cspg_cld, cspg_df = [pandas.DataFrame()] * 4
    # 处理数据，得到固定seq_len和n_features
    data, seq_len, n_features = prepare_data(cspg_da, cspg_bm, cspg_cld, cspg_df, False)

    # 构造Dataset对象
    train, val, test = MyDataSet(data, BATCH_SIZE, False)
    # 创建一个dataloader对象
    trainloader = torch.utils.data.DataLoader(train,
                                              batch_size=1,         # 一次几行数据
                                              shuffle=False,)

    device = torch.device("cuda:0")

    print(f'lr {lr}')

    # 创建模型对象
    model = Conv1DCAE(seq_len, n_features)

    model, history, encoder = train_model(model, train, test, n_epochs=1, lr=lr)


    # 定义损失函数为MSELoss
    criterion = nn.MSELoss()

    # 初始化模型参数的优化器
    enc_optimizer = torch.optim.SGD(
        encoder.parameters(), lr=0.001, momentum=0.9)
    dec_optimizer = torch.optim.SGD(
        decoder.parameters(), lr=0.001, momentum=0.9)
    lstm_optimizer = torch.optim.RMSprop(
        lstm.parameters(), lr=0.001, momentum=0.9)



    # 模型训练阶段 todo：可抽象为函数
    # model.train,作用是启用batch normalization和drop out
    






    # 循环dataloader对象，将data拿到模型中去逐步迭代训练数据
    for epoch in range(0, num_epochs):
        z_nextSeq = 0
        # 每次拿一个用户的数据
        for i, inputs in enumerate(trainloader):
            # 每一轮patch开始前设置zero_grad清除一次梯度
            enc_optimizer.zero_grad()
            dec_optimizer.zero_grad()

            inputs = inputs.to(device)

            # 通过输入得到编码模型的输出
            z = encoder(inputs)
            # todo：z需要作为LSTM模型的输入
            dataUtils.handleZ2supervised(z)
            z_predictSeq = lstm(z)
            # 通过z解码得到重建输出
            x_recon = decoder(z)

            # 计算损失 todo：需要加上lstm预测损失
            if i == 0:
                loss = criterion(x_recon, inputs)
            else:
                loss = criterion(x_recon, inputs) + \
                    criterion(z_nextSeq, z_predictSeq)

            # 反向传播
            loss.backward()

            # 更新模型参数
            enc_optimizer.step()
            dec_optimizer.step()

            z_nextSeq = dataUtils.getZFirstSeq(z)

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


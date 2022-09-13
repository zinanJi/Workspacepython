import torch.nn as nn
import torch.nn.functional as F


class Dec(nn.Module):
    def __init__(self, ) -> None:
        super().__init__()
        self.dconv1 = nn.ConvTranspose1d(in_channels=4,
                                         out_channels=8,
                                         kernel_size=1,
                                         stride=1)
        self.dconv2 = nn.ConvTranspose1d(in_channels=8,
                                         out_channels=16,
                                         kernel_size=1,
                                         stride=1)

    def forward(self, x):
        x = self.dconv1(x)
        x = F.relu(x)
        x = self.dconv2(x)
        x = F.relu(x)
        return x

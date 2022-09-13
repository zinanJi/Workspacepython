import torch.nn as nn
import torch.nn.functional as F


class Enc(nn.Module):
    def __init__(self, seq_len, n_features, z_dim=4):
        super(Enc, self).__init__()
        super(Enc, self).__init__()
        self.seq_len, self.n_features = seq_len, n_features
        self.conv1 = nn.Conv1d(in_channels=n_features,
                               out_channels=8,
                               kernel_size=1,
                               stride=1)
        self.pool = nn.MaxPool1d(kernel_size=1, stride=1)
        self.conv2 = nn.Conv1d(in_channels=8,
                               out_channels=4,
                               kernel_size=1,
                               stride=1)

    def forward(self, x):
        x = self.conv1(x)
        x = self.pool(x)
        x = F.relu(x)
        x = self.conv2(x)
        x = self.pool(x)
        x = F.relu(x)
        return x
        
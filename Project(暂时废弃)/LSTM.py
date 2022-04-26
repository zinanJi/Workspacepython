import torch.nn as nn


class LSTM(nn.Module):
    def __init__(self, input_channels, hidden_channels, kernel_size) -> None:
        super(LSTM, self).__init__()
        self.input_channels = input_channels
        self.hidden_channels = hidden_channels
        self.kernel_size = kernel_size
        self.num_layers = len(hidden_channels)

        
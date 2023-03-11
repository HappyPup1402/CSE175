#
# arch.py
#
# This script implements three Python classes for three different artificial
# neural network architectures: no hidden layer, one hidden layer, and two
# hidden layers. Note that this script requires the installation of the
# PyTorch (torch) Python package.
#
# This content is protected and may not be shared, uploaded, or distributed.
#
# PLACE ANY COMMENTS, INCLUDING ACKNOWLEDGMENTS, HERE.
# ALSO, PROVIDE ANSWERS TO THE FOLLOWING TWO QUESTIONS.
#

# Which network architecture achieves the lowest training set error?
# The lowest training set error is achieved by the model with two hidden layers with a value of 0.03308.

# Which network architecture tends to exhibit the best testing set accuracy?
# The best test set accuracy is achieved by the model with two hidden layers.

# Discussed logic with Mario Barrera
# Izaac Ramirez
# 12/13/2022
#

# PyTorch - Deep Learning Models
import torch.nn as nn
import torch.nn.functional as F


# Number of input features ...
input_size = 4
# Number of output classes ...
output_size = 3


class AnnLinear(nn.Module):
    """Class describing a linear artificial neural network, with no hidden
    layers, with inputs directly projecting to outputs."""

    def __init__(self):
        super().__init__()
        # PLACE NETWORK ARCHITECTURE CODE HERE
        self.my_layer = nn.Linear(in_features=input_size, out_features=output_size)

    def forward(self, x):
        # PLACE YOUR FORWARD PASS CODE HERE
        my_layer_net = self.my_layer(x)
        Result = my_layer_net
        return Result


class AnnOneHid(nn.Module):
    """Class describing an artificial neural network with one hidden layer,
    using the rectified linear (ReLU) activation function."""

    def __init__(self):
        super().__init__()
        # PLACE NETWORK ARCHITECTURE CODE HERE
        self.my_layerin = nn.Linear(in_features=input_size, out_features=20)
        self.hiddenLayer1 = nn.Linear(in_features=20, out_features=output_size)

    def forward(self, x):
        # PLACE YOUR FORWARD PASS CODE HERE
        x1 = self.my_layerin(x)
        x2 = F.relu(x1)
        Result = self.hiddenLayer1(x2)
        return Result


class AnnTwoHid(nn.Module):
    """Class describing an artificial neural network with two hidden layers,
    using the rectified linear (ReLU) activation function."""

    def __init__(self):
        super().__init__()
        # PLACE NETWORK ARCHITECTURE CODE HERE
        self.my_layerin = nn.Linear(in_features=input_size, out_features=16)
        self.hiddenLayer1 = nn.Linear(in_features=16, out_features=12)
        self.hiddenLayer2 = nn.Linear(in_features=12, out_features=output_size)

    def forward(self, x):
        # PLACE YOUR FORWARD PASS CODE HERE
        x1 = self.my_layerin(x)
        x2 = F.relu(x1)
        x3 = self.hiddenLayer1(x2)
        x4 = F.relu(x3)
        Result = self.hiddenLayer2(x4)
        return Result

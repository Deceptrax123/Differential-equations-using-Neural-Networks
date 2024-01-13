import torch 
from torch import nn 


def init_weights(model):
    for module in model.modules():
        if isinstance(module,(nn.Linear)):
            if module.bias.data is not None:
                module.bias.data.zero_()
            else:
                nn.init.kaiming_normal_(module.weight.data,mode='fan_in')
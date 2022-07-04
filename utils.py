import torch
import matplotlib.pyplot as plt
from torchvision.utils import make_grid


def plot_kernels(weights, save=None):
    kernels = abs(weights)
    kernels = kernels - kernels.min()
    kernels = kernels/kernels.max()
    
    plt.figure(figsize=(10,10))
    img = make_grid(kernels, nrow=8, padding=1, pad_value=1)
    plt.axis('off')
    plt.imshow(img.detach().permute(1,2,0).cpu())


def get_activation(activation, name):
    def hook(model, input, output):
        activation[name] = output
    return hook
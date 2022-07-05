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

def count_parameters(model):
    num_params = sum(p.numel() for p in model.parameters())
    print(f'Total parameters : {num_params:,}' )

def print_sparsity(model):
    for k,m in enumerate(model.modules()):
        if isinstance(m, nn.Conv2d):
            print(f"Sparsity in {m.__class__.__name__} {k}: {100. * float(torch.sum(m.weight == 0))/ float(m.weight.nelement()):.2f}%")
from __future__ import print_function
import torch

x = torch.randn(4, 4)

# 当 CUDA 可用的时候，可以使用下方这段代码，采用 torch.device() 方法来改变 tensors 是否在 GPU 上进行计算操作
if torch.cuda.is_available():
    device = torch.device("cuda")          # 定义一个 CUDA 设备对象
    y = torch.ones_like(x, device=device)  # 创建一个在 GPU 上的 tensor
    x = x.to(device)                       # 将 x 移动到 GPU
    z = x + y
    print(z)
    print(z.to("cpu", torch.double))       # 将 z 移动到 CPU 并改变数值类型
else:
    print("CUDA is not available")
from __future__ import print_function
import torch
x = torch.randn(3, 6)
y = x.view(18)
# -1 表示除给定维度外的其余维度的乘积
z = x.view(-1, 9)
print(x.size(), y.size(), z.size())
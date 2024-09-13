from __future__ import print_function
import torch
tensor1 = torch.zeros(3, 4, dtype=torch.long)
tensor2 = torch.randn_like(tensor1, dtype=torch.float)
print('tensor1: ', tensor1)
print('tensor2: ', tensor2)
from __future__ import print_function
import torch

tensor1= torch.randn(3, 4)
tensor2 = torch.rand(3, 4)
print('tensor1= ', tensor1)
print('tensor2= ', tensor2)
print('tensor1 + tensor2= ', tensor1 + tensor2)
print('tensor1 + tensor2= ', torch.add(tensor1, tensor2))
# 新声明一个 tensor 变量保存加法操作的结果
result = torch.empty(3, 4)
torch.add(tensor1, tensor2, out=result)
print('add result= ', result)
# 直接修改变量
tensor1.add_(tensor2)
print('tensor1= ', tensor1)
print('tensor2= ', tensor2)
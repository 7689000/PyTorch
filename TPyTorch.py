import torch
import torchvision
import numpy as np

x = [12,23,34,45,56,67,78]
print(torch.is_tensor(x))
print(torch.is_storage(x))

y = torch.randn(1,2,3,4,5)
print(torch.is_tensor(y))
print(torch.is_storage(y))
print(torch.numel(y)) # the total number of elements in the input Tensor

print(torch.zeros(4,4))
print(torch.numel(torch.zeros(4,4)))

print(torch.eye(3,4))
print(torch.eye(5,4))

x1 = np.array(x)
print(x1)
print(torch.from_numpy(x1))
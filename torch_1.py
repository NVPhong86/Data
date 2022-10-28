# -*- coding: utf-8 -*-
"""torch_1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gcaBknsI9qcWL5Yq3O7eQq0RcN9eQUa9
"""

import torch
import numpy as np

torch.random.seed()
x = torch.empty(5,3)
x = torch.rand(5,3)
x

x = torch.zeros(5,3,dtype = torch.long) # define dtype of number (calculus for matrix or more func, no exist error)
x

x = torch.Tensor(5,3)
x = torch.Tensor([5.5,3.3])
x

x = torch.ones(5,3)
x
y  = torch.rand_like(x,dtype = torch.double)
z = torch.add(x,y)
# y = y+x

a =  torch.rand(4,4)
b =  torch.rand(4,4)

# c = a + b
# c = torch.add(a,b)
c = torch.empty(4,4)
torch.add(a,b,out = c)

# index cu phap giong nhu numpy
a[:,1]

# chuyen matran 4,4 thanh 1 hang va 16 cot
b.view(16)
b.view(-1,8) # b.view(2,8)

# random 1 giatri
x  = torch.randn(1)
# lay ra gia tri cua 1 so
x.item()

y = torch.rand(3,3)
c = y.numpy()

# random 1 giatri
x  = torch.randn(1)
# lay ra gia tri cua 1 so trong torch
x.item()

y = torch.rand(3,3)
y
# chuyen ve numpy roi slice theo position ( nhanh hon )
c = y.numpy()
c 
c[0,0]

# chuyen tu numpy ve tensor

import numpy as np
a = np.ones(3)
a
b  = torch.from_numpy(a)
b

# kiem tra phep toan co chay tren GPU hay khong
device = torch.cuda.is_available()
device
if  torch.cuda.is_available() :
  device = torch.device('cuda')
  y = torch.ones_like(x,device = device) 
  x = x.to(device)
  z = x+y
  print(z)

# chuyen ve tinh toan tren CPU
x.cpu()

"""#Lecture 2"""

# Trong torch.Tensor
# requires_grad : khai bao tensor co luu tru thong tin ve grandiant
#grad : ket qua tao xuong ( lưu các giá trị của đạo hàm )
#grad_fn : luu cac ket qua xuong cac ham nhu sum devide...
# backward() : tim nguoc, backup lai ( hàm đạo hàm )

import torch
x = torch.tensor (2.0,requires_grad = True)
x
y = torch.exp(x)
y 
y.backward()
x.grad

from torch.autograd import grad
torch.Tensor
- requires_grad
grad_fn 
grad
backwardbackward

"""# Xây dựng Model bằng nn.Module """

import torch
import torch.nn as nn # network
import torch.nn.functional as F

class Net(nn.Module) : # expand tu thu vien
  def__init__( self ) :
    super(Net, self).__init__() # goi ham init tu class me 
    self.conv1 = nn.Conv2d(1,6,3) # (input_ch, output_ch, stride)
    self.conv2 = nn.Conv2d(6,16,3) # convelution 1, 2d is dimension (x,y)
    self.fc1 = nn.Linear(16*6*6,120)
    self.fc2 = nn.Linear(120,84) # 1 layers
    self.fc3 = nn.Linear(84,10)
  
# kernel = w*h ( width*height)
# 1,2, pixels
# 3,4
# relu : tra ve x neu x > 0
# tra ve 0 neu x < 0

  def forward(self, x) : # khi dua 1 thong tin gi vao, thi se qua ham forward
    x = self.conv1(x) #
    x = F.relu(x)
    x = F.max_pool2d(x, (2,2)) # max_pooling, kernel(2,2), lay ra gia tri max
    
    x = self.conv2(x)
    x = F.relu(x)
    x = F.max_pool2(x, 2)

    x = x.view(-1,self.num_flat_features(x))
    
    x = F.relu(self.fc1(x))
    x = F.relu(self.fc2(x))
    x = F.relu(self.fc3(x))
    
    
    
    return x
    
    def num_flat_features(self,x) :
      size = x.size()[1:]
      num_features = 1
      for s in size :
        num_features *= s
      return num_features

net  =  Net()
print(net)

input_image = torch.rand(1,1,32,32)
output = net(input_image)
print(output)
output.size
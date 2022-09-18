import numpy as np 
import torch
import torch.nn as nn
import torch.nn.functional as F
import torchvision
import torchvision.transforms as transforms
from PIL import Image
import matplotlib.pyplot as plt 
import os 
from dslBezier import DslBezier, Length, Radius, Direction, Orient

class Net(nn.Module):
    def __init__(self):
        super().__init__()        
        self.conv1 = nn.Conv2d(1, 32, 5)
        self.pool = nn.MaxPool2d(2, 2)
        self.conv2 = nn.Conv2d(32, 96, 4)                
        self.fc1 = nn.Linear(384, 96)
        self.fc2 = nn.Linear(96, 32)        
        self.fc3 = nn.Linear(32, 10)        
        self.sm = nn.Softmax(dim = 1)

    def forward(self, x):
        x = self.pool(x)        
        x = F.relu(self.conv1(x))
        x = self.pool(x)
        x = F.relu(self.conv2(x))        
        x = torch.flatten(x, 1) 
        x = F.relu(self.fc1(x))        
        x = F.relu(self.fc2(x))        
        x = self.fc3(x)
        x = self.sm(x)
        return x

model = Net()
model.load_state_dict(torch.load('./model_6'))
model.eval()

transform=torchvision.transforms.Compose([
                               torchvision.transforms.ToTensor(),
                               torchvision.transforms.Normalize(
                                 (0.1307,), (0.3081,))
                             ])


d = DslBezier() 

for i in range(1000000) :     
    d._reset()
    feat = np.random.rand(5*9)
    d._simulate(feat)

    im = d.canvas.astype(np.float32)

    img = transform(im)
    img = torch.unsqueeze(img, 0)

    result = model(img)
    
    res = result.detach().numpy()[0]
    res += -np.min(res)
    norm = res/np.sum(res)
    
    maxInd = np.argmax(norm)

    '''
    lines = d._convert(feat)
    for line in lines : 
        print(line)
    d.visualize()
    '''


    if norm[maxInd] > 0.98 :

        name = f'{maxInd}_{norm[maxInd]:0.3f}'
        d._save(name)
        lines = d._convert(feat)
        d._saveProgram(lines, name)

    
import cv2
import numpy as np
import torch.utils.data
import torchvision

# download MNIST dataset
train_data = torchvision.datasets.MNIST(
    root='./datasets',
    download=True,
    transform=torchvision.transforms.ToTensor()
)

# use data loader
dataloader = torch.utils.data.DataLoader(
    dataset=train_data,
    batch_size=10,
    # shuffle=True
)


# model definition
class MyModel(torch.nn.Module):
    def __init__(self):
        super(MyModel, self).__init__()

    def forward(self, x):

        return x


if __name__ == '__main__':
    images, labels = next(iter(dataloader))
    img = torchvision.utils.make_grid(images)
    img = np.array(img).transpose(1, 2, 0)
    cv2.imshow('img', img)
    cv2.waitKey(0)
    # print(train_data.targets)

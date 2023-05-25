import numpy.random
import torch


def differential():
    x = torch.arange(3.0, requires_grad=True)
    y = x
    y.backward()
    print(x.grad)


def normal_distribution():
    print(numpy.random.normal(size=5))


if __name__ == '__main__':
    differential()


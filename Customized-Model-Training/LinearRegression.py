import torch
from DataGenarator import point_data_generate
from matplotlib import pyplot as plt


# data prepared, do use tensors in the calculations!
x_list, y_list = point_data_generate(num=50, r=100)
x_train = torch.tensor(x_list).unsqueeze(1) / 200
y_train = torch.tensor(y_list).unsqueeze(1) / 200


class LinearRegression(torch.nn.Module):
    def __init__(self):
        super(LinearRegression, self).__init__()
        self.linear = torch.nn.Linear(1, 1)

    def forward(self, x):
        return self.linear(x)


if __name__ == '__main__':
    # build model
    model = LinearRegression()
    criterion = torch.nn.MSELoss()
    opt = torch.optim.SGD(model.parameters(), lr=0.01)

    for _ in range(1, 101):
        y_pred = model(x_train)
        loss = criterion(y_pred, y_train)
        opt.zero_grad()
        loss.backward()
        opt.step()
        print("epochs: {}, loss: {}".format(_, loss.data))

    # save model
    torch.save(model.state_dict(), './models/linear_regression.pth')

    # predication test
    pr = model(torch.Tensor([[0.1], [0.8]])).data
    plt.scatter([num / 200 for num in x_list], [num / 200 for num in y_list])
    plt.plot([0.1, 0.8], pr)
    plt.show()




import torch 
from nturgbd2coco import read_formated_data

# ------------------------------- Define model -------------------------------+

class ActionPredictor(torch.nn.Module):
    def __init__(self, n_dim_input=17 * 2, n_dim_output=5, n_dim_hidden=25, batch_size=1):
        super(ActionPredictor, self).__init__()
        self.n_dim_input = n_dim_input
        self.n_dim_output = n_dim_output
        self.n_dim_hidden = n_dim_hidden
        self.batch_size = batch_size
        self.lstm = torch.nn.LSTM(n_dim_input, n_dim_hidden)
        self.linear = torch.nn.Linear(n_dim_hidden, n_dim_output)
        self.hidden_cell = None
        self.reset_hidden_state()
        
    def forward(self, x):
        out, self.hidden_cell = self.lstm(
            x.view(len(x), self.batch_size, self.n_dim_input), 
            self.hidden_cell
        ) 
        out = self.linear(out)[-1]
        return torch.nn.functional.softmax(out, dim=-1)
        
    def reset_hidden_state(self):    
        self.hidden_cell = (
            torch.zeros(1, self.batch_size, self.n_dim_hidden),
            torch.zeros(1, self.batch_size, self.n_dim_hidden)
        )  

# +------------------------------- Training ----------------------------------+

def train(dataset, labels, epochs=1000, learning_rate=0.001):
    inputs = torch.tensor(dataset, dtype=torch.float)
    labels = torch.tensor(labels, dtype=torch.long)  
    model = ActionPredictor()
    criterion = torch.nn.CrossEntropyLoss()  
    optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)
    
    for e in range(epochs):
        model.reset_hidden_state()
        pred = model(inputs)
        loss = criterion(pred, labels)  
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        print(f'Epoch {e+1}, Loss: {loss.item()}')
    
    torch.save(model.state_dict(), 'actionPredictor.pth')


# +-------------------------------- Prediction --------------------------------+

def predict(input_data):
    model = ActionPredictor()
    model.load_state_dict(torch.load("actionPredictor.pth"))
    print(model(input_data))
    return None


if __name__ == '__main__':
    length, data = read_formated_data("kpdata\S001C001P001R001A005.skeleton(coco)") 
    labels = [5 for i in range(length)]   
    print(data.shape)
    train(data, labels)
    

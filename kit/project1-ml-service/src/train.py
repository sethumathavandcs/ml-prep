"""Minimal training loop on synthetic data. Replace with a real dataset in month 4."""
import torch, torch.nn as nn

def make_data(n=2000, seed=0):
    g = torch.Generator().manual_seed(seed)
    x = torch.randn(n, 4, generator=g)
    y = (x[:, 0] + 0.5 * x[:, 1] > 0).long()
    return x, y

def train(epochs=20, path="model.pt"):
    x, y = make_data()
    model = nn.Sequential(nn.Linear(4, 16), nn.ReLU(), nn.Linear(16, 2))
    opt = torch.optim.Adam(model.parameters(), lr=1e-2)
    loss_fn = nn.CrossEntropyLoss()
    for _ in range(epochs):
        opt.zero_grad()
        loss = loss_fn(model(x), y)
        loss.backward()
        opt.step()
    acc = (model(x).argmax(1) == y).float().mean().item()
    torch.save(model.state_dict(), path)
    return acc

if __name__ == "__main__":
    print("train accuracy:", train())

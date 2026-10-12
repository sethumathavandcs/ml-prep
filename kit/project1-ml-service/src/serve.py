import os, torch, torch.nn as nn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
model = nn.Sequential(nn.Linear(4, 16), nn.ReLU(), nn.Linear(16, 2))
if os.path.exists("model.pt"):
    model.load_state_dict(torch.load("model.pt"))
model.eval()

class Req(BaseModel):
    features: list[float]

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict")
def predict(r: Req):
    with torch.no_grad():
        p = model(torch.tensor([r.features])).softmax(1)[0].tolist()
    return {"probs": p}

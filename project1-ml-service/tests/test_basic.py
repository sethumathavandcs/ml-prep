from fastapi.testclient import TestClient
from src.serve import app
from src.train import train

def test_train_learns():
    assert train(path="/tmp/m.pt") > 0.8

def test_health():
    assert TestClient(app).get("/health").json() == {"status": "ok"}

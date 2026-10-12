setup:
	python -m venv .venv && . .venv/bin/activate && pip install -r requirements.txt
train:
	python -m src.train
serve:
	uvicorn src.serve:app --reload
test:
	pytest -q

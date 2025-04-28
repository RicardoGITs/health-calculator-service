.PHONY: init run test build clean

init:
	pip install --upgrade pip && pip install -r requirements.txt

run:
	python app.py

# Ensure project root is on PYTHONPATH so pytest can import local modules
test:
	PYTHONPATH=$(PWD) pytest --maxfail=1 --disable-warnings -q

build:
	docker build -t health-calculator-service .

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +

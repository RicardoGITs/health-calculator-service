# Health Calculator Microservice

A Python-based Flask microservice that calculates health metrics (BMI and BMR) via REST API, provides a simple web UI, is containerized with Docker, orchestrated with Makefile, and deployed to Azure App Service via GitHub Actions CI/CD.

---

## Table of Contents

1. [Features](#features)  
2. [Directory Structure](#directory-structure)  
3. [Prerequisites](#prerequisites)  
4. [Local Setup](#local-setup)  
5. [Running Locally](#running-locally)  
6. [Docker](#docker)  
7. [Makefile Tasks](#makefile-tasks)  
8. [Testing](#testing)  
9. [Web UI](#web-ui)  
10. [CI/CD Pipeline](#cicd-pipeline)  
11. [Azure Deployment](#azure-deployment)

---

## Features

- **REST API** endpoints  
  - `POST /bmi` — compute Body Mass Index  
  - `POST /bmr` — compute Basal Metabolic Rate (Harris–Benedict)  
- **Web UI** — interactive calculator for BMI & BMR  
- **Containerized** — Dockerfile for easy image build  
- **Makefile** — automation for setup, run, test, build, clean  
- **Unit tests** — `pytest` for utils & endpoints  
- **CI/CD** — GitHub Actions to test, build, and deploy  
- **Azure App Service** — hosted on Linux container plan  

---

## Directory Structure

```
health-calculator-service/
├── .gitignore
├── README.md
├── app.py
├── health_utils.py
├── requirements.txt
├── Dockerfile
├── Makefile
├── templates/
│   └── index.html
├── tests/
│   └── test_health_utils.py
└── .github/
    └── workflows/
        └── ci-cd.yml
```

---

## Prerequisites

- **Git** ≥ 2.x  
- **Python** ≥ 3.9  
- **virtualenv** or **python3-venv**  
- **Docker** (for container builds)  
- **Azure CLI** (for manual CLI deployment)  
- **GitHub** account & repository  

---

## Local Setup

1. **Clone the repo**  
   ```bash
   git clone git@github.com:RicardoGITs/health-calculator-service.git
   cd health-calculator-service
   ```

2. **Create & activate a virtualenv**  
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**  
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

---

## Running Locally

- **Start the Flask app**  
  ```bash
  make run
  # or
  python app.py
  ```
  The service listens on `http://0.0.0.0:5000`.

- **Hit the endpoints**  
  ```bash
  curl -X POST http://localhost:5000/bmi        -H "Content-Type: application/json"        -d '{"height":1.75,"weight":70}'

  curl -X POST http://localhost:5000/bmr        -H "Content-Type: application/json"        -d '{"height":175,"weight":70,"age":30,"gender":"male"}'
  ```

---

## Docker

1. **Build the image**  
   ```bash
   make build
   # or
   docker build -t health-calculator-service .
   ```

2. **Run the container**  
   ```bash
   docker run -p 5000:5000 health-calculator-service
   ```
3. **Test** at `http://localhost:5000`.

---

## Makefile Tasks

| Target       | Description                                                  |
| ------------ | ------------------------------------------------------------ |
| `make init`  | Install/update Python dependencies (`pip install -r`)        |
| `make run`   | Run Flask service (`python app.py`)                          |
| `make test`  | Run tests with `pytest` (sets `PYTHONPATH`)                  |
| `make build` | Build Docker image                                          |
| `make clean` | Remove `__pycache__` directories                             |

---

## Testing

```bash
make test
```

All unit tests for utility functions and API endpoints should pass.

---

## Web UI

Visit the home page at `https://ricardo-health-calculator.azurewebsites.net/` to access a simple interface:

- Enter **height** & **weight** for BMI  
- Enter **height**, **weight**, **age**, **gender** for BMR  
- Click **Calculate** to see results instantly  

---

## CI/CD Pipeline

GitHub Actions workflow (`.github/workflows/ci-cd.yml`) runs on every push to `main`:

1. **Checkout** code  
2. **Set up Python** (3.9)  
3. **Install dependencies**  
4. **Run tests** (`make test`)  
5. **Build Docker image**  
6. **Deploy to Azure Web App** via `azure/webapps-deploy@v2` using your Publish Profile secret

---

## Azure Deployment

1. **Register** `Microsoft.Web` if needed  
2. **Create** Resource Group  
   ```bash
   az group create --name health-rg --location westeurope
   ```
3. **Create** App Service Plan (Linux, Basic B1)  
   ```bash
   az appservice plan create      --name health-plan      --resource-group health-rg      --is-linux      --sku B1
   ```
4. **Create** Web App  
   ```bash
   az webapp create      --resource-group health-rg      --plan health-plan      --name ricardo-health-calculator      --runtime "PYTHON|3.9"
   ```
5. **Export** publish profile (XML!)  
   ```bash
   az webapp deployment list-publishing-profiles      --resource-group health-rg      --name ricardo-health-calculator      --xml > publish-profile.xml
   ```
6. **Add** `AZURE_WEBAPP_PUBLISH_PROFILE` secret in GitHub (copy XML contents)  
7. **Push** to `main` to trigger CI/CD and deploy  

---


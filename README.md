# Cloud Lab 1 — REST API Deployment

## Description

A REST API built with FastAPI and PostgreSQL.
The application is containerized with Docker and can be started locally
using Docker Compose.

## Technologies

- Python 3.12
- FastAPI
- Uvicorn
- PostgreSQL 16
- Docker
- Docker Compose
- Terraform (cloud infrastructure)
- GitHub Actions (CI/CD)

## Project Structure

```text
cloud-lab1/
├── .github/
│   └── workflows/
├── app/
│   ├── __init__.py
│   └── main.py
├── terraform/
├── .gitignore
├── compose.yaml
├── Dockerfile
├── README.md
└── requirements.txt
```

## Run Locally

Requirements: Docker Desktop and Docker Compose.

Build and start the application:

```powershell
docker compose up --build -d
```

Check the containers:

```powershell
docker compose ps
```

Stop the containers:

```powershell
docker compose down
```

PostgreSQL data is stored in a named Docker volume and is preserved
when containers are removed with `docker compose down`.
Do not use `docker compose down -v` if you want to keep the data.

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | API welcome message |
| GET | `/health` | Health check |
| GET | `/items` | List stored items |
| POST | `/items` | Create an item |
| GET | `/docs` | Interactive Swagger documentation |

## Example Request

Create an item using `POST /items`:

```json
{
  "name": "My first cloud item"
}
```

Example response:

```json
{
  "id": 1,
  "name": "My first cloud item"
}
```

## Local URLs

- API: http://localhost:8080
- Health check: http://localhost:8080/health
- Swagger UI: http://localhost:8080/docs

## Cloud Deployment

Cloud infrastructure and CI/CD configuration will be documented here
after they have been implemented and tested.

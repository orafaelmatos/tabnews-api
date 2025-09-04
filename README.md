# TabNews API Backend

This project is a **FastAPI backend service** designed to interact with the [TabNews API](https://www.tabnews.com.br).  
It allows users to **search for posts**, **filter by title, tags, or author**, and retrieve structured results in JSON format.

---

## Features

- Search TabNews posts by title.
- Filter posts by tags or author.
- Limit the number of results returned.
- Async HTTP requests using `httpx`.
- Docker-ready for isolated testing or deployment.

---

## Project Structure

```
tabnews-api/
│
├── app/
│ ├── main.py
│ ├── models.py
│ └── services.py
│
├── requirements.txt
└── Dockerfile
```

---

## Requirements

- Python 3.11+
- Docker (optional, for containerized deployment)
- Internet connection to access TabNews API

---

## Installation

```bash
git clone https://github.com/orafaelmatos/tabnews-api.git
cd tabnews-api
```

### Docker Setup

1 - Build the Docker image:

```bash
docker build -t tabnews-api .
```

2 - Run the container:

```bash
docker run -d -p 8000:8000 tabnews-api
```

### Local Setup

1 - Install dependencies:

```bash
pip install -r requirements.txt
```

2 - Run the app locally:

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

The API will be available at: http://localhost:8000

---

## API Endpoints

- `GET /` – Returns a welcome message
- `GET /posts/search` – Search Posts 
    - Example GET /posts/search?title=PITCH&limit=5 
    - Response:
        ```
        [
        {
        "id": "8460aa3b-fa09-48ac-a429-27f7996d8b70",
        "title": "[PITCH] - Criei um streaming de músicas grátis e sem anúncios",
        "user": "user_creator",
        "tags": ["musica", "tech"]
        }
        ]

        ```
---


## Notes
- The TabNews API has a rate limit. Avoid sending too many requests in a short period to prevent 429 Too Many Requests errors.
- For testing multiple requests, consider using caching or a VPN/cloud server to avoid hitting limits
- The project is fully async, using httpx and FastAPI, making it suitable for scalable applications.

---
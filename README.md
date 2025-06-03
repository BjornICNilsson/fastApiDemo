# fastApiDemo

Simple FastAPI demo providing mock weather data.

## Setup

Install dependencies:

```bash
pip install -r requirements.txt
```

## Running

Start the server with Uvicorn:

```bash
uvicorn app.main:app --reload
```

The API exposes:

- `GET /health` - health check
- `GET /weather/{city}` - weather data for a city

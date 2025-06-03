import logging
from fastapi import FastAPI, HTTPException
from .models import WeatherData

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

app = FastAPI(title="Weather API")

# mock weather data
MOCK_WEATHER = {
    "London": WeatherData(city="London", temperature=15.0, condition="Cloudy"),
    "New York": WeatherData(city="New York", temperature=20.0, condition="Sunny"),
}

@app.get("/health")
async def health() -> dict:
    """Health check endpoint."""
    logger.info("Health check")
    return {"status": "ok"}

@app.get("/weather/{city}", response_model=WeatherData)
async def get_weather(city: str) -> WeatherData:
    """Return weather data for a given city."""
    logger.info("Weather request for %s", city)
    try:
        data = MOCK_WEATHER[city]
    except KeyError as exc:
        logger.error("Weather data not found for %s", city)
        raise HTTPException(status_code=404, detail="City not found") from exc
    return data

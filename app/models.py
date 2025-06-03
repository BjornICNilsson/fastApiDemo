from pydantic import BaseModel

class WeatherData(BaseModel):
    city: str
    temperature: float
    condition: str

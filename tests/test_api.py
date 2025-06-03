import sys
from pathlib import Path

from fastapi.testclient import TestClient
import pytest

# Ensure app can be imported when tests run directly
sys.path.append(str(Path(__file__).resolve().parents[1]))

from app.main import app

client = TestClient(app)

def test_health():
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json() == {'status': 'ok'}

def test_weather_london():
    response = client.get('/weather/London')
    assert response.status_code == 200
    data = response.json()
    assert data['city'] == 'London'
    assert data['condition'] == 'Cloudy'
    assert data['temperature'] == pytest.approx(15.0, abs=0.5)

def test_weather_not_found():
    response = client.get('/weather/Paris')
    assert response.status_code == 404
    assert response.json() == {'detail': 'City not found'}

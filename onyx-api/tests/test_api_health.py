"""
ONYX CTI — Backend API Health & Contract Tests
"""

import pytest
from fastapi.testclient import TestClient
from onyx_api.routers.health import router as health_router
from fastapi import FastAPI

@pytest.fixture
def test_app():
    app = FastAPI(title="ONYX Health Test App")
    app.include_router(health_router, prefix="/api/v1")
    return app

@pytest.fixture
def client(test_app):
    return TestClient(test_app)

def test_liveness_endpoint(client):
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"
    assert data["service"] == "onyx-api"
    assert data["version"] == "3.0.0"
    assert "timestamp" in data

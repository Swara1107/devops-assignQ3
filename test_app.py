from app import app


def test_home():
    client = app.test_client()
    response = client.get("/")

    assert response.status_code == 200
    data = response.get_json()
    assert data["application"] == "DevOps Demo App"
    assert data["status"] == "running"


def test_health():
    client = app.test_client()
    response = client.get("/health")

    assert response.status_code == 200
    assert response.get_json()["status"] == "healthy"


def test_metrics():
    client = app.test_client()
    response = client.get("/metrics")

    assert response.status_code == 200
    assert b"app_info" in response.data

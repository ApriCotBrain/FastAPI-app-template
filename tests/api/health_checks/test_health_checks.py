from fastapi import status


async def test_ping_200(test_client):
    response = await test_client.get("/health/ping")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == "pong"


async def test_ready_200(test_client):
    response = await test_client.get("/health/ready")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == "ready"

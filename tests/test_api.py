def test_health(client):
    assert client.get("/health").status_code == 404
    assert client.get("/health?type=liveness").status_code == 200

def test_request_base(client):
    response = client.get("/")
    assert "hello world from DevContainer" in response.text
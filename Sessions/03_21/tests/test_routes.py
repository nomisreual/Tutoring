def test_hello(client):
    response = client.get("/")
    assert "Hello!" == response.data

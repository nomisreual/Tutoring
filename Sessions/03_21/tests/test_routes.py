def test_hello(client):
    response = client.get("/")
    assert b"Hello!" == response.data

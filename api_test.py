import requests
def test_api():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    s = response.status_code
    assert s == 200
    data = response.json()
    assert data["id"] == 1
    assert data["userId"]==1
    assert data["title"]
    assert data["body"]
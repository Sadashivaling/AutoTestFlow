import requests
def test_negative():
    response=requests.get("https://jsonplaceholder.typicode.com/posts/99999",timeout=10)
    assert response.status_code==404
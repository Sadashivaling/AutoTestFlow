import requests
def test_api():
    data={"userId":1,"id":1,"title":"automation","body":"test"}
    response=requests.post("https://jsonplaceholder.typicode.com/posts",json=data)
    assert response.status_code==201
    result=response.json()
    assert result["title"]==data["title"]
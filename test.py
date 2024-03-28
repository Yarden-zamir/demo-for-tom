from requests import get

response = get("http://localhost:8000/")
assert response.status_code == 200
assert "Hello World" in response.text

response = get("http://localhost:8000/bye")
assert response.status_code == 200
assert "Goodbye World" in response.text

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_fib_NR001():
    response = client.get("/fib?n=1")
    assert response.status_code == 200
    assert response.json() == {"result": 1}

def test_get_fib_NR002():
    response = client.get("/fib?n=2")
    assert response.status_code == 200
    assert response.json() == {"result": 1}

def test_get_fib_NR003():
    response = client.get("/fib?n=10")
    assert response.status_code == 200
    assert response.json() == {"result": 55}

def test_get_fib_ABR001():
    response = client.get("/fib")
    assert response.status_code == 400
    assert response.json() == {"detail": "クエリパラメータnが必要です"}

def test_get_fib_ABR002():
    response = client.get("/fib?n=abc")
    assert response.status_code == 422
    assert response.json() == {"detail": [{"loc":["query","n"],"msg":"value is not a valid integer","type":"type_error.integer"}]}

def test_get_fib_ABR003():
    response = client.get("/fib?n=0")
    assert response.status_code == 400
    assert response.json() == {"detail": "nは1以上である必要があります"}

def test_get_fib_ABR004():
    response = client.post("/fib?n=1")
    assert response.status_code == 405
    assert response.json() == {"detail": "Method Not Allowed"}


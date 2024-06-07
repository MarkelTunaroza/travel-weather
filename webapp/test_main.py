from main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200


def test_countries():
    response = client.get("/countries")
    assert response.status_code == 200
    assert sorted(response.json()) == ["England", "France", "Germany", "Italy", "Peru", "Portugal", "Spain"]from main import app
def test_countries():
    response = client.get("/countries")
    assert response.status_code == 200
    assert sorted(response.json()) == ["England", "France", "Germany", "Italy", "Peru", "Portugal", "Spain"]from fastapi.testclient import TestClient

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200

def test_countries():
    response = client.get("/countries")
    assert response.status_code == 200
    assert sorted(response.json()) == ["England", "France", "Germany", "Italy", "Peru", "Portugal", "Spain"]from main import app

def test_cities():
    response = client.get("/countries/Spain")
    assert response.status_code == 200
    assert sorted(response.json()) == ["Barcelona", "Madrid", "Valencia"]

def test_monthly_average():
    response = client.get("/countries/Spain/Madrid/January")
    assert response.status_code == 200
    assert response.json() == 10.5
def test_countries():
    response = client.get("/countries")
    assert response.status_code == 200
    assert sorted(response.json()) == ["England", "France", "Germany", "Italy", "Peru", "Portugal", "Spain"]from fastapi.testclient import TestClient

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200

def test_countries():
    response = client.get("/countries")
    assert response.status_code == 200
    assert sorted(response.json()) == ["England", "France", "Germany", "Italy", "Peru", "Portugal", "Spain"]

def test_cities():
    response = client.get("/countries/Spain")
    assert response.status_code == 200
    assert sorted(response.json()) == ["Barcelona", "Madrid", "Valencia"]

def test_monthly_average():
    response = client.get("/countries/Spain/Madrid/January")
    assert response.status_code == 200
    assert response.json() == 10.5
# tests/test_main.py
import pytest

def test_health_check(client):
    """Testar health check"""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "OK"
    assert data["post_count"] == 0  # Primeiro teste

def test_post_endpoint(client):
    """Testar endpoint POST"""
    response = client.post("/api")
    assert response.status_code == 200
    data = response.json()
    assert "version" in data
    assert data["total_calls"] == 1

def test_multiple_post_calls(client):
    """Testar múltiplas chamadas POST"""
    # Primeira chamada
    response1 = client.post("/api")
    assert response1.json()["total_calls"] == 1
    
    # Segunda chamada
    response2 = client.post("/api")
    assert response2.json()["total_calls"] == 2
    
    # Health check deve mostrar 2
    health = client.get("/health")
    assert health.json()["post_count"] == 2

def test_health_check_reflects_post_count(client):
    """Testar se health check reflete contador correto"""
    # Fazer algumas chamadas POST
    for i in range(3):
        client.post("/api")
    
    # Verificar health check
    response = client.get("/health")
    assert response.json()["post_count"] == 3
import pytest
import requests

@pytest.mark.api
class TestProductAPI:
    def test_get_product_details(self, api_client):
        response = requests.get(f"{api_client}/products/1")
        assert response.status_code == 200
        assert "id" in response.json()
        assert "name" in response.json()
        assert "price" in response.json()
    
    def test_get_recommendations(self, api_client):
        response = requests.get(f"{api_client}/products/1/recommendations")
        assert response.status_code == 200
        assert isinstance(response.json(), list)
    
    def test_create_order(self, api_client):
        payload = {
            "product_id": 1,
            "quantity": 2
        }
        response = requests.post(f"{api_client}/orders", json=payload)
        assert response.status_code == 201
        assert "order_id" in response.json()
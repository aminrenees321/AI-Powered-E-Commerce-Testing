import requests
import os
from dotenv import load_dotenv

load_dotenv()

class APIUtils:
    def __init__(self):
        self.base_url = os.getenv("API_BASE_URL", "https://api.mock-ecommerce.com")
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {os.getenv('API_TOKEN')}"
        }
    
    def get(self, endpoint, params=None):
        return requests.get(
            f"{self.base_url}/{endpoint}",
            headers=self.headers,
            params=params
        )
    
    def post(self, endpoint, data=None):
        return requests.post(
            f"{self.base_url}/{endpoint}",
            headers=self.headers,
            json=data
        )
import requests
import os
from dotenv import load_dotenv

# Загружаем переменные из .env файла
load_dotenv()


class ProjectsAPI:
    def __init__(self):
        self.base_url = os.getenv('YOUGILE_BASE_URL', 'https://ru.yougile.com')
        self.api_token = os.getenv('YOUGILE_API_TOKEN')

        if not self.api_token:
            raise ValueError(
                "YOUGILE_API_TOKEN environment variable is not set. Please create .env file with YOUR_TOKEN.")

        self.headers = {
            'Authorization': f'Bearer {self.api_token}',
            'Content-Type': 'application/json'
        }

    def post(self, data: dict):
        url = f"{self.base_url}/api-v2/projects"
        return requests.post(url, headers=self.headers, json=data)

    def get(self, project_id: str):
        url = f"{self.base_url}/api-v2/projects/{project_id}"
        return requests.get(url, headers=self.headers)

    def put(self, project_id: str, data: dict):
        url = f"{self.base_url}/api-v2/projects/{project_id}"
        return requests.put(url, headers=self.headers, json=data)
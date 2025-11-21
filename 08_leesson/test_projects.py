import pytest
import time
import sys
import os

# Добавляем родительскую директорию в путь Python
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from api.projects import ProjectsAPI

class TestProjects:
    @pytest.fixture
    def api(self):
        try:
            return ProjectsAPI()
        except ValueError as e:
            pytest.skip(f"Skipping test: {e}")

    @pytest.fixture
    def project_data(self):
        return {"title": f"Test Project {time.time()}"}

    # POSITIVE TESTS
    def test_create_project_positive(self, api, project_data):
        if api is None:
            pytest.skip("API not configured")
        response = api.post(project_data)
        assert response.status_code == 201
        assert 'id' in response.json()

    def test_get_project_positive(self, api, project_data):
        if api is None:
            pytest.skip("API not configured")
        created = api.post(project_data).json()
        response = api.get(created['id'])
        assert response.status_code == 200
        assert response.json()['title'] == project_data['title']

    def test_update_project_positive(self, api, project_data):
        if api is None:
            pytest.skip("API not configured")
        created = api.post(project_data).json()
        update_data = {"title": f"Updated Project {time.time()}"}
        response = api.put(created['id'], update_data)
        assert response.status_code == 200
        assert response.json()['title'] == update_data['title']

    # NEGATIVE TESTS
    def test_create_project_negative(self, api):
        if api is None:
            pytest.skip("API not configured")
        response = api.post({})
        assert response.status_code == 400

    def test_get_project_negative(self, api):
        if api is None:
            pytest.skip("API not configured")
        response = api.get("invalid_id")
        assert response.status_code == 404

    def test_update_project_negative(self, api, project_data):
        if api is None:
            pytest.skip("API not configured")
        created = api.post(project_data).json()
        response = api.put(created['id'], {})
        assert response.status_code == 400
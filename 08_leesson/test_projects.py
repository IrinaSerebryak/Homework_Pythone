import pytest
import time
from api.projects import ProjectsAPI


class TestProjects:

    def get_project_data(self):

        return {"title": f"Test Project {time.time()}"}

    # POSITIVE TESTS
    def test_create_project_positive(self):
        api = ProjectsAPI()
        project_data = self.get_project_data()
        response = api.post(project_data)
        assert response.status_code == 201
        assert 'id' in response.json()

    def test_get_project_positive(self):
        api = ProjectsAPI()
        project_data = self.get_project_data()
        created = api.post(project_data).json()
        response = api.get(created['id'])
        assert response.status_code == 200
        assert response.json()['title'] == project_data['title']

    def test_update_project_positive(self):
        api = ProjectsAPI()
        project_data = self.get_project_data()
        created = api.post(project_data).json()
        update_data = {"title": f"Updated Project {time.time()}"}
        response = api.put(created['id'], update_data)
        assert response.status_code == 200
        assert response.json()['title'] == update_data['title']

    # NEGATIVE TESTS
    def test_create_project_negative(self):
        api = ProjectsAPI()
        response = api.post({})
        assert response.status_code == 400

    def test_get_project_negative(self):
        api = ProjectsAPI()
        response = api.get("invalid_id")
        assert response.status_code == 404

    def test_update_project_negative(self):
        api = ProjectsAPI()
        project_data = self.get_project_data()
        created = api.post(project_data).json()
        response = api.put(created['id'], {})
        assert response.status_code == 400
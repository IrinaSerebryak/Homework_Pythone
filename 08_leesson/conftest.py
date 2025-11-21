import pytest
import os

def pytest_configure():
    pytest.BASE_URL = os.getenv('YOUGILE_BASE_URL', 'https://ru.yougile.com')
    pytest.API_TOKEN = os.getenv('YOUGILE_API_TOKEN')
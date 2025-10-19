import pytest
import requests

# Initialize a reutnable HTTP session for API tests

@pytest.fixture
def api_client():
    
    session = requests.Session()
    yield session
    session.close()


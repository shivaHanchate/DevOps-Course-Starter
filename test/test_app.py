import pytest
from dotenv import find_dotenv, load_dotenv

import trello_api
from app import app, create_app

@pytest.fixture
def client():
# Use our test integration config instead of the 'real' version
    file_path = find_dotenv('.env.test')
    load_dotenv(file_path, override=True)
# Create the new app.
    test_app = app.create_app()
# Use the app to create a test_client that can be used in our tests.
    with test_app.test_client() as client:
        yield client

def test_index_page(mock_get_requests, client):
    response = client.get('/')
    assert "200 OK" == response

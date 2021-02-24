import pytest
from dotenv import find_dotenv, load_dotenv
from unittest.mock import patch, Mock
import os

from todo_app.app import create_app

@pytest.fixture
def client():
# Use our test integration config instead of the 'real' version
    file_path = find_dotenv('.env.test')
    load_dotenv(file_path, override=True)
# Create the new app.
    test_app = create_app()
# Use the app to create a test_client that can be used in our tests.
    with test_app.test_client() as client:
        yield client

@patch('requests.get')
def test_index_page(mock_get_requests, client):    
    # Replace call to requests.get(url) with our own function    
    mock_get_requests.side_effect = mock_get_cards
    response = client.get('/') 
    assert "200 OK" == response.status     
    assert b"Test Todo" in response.data
    assert b"Test Doing" in response.data
    assert b"Test Done" in response.data   
    assert b"Done Test" not in response.data

sample_trello_cards_response = [{
    "id": "1",
    "name": "Test Todo",
    "idList": "5thnbgr43edcxsw2",
    "dateLastActivity": "2020-10-30"
},
{
    "id": "2",
    "name": "Test Doing",
    "idList": "8ikmnhy63tsgwyey",
    "dateLastActivity": "2020-10-30"
},
{
    "id": "3",
    "name": "Test Done",
    "idList": "a92je8dkw9dksowo",
    "dateLastActivity": "2020-10-30"
}
]

def mock_get_cards(url, params):    
    if url == f"https://api.trello.com/1/boards/{os.getenv('board_id')}/cards":       
        response = Mock()        
        # sample_trello_cards_response should point to some test response data        
        response.json.return_value = sample_trello_cards_response        
        return response    
    return None


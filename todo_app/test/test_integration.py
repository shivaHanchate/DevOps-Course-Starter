import pytest
from dotenv import find_dotenv, load_dotenv
from unittest.mock import patch, Mock
import os
from todo_app.mongo_db import MongoDb
from todo_app.app import create_app
from todo_app.card import Card


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


@patch('todo_app.app.MongoDb.get_items')
def test_index_page(get_items,client):    
    # Replace call to requests.get(url) with our own function    
    
    get_items.side_effect = mock_get_items    
    response = client.get('/') 

    assert "200 OK" == response.status  
    assert "Test Todo" in response.data.decode() 
    assert "Test Doing" in response.data.decode()
    assert "Test Done" in response.data.decode()
    assert "Done Test" not in response.data.decode()
    assert "Exercise 10" not in response.data.decode()
    

         
def mock_get_items(collection):
    items = [
        Card(
            "60d459cb5781dcb66dab942b",
            "Done",
            "Exercise 9",           
            "2021-06-24T21:29:29.569+00:00"
            ),
        Card(
            "60d459cb5781dcb66dab942b",
            "Doing",
            "Test Doing",           
            "2021-06-24T21:29:29.569+00:00"
            ),
        Card(
            "60d459cb5781dcb66dab942b",
            "Done",
            "Test",           
            "2021-06-24T22:26:03.415+00:00"
            ),
        Card(
            "60d459cb5781dcb66dab942b",
            "Done",
            "Test Done",           
            "2021-06-24T10:32:45.385+00:00"),
        Card(
            "60d459cb5781sdf66dab942b",
            "ToDo",
            "Test Todo",           
            "2021-06-30T09:18:13.037+00:00"
            )
        ]
    return items



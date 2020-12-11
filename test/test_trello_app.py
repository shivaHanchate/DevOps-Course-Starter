import os
import dotenv
import pytest
from selenium import webdriver
from threading import Thread
from app import create_app
from dotenv import find_dotenv, load_dotenv
import requests


def create_trello_board():
    endpoint = f"https://api.trello.com/1/boards"
    response = requests.post(endpoint, params={"name": "TestApp","key": os.getenv('api_key'), "token": os.getenv('token')}).json()        
    return response['id']  


def delete_trello_board(board_id):
    endpoint = f"https://api.trello.com/1/boards/{board_id}"
    response = requests.delete(endpoint, params={"key": os.getenv('api_key'), "token": os.getenv('token')}).json()       
    return response


@pytest.fixture(scope='module')
def test_app():
    file_path = find_dotenv('.env')
    load_dotenv(file_path, override=True)
# Create the new board & update the board id environment variable
    board_id = create_trello_board()
    os.environ['board_id'] = board_id
    # construct the new application
    application = create_app()
    # start the app in its own thread.
    thread = Thread(target=lambda: application.run(use_reloader=False))
    thread.daemon = True
    thread.start()
    yield application
    # Tear Down
    thread.join(1)
    delete_trello_board(board_id)


@pytest.fixture(scope="module")
def driver():
    with webdriver.Firefox() as driver:
        yield driver


def test_task_journey(driver, test_app):
    driver.get('http://localhost:5000/')
    assert driver.title == 'To-Do App'
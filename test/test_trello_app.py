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

def create_trello_lists():
    endpoint = f"https://api.trello.com/1/lists"
    response = requests.post(endpoint, params={"name": "ToDo","idBoard":  os.environ['board_id'], "key": os.getenv('api_key'), "token": os.getenv('token')}).json()        
    os.environ['todo_list_id'] = response['id'] 
    response = requests.post(endpoint, params={"name": "Doing","idBoard":  os.environ['board_id'], "key": os.getenv('api_key'), "token": os.getenv('token')}).json()        
    os.environ['doing_list_id'] = response['id'] 
    response = requests.post(endpoint, params={"name": "Done","idBoard":  os.environ['board_id'], "key": os.getenv('api_key'), "token": os.getenv('token')}).json()        
    os.environ['done_list_id'] = response['id'] 


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
    create_trello_lists()   
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


def test_task_journey(driver: webdriver, test_app):
    driver.get('http://localhost:5000/')    
    assert driver.title == 'To-Do App'
    text_input = driver.find_element_by_xpath("//*[@id='NewItemTitle']")
    text_input.send_keys("New Todo")   
    assert  driver.find_element_by_xpath("//button[contains(text(),'Add Item')]").text == "Add Item"  
    driver.find_element_by_xpath("//button[contains(text(),'Add Item')]").click()   
    assert  driver.find_element_by_xpath("//a[contains(text(),'Mark as In Progress')]").text == "Mark as In Progress"      
    driver.find_element_by_xpath("//a[contains(text(),'Mark as In Progress')]").click()    
    assert  driver.find_element_by_xpath("//a[contains(text(),'Mark as Done')]").text == "Mark as Done"    
    driver.find_element_by_xpath("//a[contains(text(),'Mark as Done')]").click()     
    assert  driver.find_element_by_xpath("//summary[contains(text(),'All Done Items')]").text == "All Done Items"   
    driver.find_element_by_xpath("//summary[contains(text(),'All Done Items')]").click()
    assert  driver.find_element_by_xpath("//a[contains(text(),'Mark as ToDo')]").text == "Mark as ToDo"    
    driver.find_element_by_xpath("//a[contains(text(),'Mark as ToDo')]").click()
    assert  driver.find_element_by_xpath("//a[contains(text(),'Mark as In Progress')]").text == "Mark as In Progress" 
   
   
import os
import dotenv
import pytest
from selenium import webdriver
from threading import Thread
from todo_app.app import create_app
from dotenv import find_dotenv, load_dotenv
import pymongo
import random
import string


def get_mongo_db_collection():
        dbClientUri = f"mongodb+srv://{os.getenv('user_name')}:{os.getenv('password')}@{os.getenv('mongo_url')}/{os.getenv('database_name')}?retryWrites=true&w=majority"
        mongo_db_name = os.getenv('database_name')
        collection_name = os.getenv('collection_name')
        dBClient = pymongo.MongoClient(dbClientUri)
        db = dBClient[mongo_db_name]
        return db[collection_name]


@pytest.fixture(scope='module')
def test_app():
    file_path = find_dotenv('.env')
    load_dotenv(file_path, override=True)
# Create the new board & update the board id environment variable
    os.environ['database_name'] = 'test-' + \
        ''.join(random.choice(string.ascii_uppercase + string.digits)
                for _ in range(10))
    collection = get_mongo_db_collection() 
    # construct the new application
    application = create_app()
    # start the app in its own thread.
    thread = Thread(target=lambda: application.run(use_reloader=False))
    thread.daemon = True
    thread.start()
    yield application
    # Tear Down
    thread.join(1)
    collection.drop()  

@pytest.fixture(scope="module")
def driver():
    opts = webdriver.ChromeOptions()
    opts.add_argument('--headless')
    opts.add_argument('--no-sandbox')
    opts.add_argument('--disable-dev-shm-usage')
    with webdriver.Chrome('./chromedriver', options=opts) as driver:
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
   
   
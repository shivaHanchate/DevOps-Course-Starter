import os
import pymongo
from pymongo import MongoClient
from todo_app.card import Card
import pendulum
from bson.objectid import ObjectId



class MongoDb:

    def __init__(self):        
        self.username = os.getenv('user_name')
        self.password = os.getenv('password')
        self.mongo_url = os.getenv('mongo_url')
        self.database_name = os.getenv('database_name')
        self.collection_name = os.getenv('collection_name')

    def get_mongo_db_collection(self):
        dbClientUri = f"mongodb+srv://{self.username}:{self.password}@{self.mongo_url}/{self.database_name}?retryWrites=true&w=majority"
        mongo_db_name = self.database_name
        collection_name = self.collection_name
        dBClient = pymongo.MongoClient(dbClientUri)
        db = dBClient[mongo_db_name]
        return db[collection_name]

    def get_items(collection):
        items = []
        for item in collection.find():
            items.append(
                Card(
                    item['_id'],
                    item['status'],
                    item['title'],
                    item['last_modified']
                )
            )
        return items
    
    def add_card(self,new_todo_item):
        collection=self.get_mongo_db_collection()
        collection.insert_one(
            {
                "title": new_todo_item,
                "status": 'ToDo',
                "last_modified": pendulum.now()
            }
        )   

    def move_card_not_started_in_progress(self, card_id):
        collection=self.get_mongo_db_collection()
        collection.update_one(
            {"_id": ObjectId(card_id)},
            {
                "$set": {
                    "status": 'Doing',
                    "last_modified": pendulum.now()
                }
            }
        )

    def move_card_in_progress_done(self, card_id):
        collection=self.get_mongo_db_collection()
        collection.update_one(
            {"_id": ObjectId(card_id)},
            {
                "$set": {
                    "status": 'Done',
                    "last_modified": pendulum.now()
                }
            }
        )

    def move_card_done_todo(self, card_id):
        collection=self.get_mongo_db_collection()
        collection.update_one(
            {"_id": ObjectId(card_id)},
            {
                "$set": {
                    "status": 'ToDo',
                    "last_modified": pendulum.now()
                }
            }
        )

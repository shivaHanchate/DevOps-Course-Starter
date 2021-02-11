import requests
import os


class TrelloApi:

    def __init__(self):
        self.api_key = os.getenv('api_key')
        self.token = os.getenv('token')
        self.board_id = os.getenv('board_id')
        self.todo_list_id = os.getenv('todo_list_id')
        self.doing_list_id = os.getenv('doing_list_id')
        self.done_list_id = os.getenv('done_list_id')

    def get_board_cards(self):
        endpoint = f"https://api.trello.com/1/boards/{self.board_id}/cards"
        response = requests.get(endpoint, params={"key": self.api_key, "token": self.token}).json()
        return response

    def get_board_lists(self):
        endpoint = f"https://api.trello.com/1/boards/{self.board_id}/lists"
        response = requests.get(endpoint, params={"key": self.api_key, "token": self.token}).json()               
        return response

    def get_list_cards(self, card_id):
        endpoint = f"https://api.trello.com/1/cards/{card_id}/list"
        response = requests.get(endpoint, params={"key": self.api_key, "token": self.token}).json()
        return response

    def add_card(self, new_todo_item):
        endpoint = f"https://api.trello.com/1/cards"
        response = requests.post(endpoint, params={"name": new_todo_item, "key": self.api_key, "token": self.token, "idList": self.todo_list_id}).json()
        return response

    def move_card_not_started_in_progress(self, card_id):
        endpoint = f"https://api.trello.com/1/cards/{card_id}/idList"
        response = requests.put(endpoint, params={"key": self.api_key, "token": self.token, "value": self.doing_list_id}).json()
        return response

    def move_card_in_progress_done(self, card_id):
        endpoint = f"https://api.trello.com/1/cards/{card_id}/idList"
        response = requests.put(endpoint, params={"key": self.api_key, "token": self.token, "value": self.done_list_id}).json()
        return response

    def move_card_done_todo(self, card_id):
        endpoint = f"https://api.trello.com/1/cards/{card_id}/idList"
        response = requests.put(endpoint, params={"key": self.api_key, "token": self.token, "value": self.todo_list_id}).json()
        return response

import requests
from config import api_key, token, board_id, todo_list_id, doing_list_id, done_list_id


class TrelloApi:

    def __init__(self):
        self.api_key = api_key
        self.token = token
        self.board_id = board_id
        self.todo_list_id = todo_list_id
        self.doing_list_id = doing_list_id
        self.done_list_id = done_list_id

    def get_board_cards(self):
        endpoint = f"https://api.trello.com/1/boards/{self.board_id}/cards?"
        response = requests.get(endpoint, params={"key": self.api_key, "token": self.token}).json()
        return response

    def get_board_lists(self):
        endpoint = f"https://api.trello.com/1/boards/{board_id}/lists?"
        response = requests.get(endpoint, params={"key": self.api_key, "token": self.token}).json()               
        return response

    def get_list_cards(self, card_id):
        endpoint = f"https://api.trello.com/1/cards/{card_id}/list?"
        response = requests.get(endpoint, params={"key": self.api_key, "token": self.token}).json()
        return response

    def add_card(self, new_todo_item):
        endpoint = f"https://api.trello.com/1/cards?name={new_todo_item}"
        response = requests.post(endpoint, params={"key": self.api_key, "token": self.token, "idList": self.todo_list_id}).json()
        return response

    def move_card_not_started_in_progress(self, card_id):
        endpoint = f"https://api.trello.com/1/cards/{card_id}/idList?value={self.doing_list_id}"
        response = requests.put(endpoint, params={"key": self.api_key, "token": self.token}).json()
        return response

    def move_card_in_progress_done(self, card_id):
        endpoint = f"https://api.trello.com/1/cards/{card_id}/idList?value={self.done_list_id}"
        response = requests.put(endpoint, params={"key": self.api_key, "token": self.token}).json()
        return response

    def move_card_done_todo(self, card_id):
        endpoint = f"https://api.trello.com/1/cards/{card_id}/idList?value={self.todo_list_id}"
        response = requests.put(endpoint, params={"key": self.api_key, "token": self.token}).json()
        return response

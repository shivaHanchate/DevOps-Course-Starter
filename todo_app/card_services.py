import os
from todo_app.card import Card


class CardService:
    def __init__(self):
        self.todo_list_id = os.getenv('todo_list_id')
        self.doing_list_id = os.getenv('doing_list_id')

    def card_details(self, data):
        trello_cards = []
        for item in data:
            card_id = item['id']
            card_name = item['name']
            if item['idList'] == self.todo_list_id:
                card_status = "ToDo"
            elif item['idList'] == self.doing_list_id:
                card_status = "Doing"
            else:
                card_status = "Done"
            card_mod_date = item['dateLastActivity']                     
            card = Card(card_id, card_name, card_status, card_mod_date)            
            trello_cards.append(card)            
        return trello_cards

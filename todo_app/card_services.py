import os
from todo_app.card import Card


class CardService:
    def __init__(self):
        self.todo_list_id = os.getenv('todo_list_id')
        self.doing_list_id = os.getenv('doing_list_id')

    def card_details(self, data):
        db_cards = []
        for item in data:
            card_id = item['id']
            card_name = item['name']
            if item['idList'] == "ToDo":
                card_status = "ToDo"
            elif item['idList'] == "Doing":
                card_status = "Doing"
            else:
                card_status = "Done"
            card_mod_date = item['dateLastActivity']                     
            card = Card(card_id, card_name, card_status, card_mod_date)            
            db_cards.append(card)            
        return db_cards

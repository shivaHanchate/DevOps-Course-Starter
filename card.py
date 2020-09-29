from config import api_key, token, board_id, todo_list_id, doing_list_id, done_list_id


class Card:
    def __init__(self):
        self.api_key = api_key
        self.token = token
        self.board_id = board_id
        self.todo_list_id = todo_list_id
        self.doing_list_id = doing_list_id
        self.done_list_id = done_list_id

    def card_details(self, data):
        trello_card = []
        for item in data:
            id_card = item['id']
            card_name = item['name']
            if item['idList'] == self.todo_list_id:
                status = "ToDo"
            elif item['idList'] == self.doing_list_id:
                status = "Doing"
            else:
                status = "Done"
            trello_card.append({"id": id_card, "card_name": card_name, "status": status})
        return trello_card




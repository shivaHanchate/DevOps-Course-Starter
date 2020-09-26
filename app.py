import requests
from config import api_key, token, boardId, toDoListId, doingListId, doneListId
from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)
app.config.from_object('flask_config.Config')


class Board:

    def get_Board_Cards(api_key, token, boardId):
        endpoint = f"https://api.trello.com/1/boards/{boardId}/cards?"
        response = requests.get(endpoint, params={"key": api_key, "token": token}).json()
        return response


class List:

    def get_List_Cards(api_key, token, CardId ):
        endpoint = f"https://api.trello.com/1/cards/{CardId}/list?"
        response = requests.get(endpoint, params={"key": api_key, "token": token}).json()
        return response


class Card:

    def add_Card(api_key, token, newToDoItem):
        endpoint = f"https://api.trello.com/1/cards?name={newToDoItem}"
        response = requests.post(endpoint, params={"key": api_key, "token": token, "idList": toDoListId}).json()
        return response

    def move_Card_NotStarted_InProgress(id):
        endpoint = f"https://api.trello.com/1/cards/{id}/idList?value={doingListId}"
        response = requests.put(endpoint, params={"key": api_key, "token": token}).json()
        return response

    def move_Card_InProgress_Done(id):
        endpoint = f"https://api.trello.com/1/cards/{id}/idList?value={doneListId}"
        response = requests.put(endpoint, params={"key": api_key, "token": token}).json()
        return response

    def move_Card_Done_Todo(id):
        endpoint = f"https://api.trello.com/1/cards/{id}/idList?value={toDoListId}"
        response = requests.put(endpoint, params={"key": api_key, "token": token}).json()
        return response


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        newToDoItem = request.form["NewToDoItem"]
        Card.add_Card(api_key, token, newToDoItem)
        data = Board.get_Board_Cards(api_key, token, boardId)
        return render_template('index.html', items=data)
    data = Board.get_Board_Cards(api_key, token, boardId)
    print(data)
    return render_template('index.html', items = data)


@app.route('/items/<id>/inprogress')
def move_item_to_inprogress(id):
    Card.move_Card_NotStarted_InProgress(id)
    return redirect(url_for('index'))


@app.route('/items/<id>/done')
def move_item_to_done(id):
    Card.move_Card_InProgress_Done(id)
    return redirect(url_for('index'))


@app.route('/items/<id>/todo')
def move_item_todo(id):
    Card.move_Card_Done_Todo(id)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()

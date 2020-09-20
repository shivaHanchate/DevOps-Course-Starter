import requests
from config import api_key, token, boardId, toDoListId, doingListId, doneListId
from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)
app.config.from_object('flask_config.Config')


def get_Board_Cards(api_key, token, boardId):
    endpoint = f"https://api.trello.com/1/boards/{boardId}/cards?"
    response = requests.get(endpoint, params={"key": api_key, "token": token}).json()
    return response


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


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        newToDoItem = request.form["NewToDoItem"]
        add_Card(api_key, token, newToDoItem)
        data = get_Board_Cards(api_key, token, boardId)
        return render_template('index.html', items=data)
    data = get_Board_Cards(api_key, token, boardId)
    print(data)
    return render_template('index.html', items = data)


@app.route('/items/<id>/inprogress')
def move_item_to_inprogress(id):
    move_Card_NotStarted_InProgress(id)
    return redirect(url_for('index'))


@app.route('/items/<id>/done')
def move_item_to_done(id):
    move_Card_InProgress_Done(id)
    return redirect(url_for('index'))


"""
@app.route('/', methods=["POST"])
def additem():
    NewToDoItem = request.form["NewToDoItem"]
    session.add_item(NewToDoItem)
    return render_template('index.html', items=session.get_items())

@app.route('/items/<id>/complete')
def complete_item(id):
    session.complete_item(id)
    return redirect(url_for('index'))
"""

if __name__ == '__main__':
    app.run()

from flask import Flask, render_template, request, redirect, url_for
from todo_app.trello_api import TrelloApi
from todo_app.card_services import CardService
from todo_app.view_model import ViewModel


def create_app():
    app = Flask(__name__)    
    trello_api = TrelloApi()
    card_service = CardService()

    @app.route('/')
    def index():
        trello_cards = card_service.card_details(trello_api.get_board_cards())
        item_view_model = ViewModel(trello_cards)    
        return render_template('index.html', view_model=item_view_model)

    @app.route('/', methods=["POST"])
    def add_item():
        new_todo_item = request.form["NewToDoItem"]
        trello_api.add_card(new_todo_item)
        return redirect(url_for('index'))

    @app.route('/items/<id>/inprogress')
    def move_item_to_in_progress(id):
        trello_api.move_card_not_started_in_progress(id)
        return redirect(url_for('index'))

    @app.route('/items/<id>/done')
    def move_item_to_done(id):
        trello_api.move_card_in_progress_done(id)
        return redirect(url_for('index'))

    @app.route('/items/<id>/todo')
    def move_item_todo(id):
        trello_api.move_card_done_todo(id)
        return redirect(url_for('index'))

    return app

app = create_app()
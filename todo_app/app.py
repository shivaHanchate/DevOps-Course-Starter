from flask import Flask, render_template, redirect, request, url_for
from todo_app.mongo_db import MongoDb
from todo_app.card_services import CardService
from todo_app.view_model import ViewModel
from todo_app.card import Card


def create_app():    
    app = Flask(__name__)    
    mongo_db = MongoDb()
    card_service = CardService()
    collection = mongo_db.get_mongo_db_collection()

    @app.route('/')
    def index():        
        items = MongoDb.get_items(collection)        
        item_view_model = ViewModel(items)    
        return render_template('index.html', view_model=item_view_model)

    @app.route('/', methods=["POST"])
    def add_item():
        new_todo_item = request.form["NewToDoItem"]
        mongo_db.add_card(new_todo_item)
        return redirect(url_for('index'))

    @app.route('/items/<id>/inprogress')
    def move_item_to_in_progress(id):
        mongo_db.move_card_not_started_in_progress(id)
        return redirect(url_for('index'))

    @app.route('/items/<id>/done')
    def move_item_to_done(id):
        mongo_db.move_card_in_progress_done(id)
        return redirect(url_for('index'))

    @app.route('/items/<id>/todo')
    def move_item_todo(id):
        mongo_db.move_card_done_todo(id)
        return redirect(url_for('index'))

    return app


app = create_app()
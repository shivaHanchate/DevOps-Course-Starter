import pytest

import trello_api
from app import app
from view_model import ViewModel
from card import Card


def test_shows_todo_items():

    trello_cards = [
        Card(1, "First item", "ToDo"),
        Card(2, "Second item", "Doing"),
        Card(3, "Third item", "Done")
    ]

    view_model = ViewModel(trello_cards)

    todo_items = view_model.todo_items
    assert len(todo_items) == 1
    card = todo_items[0]
    assert card.status == "ToDo"


def test_shows_doing_items():

    trello_cards = [
        Card(1, "First item", "ToDo"),
        Card(2, "Second item", "Doing"),
        Card(3, "Third item", "Done")
    ]

    view_model = ViewModel(trello_cards)

    doing_items = view_model.doing_items
    assert len(doing_items) == 1
    card = doing_items[0]
    assert card.status == "Doing"


def test_shows_done_items():

    trello_cards = [
        Card(1, "First item", "ToDo"),
        Card(2, "Second item", "Doing"),
        Card(3, "Third item", "Done")
    ]

    view_model = ViewModel(trello_cards)

    done_items = view_model.done_items
    assert len(done_items) == 1
    card = done_items[0]
    assert card.status == "Done"

def test_show_all_done_items():

    trello_cards = [
        Card(1, "First item", "ToDo", "10-10-2020"),
        Card(2, "Second item", "Doing", "10-10-2020"),
        Card(3, "Third item", "Done", "10-10-2020"),
        Card(3, "Third item", "Done", "10-10-2020"),
        Card(3, "Third item", "Done", "10-10-2020"),
        Card(3, "Third item", "Done", "10-10-2020"),
        Card(3, "Third item", "Done", "10-10-2020"),
    ]

    view_model = ViewModel(trello_cards)

    all_done_items = view_model.show_all_done_items
    assert len(all_done_items) <= 5
    card = all_done_items[0]
    assert card.status == "Done"
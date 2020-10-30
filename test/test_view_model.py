import pytest

import trello_api
from app import app
from view_model import ViewModel
from card import Card


def test_shows_todo_items():

    trello_cards = [
        Card(1, "First item", "ToDo", "2020-10-27"),
        Card(2, "Second item", "Doing", "2020-10-27"),
        Card(3, "Third item", "Done", "2020-10-27")
    ]

    view_model = ViewModel(trello_cards)

    todo_items = view_model.todo_items
    assert len(todo_items) == 1
    card = todo_items[0]
    assert card.status == "ToDo"


def test_shows_doing_items():

    trello_cards = [
        Card(1, "First item", "ToDo", "2020-10-27"),
        Card(2, "Second item", "Doing", "2020-10-27"),
        Card(3, "Third item", "Done", "2020-10-27"),
    ]

    view_model = ViewModel(trello_cards)

    doing_items = view_model.doing_items
    assert len(doing_items) == 1
    card = doing_items[0]
    assert card.status == "Doing"


def test_shows_done_items():

    trello_cards = [
        Card(1, "First item", "ToDo", "2020-10-27"),
        Card(2, "Second item", "Doing", "2020-10-27"),
        Card(3, "Third item", "Done", "2020-10-27")
    ]

    view_model = ViewModel(trello_cards)

    done_items = view_model.done_items
    assert len(done_items) == 1
    card = done_items[0]
    assert card.status == "Done"

def test_show_all_done_items():

    trello_cards = [
        Card(1, "First item", "ToDo", "2020-10-27"),
        Card(2, "Second item", "Doing", "2020-10-27"),
        Card(3, "Third item", "Done", "2020-10-27"),
        Card(4, "Fourth item", "Done", "2020-10-27"),
        Card(5, "Fifth item", "Done", "2020-10-27"),
        Card(6, "Sixth item", "Done", "2020-10-27"),
        Card(7, "Seventh item", "Done", "2020-10-27"),
    ]

    view_model = ViewModel(trello_cards)

    all_done_items = view_model.show_all_done_items
    assert len(all_done_items) == 5
    

def test_recent_done_items():

    trello_cards = [
        Card(1, "First item", "ToDo", "2020-10-27T22:02:07.091Z"),
        Card(2, "Second item", "Doing", "2020-10-28T22:02:07.091Z"),
        Card(3, "Third item", "Done", "2020-10-30T12:02:07.091Z"),
        Card(4, "Fourth item", "Done", "2020-10-30T22:02:07.091Z"),
        Card(5, "Fifth item", "Done", "2020-10-26T22:02:07.091Z"),
        Card(6, "Sixth item", "Done", "2020-10-26T22:02:07.091Z"),
        Card(7, "Seventh item", "Done", "2020-10-26T22:02:07.091Z"),
    ]

    view_model = ViewModel(trello_cards)

    recent_done_items = view_model.recent_done_items
    assert len(recent_done_items) == 2

def test_older_done_items():

    trello_cards = [
        Card(1, "First item", "ToDo", "2020-10-27T22:02:07.091Z"),
        Card(2, "Second item", "Doing", "2020-10-28T22:02:07.091Z"),
        Card(3, "Third item", "Done", "2020-10-30T12:02:07.091Z"),
        Card(4, "Fourth item", "Done", "2020-10-30T22:02:07.091Z"),
        Card(5, "Fifth item", "Done", "2020-10-26T22:02:07.091Z"),
        Card(6, "Sixth item", "Done", "2020-10-26T22:02:07.091Z"),
        Card(7, "Seventh item", "Done", "2020-10-26T22:02:07.091Z"),
    ]

    view_model = ViewModel(trello_cards)

    older_done_items = view_model.older_done_items
    assert len(older_done_items) == 3

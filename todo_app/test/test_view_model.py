from todo_app.view_model import ViewModel
from todo_app.card import Card
import pendulum

now = pendulum.now('Europe/London')
now = now.to_iso8601_string()


def test_shows_todo_items():

    items = [
        Card(1, "ToDo", "First item", "2020-10-27"),
        Card(2, "Doing", "Second item", "2020-10-27"),
        Card(3, "Done", "Third item", "2020-10-27")
    ]

    view_model = ViewModel(items)

    todo_items = view_model.todo_items
    assert len(todo_items) == 1
    card = todo_items[0]
    assert card.status == "ToDo"
    

def test_shows_doing_items():

    items = [
        Card(1, "ToDo", "First item", "2020-10-27"),
        Card(2, "Doing", "Second item", "2020-10-27"),
        Card(3, "Done", "Third item", "2020-10-27"),
    ]

    view_model = ViewModel(items)

    doing_items = view_model.doing_items
    assert len(doing_items) == 1
    card = doing_items[0]
    assert card.status == "Doing"


def test_shows_done_items():

    items = [
        Card(1, "ToDo", "First item", "2020-10-27"),
        Card(2, "Doing", "Second item", "2020-10-27"),
        Card(3, "Done", "Third item", "2020-10-27")
    ]

    view_model = ViewModel(items)

    done_items = view_model.done_items
    assert len(done_items) == 1
    card = done_items[0]
    assert card.status == "Done"

def test_show_all_done_items():

    items = [
        Card(1,"ToDo", "First item",  "2020-10-27"),
        Card(2, "Doing", "Second item", "2020-10-27"),
        Card(3, "Done", "Third item", "2020-10-27"),
        Card(4, "Done", "Fourth item", "2020-10-27"),
        Card(5, "Done", "Fifth item", "2020-10-27"),
        Card(6, "Done", "Sixth item", "2020-10-27"),
        Card(7, "Done", "Seventh item", "2020-10-27"),
    ]

    view_model = ViewModel(items)

    all_done_items = view_model.show_all_done_items
    assert len(all_done_items) == 5
        

def test_recent_done_items():  

    items = [
        Card(1, "ToDo", "First item", "2020-10-27T22:02:07.091Z"),
        Card(2, "Doing", "Second item", "2020-10-28T22:02:07.091Z"),
        Card(3, "Done", "Third item", now),
        Card(4, "Done", "Fourth item", now),
        Card(5, "Done", "Fifth item", "2020-10-26T22:02:07.091Z"),
        Card(6, "Done", "Sixth item", "2020-10-26T22:02:07.091Z"),
        Card(7, "Done", "Seventh item", "2020-10-26T22:02:07.091Z"),
    ]

    view_model = ViewModel(items)

    recent_done_items = view_model.recent_done_items
    assert len(recent_done_items) == 2

def test_older_done_items():

    items = [
        Card(1, "ToDo", "First item", "2020-10-27T22:02:07.091Z"),
        Card(2, "Doing", "Second item", "2020-10-28T22:02:07.091Z"),
        Card(3, "Done", "Third item", now),
        Card(4, "Done", "Fourth item", now),
        Card(5, "Done", "Fifth item", "2020-10-26T22:02:07.091Z"),
        Card(6, "Done", "Sixth item", "2020-10-26T22:02:07.091Z"),
        Card(7, "Done", "Seventh item", "2020-10-26T22:02:07.091Z"),
    ]

    view_model = ViewModel(items)
    print(view_model)
    older_done_items = view_model.older_done_items
    assert len(older_done_items) == 3

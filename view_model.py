class ViewModel:
    def __init__(self, items):
        self._items = items

    @property
    def items(self):
        return self._items

    @property
    def todo_items(self):
        todo_items = []
        for item in self.items:
            if item.status == "ToDo":
                todo_items.append(item)
        return todo_items

    @property
    def doing_items(self):
        doing_items = []
        for item in self.items:
            if item.status == "Doing":
                doing_items.append(item)
        return doing_items

    @property
    def done_items(self):
        done_items = []
        for item in self.items:
            if item.status == "Done":
                done_items.append(item)
        return done_items

    @property
    def show_all_done_items(self):
        pass

    @property
    def recent_done_items(self):
        pass

    @property
    def older_done_items(self):
        pass
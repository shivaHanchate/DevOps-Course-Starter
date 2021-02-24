import pendulum

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
        all_done_items = []        
        for item in self.items:
            if item.status == "Done":
                all_done_items.append(item)
        return all_done_items

    @property
    def recent_done_items(self):
        recent_done_items = []           
        for item in self.items:            
            if item.status == "Done":
                now = pendulum.now('Europe/London')
                now = now.to_iso8601_string()
                now = pendulum.parse(now).format('DD/MM/YYYY') 
                mod_date = pendulum.parse(str(item.mod_date)).format('DD/MM/YYYY')                
                if  mod_date == now:
                    recent_done_items.append(item)
        return recent_done_items

    @property
    def older_done_items(self):
        older_done_items = []
        for item in self.items:            
            if item.status == "Done":
                now = pendulum.now('Europe/London')
                now = now.to_iso8601_string()
                now = pendulum.parse(now).format('DD/MM/YYYY')
                mod_date = pendulum.parse(str(item.mod_date)).format('DD/MM/YYYY')                
                if  mod_date != now:
                    older_done_items.append(item)
        return older_done_items


from datetime import date


class Entry:
    def __init__(self, id, title, body):
        self.id = id
        self.title = title
        self.body = body
        self.date_created = date.today()

    def set_body(self, body):
        self.body = body

    def set_title(self, title):
        self.title = title

    def set_id(self, id):
        self.id = id

    def get_id(self):
        return self.id

    def get_title(self):
        return self.title

    def get_body(self):
        return self.body

    def __eq__(self, other):
        if self is other:
            return True
        if not isinstance(other, Entry):
            return False
        return (self.id == other.id and
                self.title == other.title and
                self.body == other.body and
                self.date_created == other.date_created)

    def __hash__(self):
        return hash((self.id, self.title, self.body, self.date_created))

    def get_entry(self):
        return "TITLE: " + self.title + "\nBODY: " + self.body

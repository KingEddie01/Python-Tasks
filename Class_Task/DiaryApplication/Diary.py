from Class_Task.DiaryApplication.Entry import Entry


class Diary:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.is_locked = False
        self.diaries = []

    def locked(self):
        self.is_locked = True

    # def unlock(self.password):
    #     self.is_locked = False

    def get_is_locked(self):
        return self.is_locked

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password

    def generate_id(self):
        return len(self.diaries) + 1

    def find_entry(self, entry_id):
        for entry in self.diaries:
            if entry.get_id() == entry_id:
                return entry
        raise ValueError("CANNOT FIND ENTRY")

    def create_entry(self, title, body):
        entry_id = self.generate_id()
        entry = Entry(entry_id, title, body)
        if not entry.get_title() and not entry.get_body():
            raise ValueError("TITLE AND BODY CANNOT BE EMPTY")
        self.diaries.append(entry)

    def delete_entry(self, entry_id):
        entry = self.find_entry(entry_id)
        self.diaries.remove(entry)

    def update_entry(self, entry_id, new_title, new_body):
        entry = self.find_entry(entry_id)
        entry.set_title(new_title)
        entry.set_body(new_body)
        entry.set_id(entry_id)

    def __eq__(self, other):
        if self is other:
            return True
        if not isinstance(other, Diary):
            return False
        return (self.is_locked == other.is_locked and
                self.username == other.username and
                self.password == other.password and
                self.diaries == other.diaries)

from Class_Task.DiaryApplication.Diary import Diary


class Diaries:
    def __init__(self):
        self.diaries_collection = []
        self.username = None

    def add_diary(self, username, password):
        diary = Diary(username, password)
        self.diaries_collection.append(diary)

    def find_by_username(self, username):
        for diary in self.diaries_collection:
            if diary.get_username() == username:
                return diary
        raise ValueError("Username cannot be found")

    def get_number_of_diaries_saved(self):
        return len(self.diaries_collection)

    def delete_diary(self, username, password):
        diary = self.find_by_username(username)
        self.diaries_collection.remove(diary)

    def get_username(self):
        return self.username

    def update_entry(self, id, title, body):
        diary = self.find_by_username(self.username)
        diary.update_entry(id, title, body)

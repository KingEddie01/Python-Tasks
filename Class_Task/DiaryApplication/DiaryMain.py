from datetime import date

from Class_Task.DiaryApplication.Diaries import Diaries
from Class_Task.DiaryApplication.Entry import Entry


class DiaryMain:
    def __init__(self):
        self.username = None
        self.password = None
        self.title = None
        self.body = None
        self.date = date.today()
        self.diary = Diaries()
        self.entry = Entry(id, self.title, self.body)

    def display(self, message):
        print(message)

    def collect_input(self, input_message):
        return input(input_message)

    def main_display(self):
        self.display("WELCOME TO EDDIE'S DIARY")
        self.display("\"your story, your life!!!\"")
        choice = self.collect_input(
            """Select an option
            HOME PAGE
            1.Create Account:
            2.Login:
            0.Exit
            """
        )
        if choice == "1":
            self.create_account()
        elif choice == "2":
            self.login()
        elif choice == "0":
            self.exit()
        else:
            self.exit()

    def exit(self):
        self.display("Thanks for using Eddie's Diary")
        self.display("")
        exit(0)

    def login(self):
        self.display("Login Username and Password")
        try:
            self.username = self.collect_input("Enter Username : ")
            self.password = self.collect_input("Enter Password : ")
            if self.diary.find_by_username(self.username).get_password() == self.password:
                self.display("Login successful")
                self.menu_display()
        except Exception as e:
            self.display(str(e))
            self.login_display()

    def login_display(self):
        select = self.collect_input(
            """Select an option
            1. Login
            2. Create a new account
            0. Exit
            """
        )
        if select == "1":
            self.login()
        elif select == "2":
            self.create_account()
        elif select == "0":
            self.exit()

    def create_account(self):
        self.display("Create Account")
        self.username = self.collect_input("Enter Username : ");
        self.password = self.collect_input("Enter password : ")
        if not self.username:
            self.display("Enter Valid Username")
            self.create_account()
        elif not self.password:
            self.display("Enter Valid Password")
            self.create_account()
        else:
            self.display(f"Username and Password created successfully on {self.date}")
            self.diary.add_diary(self.username, self.password)
            self.menu_display()

    def menu_display(self):
        choice_menu = self.collect_input(
            """MENU
            1.Create Entry:
            2.Update Entry:
            3.Find Entry:
            4.Delete Entry:
            0.Exit
            """
        )
        if choice_menu == "1":
            self.create_entry()
        elif choice_menu == "2":
            self.update_entry()
        elif choice_menu == "3":
            self.find_entry()
        elif choice_menu == "4":
            self.delete_entry()
        elif choice_menu == "0":
            self.main_display()

    def find_entry(self):
        self.display("Find Entry")
        try:
            entry_id = self.collect_input("Enter id : ")
            self.diary.find_by_username(self.username).find_entry(int(entry_id))
            entry = self.diary.find_by_username(self.username).find_entry(int(entry_id))
            self.display(entry.get_entry())
            self.entry_display()
        except Exception as e:
            self.display(str(e))
            self.entry_display()

    def entry_display(self):
        select_find = self.collect_input(
            """Select an option:
            1.Find New Entry:
            0.Exit
            """
        )
        if select_find == "1":
            self.find_entry()
        elif select_find == "0":
            self.menu_display()

    def delete_entry(self):
        self.display("Delete entry")
        entry_id = None
        try:
            entry_id = self.collect_input("Enter id :")
            self.diary.find_by_username(self.username).delete_entry(int(entry_id))
            self.display(f"Entry {entry_id} was deleted successfully")
        except Exception as e:
            self.display(str(e))
        select_delete = self.collect_input(
            """Select an option:
            1.Delete New Entry:
            0.Exit
            """
        )
        if select_delete == "1":
            self.delete_entry()
        elif select_delete == "0":
            self.menu_display()

    def update_entry(self):
        self.display("Update Entry")
        entry_id = self.collect_input("Enter id : ")
        self.entry = self.diary.find_by_username(self.username).find_entry(int(entry_id))
        new_title = self.collect_input("Enter New title")
        new_body = self.collect_input("Enter New body")
        self.diary.find_by_username(self.username).update_entry(int(entry_id), self.title, self.body)
        self.entry.title = new_title
        self.entry.body = new_body
        self.display(f"Entry has been updated successfully on {self.date}")
        self.display_option()

    def display_option(self):
        select_update = self.collect_input(
            """Select an option:
            1.Update Entry:
            0.Exit
            """
        )
        if select_update == "1":
            self.update_entry()
        elif select_update == "0":
            self.menu_display()
        else:
            self.display("Enter a valid option")
            self.display_option()

    def create_entry(self):
        self.display("Create Entry")
        self.title = self.collect_input("Enter title : ")
        self.body = self.collect_input("Enter body : ")
        self.diary.add_diary(self.title, self.body)
        self.diary.find_by_username(self.username).create_entry(self.title, self.body)
        self.display(f"Successfully created entry on {self.date}")
        self.display_create_entry()

    def display_create_entry(self):
        select_entry = self.collect_input(
            """Select an option:
            1.Create New Entry:
            0.Exit
            """
        )
        if select_entry == "1":
            self.create_entry()
        elif select_entry == "0":
            self.menu_display()
        else:
            self.display("Enter a valid option")
            self.display_create_entry()


if __name__ == "__main__":
    diary_main = DiaryMain()
    diary_main.main_display()

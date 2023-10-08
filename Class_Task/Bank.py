from Class_Task.Account import Account


class Bank:

    def __init__(self, bank_name):
        self.__bank_name = bank_name
        self.__accounts = []

    def register(self, firstName, lastName, pin):
        new_account = Account(self.__generate_accountNumber(), firstName + " " + lastName, pin)
        self.__accounts.append(new_account)

    def __generate_accountNumber(self):
        return str(len(self.__accounts) + 1)

    def find_account(self, accountNumber):
        for account in self.__accounts:
            if account.get_accountNumber() == accountNumber:
                return account

    def deposit(self, amount, accountNumber):
        self.find_account(accountNumber).deposit(amount)

    def withdraw(self, amount, accountNumber, pin):
        self.find_account(accountNumber).withdraw(amount, pin)

    def check_balance(self, accountNumber, pin):
        return self.find_account(accountNumber).check_balance(pin)

    def transfer(self, amount, sender_accountNumber, receiver_accountNumber, pin):
        self.find_account(sender_accountNumber).withdraw(amount, receiver_accountNumber, pin)
        self.find_account(receiver_accountNumber).deposit(amount, sender_accountNumber, pin)

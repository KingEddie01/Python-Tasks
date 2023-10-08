from Class_Task.BankApplication.Account import Account


class Bank:
    def __init__(self, bank_name):
        self.account_list = []
        self.bank_name = bank_name

    def register(self, first_name, last_name, pin):
        full_name = f"{first_name} {last_name}"
        accountNumber = self.generate_account_number()
        account = Account(full_name, self.generate_account_number(), pin)
        self.account_list.append(account)
        return accountNumber

    def generate_account_number(self):
        return str(len(self.account_list) + 1)

    def find_account(self, account_number):
        for data in self.account_list:
            if data.get_account_number() == account_number:
                return data
        else:
            raise ValueError("CANNOT FIND ACCOUNT")

    def deposit(self, account_number, amount):
        if amount > 0:
            self.find_account(account_number).deposit(amount)
        else:
            raise ValueError("Invalid amount")

    def withdraw(self, account_number, amount, pin):
        self.find_account(account_number).withdraw(amount, pin)

    def transfer(self, from_account, to_account, amount, pin):
        account_sender = self.find_account(from_account)
        account_sender.withdraw(amount, pin)
        account_receiver = self.find_account(to_account)
        account_receiver.deposit(amount)

    def check_balance(self, account_number, pin):
        return self.find_account(account_number).check_balance(pin)

    def number_of_registered_account(self):
        return len(self.account_list)

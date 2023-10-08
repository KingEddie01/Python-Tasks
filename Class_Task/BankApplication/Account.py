class Account:
    def __init__(self, account_name, account_number, pin):
        self.balance = 0
        self.account_name = account_name
        self.pin = pin
        self.account_number = account_number

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            raise ValueError("Enter a valid amount")

    def check_balance(self, pin):
        if self.pin == pin:
            return self.balance
        raise ValueError("INVALID PIN")

    def get_balance(self):
        return self.balance

    def update_pin(self, old_pin, new_pin):
        self.validate_pin(old_pin)
        self.pin = new_pin

    def validate_pin(self, pin):
        if self.pin != pin:
            raise ValueError("Invalid Pin")

    def withdraw(self, amount, pin):
        self.validate_pin(pin)
        if 0 < amount < self.balance:
            self.balance -= amount
        else:
            raise ValueError("INSUFFICIENT BALANCE")

    def get_account_number(self):
        return self.account_number

    def get_pin(self):
        return self.pin

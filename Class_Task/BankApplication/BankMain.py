from datetime import date

from Class_Task.BankApplication.Bank import Bank


class BankMain:
    firstName = ""
    lastName = ""
    pin = ""
    accountNumber = ""
    accountBalance = 0.0
    amount = 0.0
    date = date.today()
    accountName = ""
    bank = Bank("XCHANGE BANK")

    @staticmethod
    def display(message):
        print(message)

    @staticmethod
    def collect_input(input_message):
        return input(input_message)

    @staticmethod
    def first_menu():
        BankMain.display("WELCOME TO XCHANGE BANK")
        BankMain.display("\"Money Farm\"")
        choice = BankMain.collect_input("""
            HOME PAGE
            Select an option
            1.Register Account
            2.Exit
            """)

        if choice == "1":
            BankMain.register()
        elif choice == "2":
            BankMain.exit()
        else:
            BankMain.display("Invalid input")
            BankMain.first_menu()

    @staticmethod
    def register():
        BankMain.display("Register Account")
        BankMain.firstName = BankMain.collect_input("Enter First Name : ")
        if not BankMain.firstName:
            BankMain.display("First Name is empty")
            BankMain.register()

        BankMain.lastName = BankMain.collect_input("Enter Last Name : ")
        if not BankMain.lastName:
            BankMain.display("Last Name is empty")
            BankMain.register()

        BankMain.pin = BankMain.collect_input("Enter Pin : ")
        if not BankMain.pin:
            BankMain.display("Invalid Pin, Please try again")
            BankMain.register()

        account_number = BankMain.bank.register(BankMain.firstName, BankMain.lastName, BankMain.pin)
        BankMain.display("Account Successfully Created")
        BankMain.display("your account number is: " + account_number)
        BankMain.mini_menu()

    @staticmethod
    def mini_menu():
        choose = BankMain.collect_input("""
            Select an Option
            1.Deposit
            2.Withdraw
            3.Transfer
            4.Check Balance
            0.Exit
            """)

        if choose == "1":
            BankMain.deposit()
        elif choose == "2":
            BankMain.withdraw()
        elif choose == "3":
            BankMain.transfer()
        elif choose == "4":
            BankMain.check_balance()
        elif choose == "0":
            BankMain.exit()
        else:
            BankMain.display("Invalid option")
            BankMain.mini_menu()

    @staticmethod
    def deposit():
        BankMain.display("Deposit")
        try:
            BankMain.accountNumber = BankMain.collect_input("Enter Account Number : ")
            BankMain.amount = float(BankMain.collect_input("Enter Amount: "))
            BankMain.bank.deposit(BankMain.accountNumber, BankMain.amount)
            balance = BankMain.bank.check_balance(BankMain.accountNumber, BankMain.pin)
            BankMain.display(f"""
                Credit Alert!!!
                Your account {BankMain.accountNumber} has been credited with ${BankMain.amount}
                on {BankMain.date}
                your Balance is {balance}
            """)
            BankMain.mini_menu()
        except ValueError as e:
            BankMain.display(f"Error: {e}")
            BankMain.mini_menu()

    @staticmethod
    def withdraw():
        BankMain.display("Withdraw")
        try:
            BankMain.accountNumber = BankMain.collect_input("Enter Account Number : ")
            BankMain.amount = float(BankMain.collect_input("Enter Amount : "))
            BankMain.pin = BankMain.collect_input("Enter your pin: ")
            BankMain.bank.withdraw(BankMain.accountNumber, float(BankMain.amount), BankMain.pin)
            balance = BankMain.bank.check_balance(BankMain.accountNumber, BankMain.pin)
            BankMain.display(f"""
                Debit Alert!!!
                Your account {BankMain.accountNumber} has been debited with ${BankMain.amount}
                on {BankMain.date}
                your Balance is {balance}
            """)
            BankMain.mini_menu()
        except ValueError as e:
            BankMain.display(f"Error: {e}")
            BankMain.mini_menu()

    @staticmethod
    def transfer():
        BankMain.display("Transfer")
        try:
            BankMain.accountNumber = BankMain.collect_input("Enter Account Number : ")
            BankMain.amount = float(BankMain.collect_input("Enter Amount : "))
            recipient_account_number = BankMain.collect_input("Enter Recipient Account Number : ")
            BankMain.bank.transfer(BankMain.amount, BankMain.accountNumber, recipient_account_number, BankMain.pin)
            balance = BankMain.bank.check_balance(BankMain.accountNumber, BankMain.pin)
            BankMain.display(f"""
                Debit Alert!!!
                Your account has been debited with ${BankMain.amount}
                {BankMain.date}
                your Balance is {balance}
            """)
        except ValueError as e:
            BankMain.display(f"Error: {e}")
        BankMain.mini_menu()

    @staticmethod
    def check_balance():
        BankMain.display("Check Balance")
        try:
            BankMain.accountNumber = BankMain.collect_input("Enter Account Number : ")
            BankMain.pin = BankMain.collect_input("Enter PIN Number : ")
            balance = BankMain.bank.check_balance(BankMain.accountNumber, BankMain.pin)
            BankMain.display(f"Balance: {balance}")
        except ValueError as e:
            BankMain.display(f"Error: {e}")
        BankMain.mini_menu()

    @staticmethod
    def exit():
        BankMain.display("Thanks for using XCHANGE Bank")


if __name__ == "__main__":
    BankMain.first_menu()

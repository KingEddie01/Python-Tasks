import unittest

from Class_Task.BankApplication.Bank import Bank


class TestBank(unittest.TestCase):
    def test_bank_exist(self):
        bank = Bank("ACCESS BANK NIGERIA PLC")
        self.assertIsNotNone(bank)

    def test_register_account(self):
        bank = Bank("ACCESS BANK NIGERIA PLC")
        bank.register("Edmund", "Udeh", "pin")
        self.assertEqual(1, bank.number_of_registered_account())

    def test_deposit_into_account(self):
        bank = Bank("ACCESS BANK NIGERIA PLC")
        bank.register("Edmund", "Udeh", "pin")
        bank.find_account("1")
        bank.deposit("1", 5000.00)
        self.assertEqual(5000.00, bank.check_balance("1", "pin"))

    def test_cannot_deposit_negative_amount(self):
        bank = Bank("ACCESS BANK NIGERIA PLC")
        bank.register("Edmund", "Udeh", "pin")
        bank.find_account("1")
        with self.assertRaises(ValueError):
            bank.deposit("1", -5000.00)

    def test_withdraw_from_account(self):
        bank = Bank("ACCESS BANK NIGERIA PLC")
        bank.register("Edmund", "Udeh", "pin")
        bank.find_account("1")
        bank.deposit("1", 5000.00)
        self.assertEqual(5000.00, bank.check_balance("1", "pin"))
        bank.withdraw("1", 3000.00, "pin")
        self.assertEqual(2000.00, bank.check_balance("1", "pin"))

    def test_transfer_to_other_bank(self):
        bank = Bank("ACCESS BANK NIGERIA PLC")
        bank.register("Edmund", "Udeh", "pin")
        bank.find_account("1")
        bank.deposit("1", 5000.00)
        self.assertEqual(5000.00, bank.check_balance("1", "pin"))
        bank.register("Ashley", "Ndabai", "pin1")
        bank.find_account("2")
        self.assertEqual(0.0, bank.check_balance("2", "pin1"))
        bank.transfer("1", "2", 2000.00, "pin")
        self.assertEqual(2000.00, bank.check_balance("2", "pin1"))
        self.assertEqual(3000.00, bank.check_balance("1", "pin"))


if __name__ == "__main__":
    unittest.main()

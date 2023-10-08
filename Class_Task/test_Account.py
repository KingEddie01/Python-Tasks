from unittest import TestCase

from Class_Task.Account import Account


class TestAccount(TestCase):
    def setUp(self):
        self.account = Account("123456", "Edmund", "1234")

    def test_deposit(self):
        self.account.deposit(5000)
        self.assertEqual(self.account.getBalance(), 5000)

    def test_withdraw(self):
        self.account.deposit(5000)
        self.assertEqual(self.account.getBalance(), 5000)
        self.account.withdraw(2000, "1234")
        self.assertEqual(self.account.getBalance(), 3000)

    def test_check_balance(self):
        self.account.deposit(5000)
        self.account.checkBalance("1234")
        self.assertEqual(self.account.getBalance(), 5000)

    def test_cannot_withdraw_negative_amount(self):
        self.account.deposit(5000)
        self.assertEqual(self.account.getBalance(), 5000)
        self.assertRaises(ValueError, self.account.validate_withdrawal, -3000)

    def test_cannot_withdraw_with_wrong_pin(self):
        self.account.deposit(5000)
        self.assertEqual(self.account.getBalance(), 5000)
        self.account.withdraw(2000, "1234")
        self.assertRaises(ValueError, self.account.validate_Pin, "2345")

    def test_for_update_pin(self):
        self.account.update_pin("1234", "7456")
        self.assertEqual(self.account.checkBalance("7456"), 0)

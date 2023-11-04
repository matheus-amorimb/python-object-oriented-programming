import unittest
from src.BankAccount import BankAccount

class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.account_number = '180698'
        self.first_name = 'FIRST'
        self.last_name = 'LAST'
        self.account = BankAccount(self.account_number, self.first_name, self.last_name)

    def test_initial_balance(self):
        self.assertEqual(self.account.balance, 0.0)

    def test_deposit(self):
        self.account.deposit(100)
        self.assertEqual(self.account.balance, 100.0)

    def test_withdraw(self):
        self.account.deposit(100)
        self.account.withdraw(50)
        self.assertEqual(self.account.balance, 50.0)

    def test_apply_interest(self):
        self.account.deposit(100)
        BankAccount.set_interest_rate(0.5)
        self.account.apply_interest()
        self.assertEqual(self.account.balance, 100.5)

    def test_set_interest_rate(self):
        BankAccount.set_interest_rate(1.0)
        self.assertEqual(BankAccount.get_interest_rate(), 1.0)

    def test_deposit_negative_value(self):
        with self.assertRaises(ValueError):
            self.account.deposit(-50)

    def test_withdraw_negative_value(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(-50)
    
    def test_withdraw_more_than_balance(self):
        with self.assertRaises(ValueError):
            self.initial_balance = 100
            BankAccount(self.account_number, self.first_name, self.last_name, self.initial_balance)
            self.account.withdraw(200)

    def test_create_account_blank_first_name(self):
        self.first_name = ''
        with self.assertRaises(ValueError):
            BankAccount(self.account_number, self.first_name, self.last_name)

    def test_create_account_blank_last_name(self):
        with self.assertRaises(ValueError):
            self.last_name = ''
            BankAccount(self.account_number, self.first_name, self.last_name)

    def test_create_account_account_number_string(self):
        with self.assertRaises(ValueError):
            self.account_number = 'ABCD'
            BankAccount(self.account_number, self.first_name, self.last_name)

    def tearDown(self):
        pass

if __name__ == "__main__":
    pass
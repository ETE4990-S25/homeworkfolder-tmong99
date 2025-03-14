import unittest

class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = {}
    
    def add_account(self, account_num, initial_balance = 0):
        """Add a new account to the bank with initialized balance of 0"""

        if account_num in self.accounts:
            print("This account already exists in the bank")
        else:
            if initial_balance < 0:
                print("Invalid Initial Balance (Must Be Greater than 0)")
            else:
                self.accounts[account_num] = initial_balance
                print(f"Account #{account_num} added with initial balance of ${initial_balance}")
    
    def check_balance(self, account_num):
        """Check the balance of an account"""
        if account_num in self.accounts:
            print(f"Account {account_num} balance: ${self.accounts[account_num]}")
        else:
            print(f"Account number {account_num} does not exist")

    def deposit(self, account_num, amount):
        """Deposit Money Into An Account"""
        if account_num in self.accounts:
            if amount > 0:
                self.accounts[account_num] += amount
                print(f"${amount} has been deposited into account {account_num}. Your Balance is now ${self.accounts[account_num]}")
            else:
                print("Please enter a valid number to deposit")
        else:
            print(f"Account number {account_num} doesn't exist")

    def withdraw(self, account_num, amount):
        """Withdraw Money From Account"""
        if account_num in self.accounts:
            if amount > 0:
                if self.accounts[account_num] >= amount:
                    self.accounts[account_num] -= amount
                    print(f"${amount} has been withdrawn from account {account_num} Your Balance is now ${self.accounts[account_num]}")
                else:
                    print("Insufficient Funds")
            else:
                print("Please Enter a Valid Amount to Withdraw")
        else:
            print("Account Number {account_num} doesn't exist")

    def list_accounts(self):
        """List All Accounts and Respective Balances"""
        if not self.accounts:
            print("This Bank Has No Accounts")
        else:
            print("Accounts In The Bank: ")
            for account_number, balance in self.accounts.items():
                print(f"Account {account_number}: ${balance}")



class BankTest(unittest.TestCase):
    def setUp(self):
        """Set up a Bank Instance and test some accounts"""
        self.bank = Bank("BankTest")
        self.bank.add_account("123", 1000)
        self.bank.add_account("321", 500)

    # test add_account() method 
    def test_add_account(self):
        """Test Adding a New Account"""
        with self.assertRaises(ValueError):
           self.bank.add_account("123", 2000)
    
    # test withdraw() method
    def test_withdraw(self):
        self.bank.withdraw("123", 100)
        self.assertEqual(self.bank.accounts["321"], 600)

    # test deposit() method
    def test_deposit(self):
        self.bank.deposit("123", 500)
    
    # test check_balance() method
    def test_check_balance(self):
        self.assertEqual(self.bank.accounts["123"], 1400)

        with self.assertRaises(KeyError):
            self.bank.check_balance("9001")
    
    

if __name__ == "__main__":
    #unittest.main()
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
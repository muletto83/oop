'''
Assignment
Complete the BankAccount class.

Complete the constructor
Set __account_number to account_number
Set __balance to initial_balance
Complete the public getters
Complete the get_account_number method to get the value of the private variable __account_number and return it.
Complete the get_balance method to get the value of the private variable __balance and return it.
Complete the deposit method
It should accept an amount as input and add it to the account balance.
If the deposit amount isn't positive, it should raise a ValueError exception with the message cannot deposit zero or negative funds. Otherwise, it should add the amount to the balance.
Complete the withdraw method
It should accept an amount and check if there is enough money in the account for the withdrawal.
If the withdrawal amount isn't positive, it should raise a ValueError exception with the message cannot withdraw zero or negative funds.
Then, if there are not enough funds it should raise a ValueError exception with the message insufficient funds.
Otherwise, it should deduct the amount from the balance
'''

class BankAccount:
    def __init__(self, account_number, initial_balance):
        pass

    def get_account_number(self):
        pass

    def get_balance(self):
        pass

    def deposit(self, amount):
        pass

    def withdraw(self, amount):
        pass

"""
# Practice: ATM Interface

Save your solution in a directory in `practice/` named `atm-interface`.

An account will be a class named `Account` in a module named `account`: it will have private attributes for the balance and interest rate.
Remember to underscore `_` prefix any private attributes.
A newly-instantiated account will have zero balance and an interest rate of 0.1%.

Write instance methods in the account class that:

* `get_funds()` Return account balance   need 
* `deposit(amount)` Deposit to the account
* `check_withdrawal(amount)` Return `True` if large enough balance for a withdrawal
* `withdraw(amount)` Withdraw an allowed amount; raise a `ValueError` if insufficent balance
* `calc_interest()` Calculate and return interest on the current account balance

I've already written out [some test code](/practice/atm-interface/account_test.py) that will check that your `Account` class behaves as expected.
Save it as `account_test.py` in your solution directory.
These tests should all pass for your `Account` implementation.
Either run `py.test` from the `atm-interface` directory, or setup a PyCharm test Run Configuration.

You should still write doctests for your functions that test internal implementation.
E.g. Check that internal variables are set correctly.
My classes can't do that since internal variables are not part of the defined behavior.

"""
import random as rd


class Account:
    """
    
    """

    def __init__(self, first_name: str, surname: str, _balance: int, account_type: str):
        self.first_name = first_name
        self.surname = surname
        self.account_type = account_type
        self._balance = _balance
        self._interest_rate = 0.1  # Correct ?

        self._account_number = self.generate_account_number()

    def __repr__(self):
        message = f'Ledger balance: {self._balance}'
        return message

    def __str__(self):
        message = f'Your current balance is {self._balance}'
        return message

    @classmethod
    def from_csv_string(cls, csv_string):
        """
        art999999, float(0.0), checking  
        """
        first_name, surname, account_number, _balance, account_type = csv_string.split(',')
        _balance = float(_balance)
        pasticci = cls(first_name=first_name, surname=surname, _balance=_balance, account_type=account_type)
        return pasticci

    @property  # decorator modifies behavior of function below
    def fullname(self):  # Convenience METHOD; @ makes it act like a property/attribute; callable as .fullname
        return f'{self.first_name} {self.surname}'


    def generate_account_number(self):

        first_three = self.surname[0:3]
        result = rd.randint(100000, 300000)
        six_dig = str(result)[0:7]
        account_number = first_three + six_dig

        return account_number

    def get_funds(self):  # METHOD
        """
        Returns account balance
        """
        return self._balance

    def check_withdraw(self, amount: int):  # METHOD
        """
        Return True (boolean) if large enough balance for a withdrawal
        """
        if amount <= self._balance:
            return True
        else:
            return False

    def withdraw(self, amount: int):  # METHOD
        """
        Withdraw allowed amount; raise value error if insufficient funds.
        """
        if self.check_withdraw(amount):  # Inputs the output from check-withdrawal(amount)
            self._balance -= amount  # Balance is decremented after each withdrawal
            return self._balance  # New balance is shown
        else:
            message = f'Insufficient funds.'
            raise ValueError(message)

    def deposit(self, amount: int):  # METHOD
        """
        Deposit funds 
        """
        self._balance += amount  # amount is the required param passed in this METHOD
        return self._balance

    def calc_interest(self):  # METHOD
        """
        Calculate and return interest on current account balance. 
        _interest_rate
        """
        # TODO: If no 0 balance in 30-day period, add interest; else, no interest
        interest = self._balance * self._interest_rate
        return interest


    def get_standing(self):
        if self._balance <= 1000:
            return False
        else:
            return True


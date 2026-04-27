import datetime as dt
from datetime import timezone
import random

class Account:
    current_time = dt.datetime.now(timezone.utc)


    def __init__(self, account_no, first_name, last_name, offset, balance=0):
        self.account_no = account_no
        self._first_name = first_name
        self._last_name = last_name
        self. tz_offset = offset
        self._balance = balance

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self._first_name = value

    @property
    def last_name(self):
        return self._last_name
    @last_name.setter
    def last_name(self, value):
        self._last_name = value

    @property
    def full_name(self):
        return f"{self._first_name} {self._last_name}".title()

    @property
    def balance(self):
        if self._balance < 0:
            raise ValueError("Balance should be 0 or higher.")
        else:
            return self._balance

    def deposit(self, amount):
        print(f"{amount} credited ...")
        self._balance += amount

    def withdraw(self, amount):
        print(f"{amount} debited...")
        self._balance -= amount





id1 = Account(1234, 'ajay', 'lodhi', 7, 100)
print(id1.first_name)
print(id1.full_name)
print(id1.balance)

id1.deposit(100)
print(id1.balance)
id1.withdraw(50)
print(id1.balance)



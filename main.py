import datetime as dt
import itertools
from datetime import timezone, timedelta


class Account:
    current_time = dt.datetime.now(timezone.utc)
    interest = 0.03
    result = {}



    def __init__(self, account_no, first_name, last_name, offset= 7, balance=0):
        self.account_no = account_no
        self._first_name = first_name
        self._last_name = last_name
        self.tz_offset =timezone(timedelta(hours = offset))
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
        Account.result['Transaction code'] = 'D'

    def withdraw(self, amount):
        if amount > self.balance:
            print("transaction declined...")
        else:
            print(f"{amount} debited...")
            self._balance -= amount

    def int_calc(self):
        interest = self._balance * Account.interest
        return interest + self._balance

class Transaction:
    transaction_counter = itertools.count(start=0, step=1)

    def __init__(self, account_number, transaction_code, tz_offset):
        self.account_number = account_number
        self.transaction_code = transaction_code
        self.transaction_id = next(self.transaction_counter)
        self.time_utc = dt.datetime.now(timezone.utc)
        self.time = self.time_utc.astimezone(timezone(timedelta(hours=tz_offset)))

        def __str__(self):
            return (f"{self.transaction_code}-{self.account_number}-{self.time_utc.strftime('%Y%m%d%H%M%S')}"
                    f"-{self.transaction_id}")


transact = Transaction(account_number=1, transaction_code='D', tz_offset=-7)
print(transact)
conf_no = f"{transact.transaction_code}-{transact.account_number}-{transact.time_utc.strftime('%Y%m$d%H%M%S')}-{transact.transaction_id}"
print(conf_no)



hello = Transaction(1111,100, mst=7)
print(hello.time)
print(hello.time_utc)
hello2 = Account(111112, 'satyam', 'kumar', 7, 203)
hello2.deposit(200)
print(hello.transaction_id)


# id1 = Account(1234, 'ajay', 'lodhi', 7, 100)
# print(id1.first_name)
# print(id1.full_name)
# print(id1.balance)
#
# id1.deposit(100)
# print(id1.balance)
# id1.withdraw(50)
# print(id1.balance)
#
# id1.withdraw(30000)
# print(id1.transaction_id)
#
# satyam = Account(1234, 'satyam', 'lodhi', balance=100)
# satyam.withdraw(105)
# print(satyam.transaction_id)
# print(Account.result)
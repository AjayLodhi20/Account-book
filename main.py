import datetime as dt
from datetime import timezone
import random

class Account:
    current_time = dt.datetime.now(timezone.utc)


    def __init__(self, account_no, first_name, last_name, offset, balance):
        self.account_no = account_no
        self._first_name = first_name
        self._last_name = last_name
        self. tz_offset = offset
        self.balance = balance
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



id1 = Account(1234, 'ajay', 'lodhi', 7, 100)
print(id1.first_name)
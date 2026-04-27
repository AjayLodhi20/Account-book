import datetime as dt
from datetime import timezone
import random

class Account:
    current_time = dt.datetime.now(timezone.utc)


    def __init__(self, account_no, first_name, last_name, offset, balance):
        self.account_no = account_no
        self._first_name = first_name
        self.last_name = last_name
        self. tz_offset = offset
        self.balance = balance
    @property
    def first_name(self):
        self._first_name
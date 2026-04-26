import datetime as dt
from datetime import timezone
import random

class Account:
    current_time = dt.datetime.now(timezone.utc)

    def __init__(self, ):
        account_no = self.account_number()

    def account_number(self):
        number = '1234567890'
        new_list = list(number)
        random.shuffle(new_list)
        account_no = new_list

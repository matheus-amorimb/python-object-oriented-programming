import itertools
import numbers
import types
from collections import namedtuple
from datetime import datetime, timedelta, timezone

from .TimeZone import TimeZone


class BankAccount:
    _transaction_codes = {
        'deposit': 'D',
        'withdraw': 'W',
        'interest': 'I',
        'rejected': 'X',
    }

    _interest_rate = 0.5   # percentage

    _transaction_id = itertools.count(1)

    def __init__(
        self, id, first_name, last_name, timezone=None, initial_balance=0
    ):
        self.account_number = id
        self.first_name = first_name
        self.last_name = last_name
        self._full_name = f'{first_name} {last_name}'
        self._balance = float(initial_balance)

        if timezone is None:
            timezone = TimeZone('UTC', 0)
        self.timezone = timezone

    @property
    def account_number(self):
        return self._account_number

    @account_number.setter
    def account_number(self, value):
        self._account_number = BankAccount.check_id(value)

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        self._first_name = BankAccount.check_name(first_name, 'First Name')

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        self._last_name = BankAccount.check_name(last_name, 'Last Name')

    @property
    def full_name(self):
        self._full_name = self.first_name + ' ' + self.last_name
        return self._full_name

    @property
    def timezone(self):
        return self._timezone

    @timezone.setter
    def timezone(self, value):
        if not isinstance(value, TimeZone):
            raise ValueError('Time zone must be a valid TimeZone object.')
        self._timezone = value

    @classmethod
    def get_interest_rate(cls):
        return cls._interest_rate

    @classmethod
    def set_interest_rate(cls, value):
        if not isinstance(value, numbers.Real):
            raise ValueError('Interest rate must be a real number.')
        if value < 0:
            raise ValueError('Interest rate cannot be negative.')
        cls._interest_rate = value

    @property
    def balance(self):
        return round(self._balance, 2)

    @staticmethod
    def is_string(value):
        if not isinstance(value, str):
            raise ValueError(
                f'Name must be passed as string. It was passed a {type(value).__name__}.'
            )
        return value

    @staticmethod
    def check_name(value, field_name):
        value = BankAccount.is_string(value)
        if not value.isalpha():
            raise ValueError(
                f'{field_name} must contain only letters and cannot be empty.'
            )
        return value

    @staticmethod
    def check_id(value):
        value = BankAccount.is_string(value)
        if not value.isdigit():
            raise ValueError('ID must contain only numbers.')
        return value

    def generate_confirmation_code(self, transaction_type):
        counter = next(BankAccount._transaction_id)

        utc_time = datetime.now(timezone.utc)
        preferred_time_zone = utc_time + self.timezone.offset

        confirmation_code = f"{transaction_type}-{self.account_number}-{preferred_time_zone.strftime('%Y%m%d%H%M')}-{self.timezone.name}-{counter}"

        return confirmation_code

    @staticmethod
    def parse_confirmation_code(confirmation_code, preferred_time_zone=None):
        Confirmation = namedtuple(
            'Confirmation',
            [
                'transaction_code',
                'account_number',
                'time',
                'time_utc',
                'transaction_id',
            ],
        )

        parts = confirmation_code.split('-')

        if len(parts) != 5:
            raise ValueError('Invalid confirmation code')

        (
            transaction_code,
            account_number,
            time,
            timezone,
            transaction_id,
        ) = parts

        if preferred_time_zone is None:
            preferred_time_zone = TimeZone('UTC', 0)

        if not isinstance(preferred_time_zone, TimeZone):
            raise ValueError('Time zone must be a valid TimeZone object.')

        preferred_time_str = f"{datetime.strptime(time,'%Y%m%d%H%M').strftime('%Y-%m-%d %H:%M:%S')} ({preferred_time_zone.name})"

        time_utc = (
            datetime.strptime(time, '%Y%m%d%H%M') - preferred_time_zone.offset
        )
        time_utc_str = time_utc.strftime('%Y-%m-%d %H:%M:%S')

        return Confirmation(
            transaction_code,
            account_number,
            preferred_time_str,
            time_utc_str,
            transaction_id,
        )

    @staticmethod
    def validate_value(value, min_value=0):
        if not isinstance(value, (int, float)):
            raise ValueError('Deposit value must be a real number')
        if value < min_value:
            raise ValueError(f'Deposit value must be at least {min_value}.')
        return value

    def deposit(self, value):
        value = BankAccount.validate_value(value, min_value=0.1)
        type_transaction = BankAccount._transaction_codes['deposit']
        conf_code = self.generate_confirmation_code(type_transaction)
        self._balance += value
        return f'Operation {conf_code} completed successfully \n Balance available: {self.balance}.'

    def withdraw(self, value):
        value = BankAccount.validate_value(value)
        if self.balance < value:
            type_transaction = BankAccount._transaction_codes['rejected']
        else:
            type_transaction = BankAccount._transaction_codes['withdraw']
            self._balance -= value

        conf_code = self.generate_confirmation_code(type_transaction)
        return f'Operation {conf_code} completed successfully \n Balance available: {self.balance}.'

    def apply_interest(self):
        interest = (self._balance) * (BankAccount.get_interest_rate() / 100)
        conf_code = self.generate_confirmation_code(
            BankAccount._transaction_codes['interest']
        )
        self._balance += interest
        return f'Operation {conf_code} completed successfully \n Balance available: {self.balance}'


if __name__ == '__main__':
    pass

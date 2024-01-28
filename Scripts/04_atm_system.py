from enum import Enum
from datetime import datetime

class ATMState(Enum):
    IDLE = 'idle'
    BUSY = 'busy'


class User:
    def __init__(self, atm_card: 'ATMCard', bank_account: 'BankAccount'):
        self.__atm_card = atm_card
        self.__bank_account = bank_account


class ATMCard:
    def __init__(self, holder_name: str, card_number: str, card_pin: str, exp_date: datetime):
        self.__holder_name = holder_name
        self.__card_number = card_number
        self.__card_pin = card_pin
        self.__exp_date = exp_date

    def get_pin(self):
        return self.__card_pin


class BankAccount:
    def __init__(self, account_num: str, routing_num: str, balance: float):
        self.__account_num = account_num
        self.__routing_num = routing_num
        self.__balance = balance

    def get_account_num(self):
        return self.__account_num

    def get_balance(self):
        return self.__balance


class Bank:
    def __init__(self):
        self.__accounts = {}  # a bank may have multiple accounts

    def add_account(self, account_num: int, account: 'BankAccount'):
        self.__accounts.update({account_num: account})

    def get_account(self, account_num: int):
        return self.__accounts.get(account_num)


class ATM:
    def __init__(self):
        self.__state = ATMState.IDLE
        self.__card = None

    def insert_card(self, atm_card: 'ATMCard'):
        if self.__state == ATMState.IDLE:
            print('Card is inserted. Please enter your PIN.')
            self.__state = ATMState.BUSY
            self.__card = atm_card
        else:
            print('ATM is busy. Please try again later.')

    def request_pin(self, pin: str):
        if self.__card is None:
            print('No card is inserted. Please insert the card first.')
        else:
            if pin == self.__card.get_pin():
                print('Correct PIN. Access granted.')
            else:
                print('Incorrect PIN. Please try again.')

    def eject_card(self):
        print('Card is ejected.')
        self.__state = ATMState.IDLE


if __name__ == '__main__':
    # create a bank account
    my_account = BankAccount(account_num='123456', routing_num='222333', balance=1000)
    my_bank = Bank()
    my_bank.add_account(my_account.get_account_num(), my_account)
    my_atm_card = ATMCard(holder_name='zhang san', card_number='123123', card_pin='000000', exp_date=datetime(2030, 12, 31))
    # create an ATM
    my_atm = ATM()

    # the ATM accepts the card
    my_atm.insert_card(my_atm_card)
    my_atm.request_pin(pin='000111')
    my_atm.request_pin(pin='000000')

    # remove the card
    my_atm.eject_card()
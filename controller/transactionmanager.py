from model.transactionquery import TransactionQuery
from data_access.account_data_access import DataAccess
import re
from datetime import datetime
from model.transactionexception import TransactionException

class TransactionManager():
    def __init__(self):
        self.query = TransactionQuery()
        self.data_access = DataAccess()
        self.balance_emitter = 0
        self.balance_receiver = 0
        self.ERROR_MESSAGEEEE = None

    
    def __check_date(self, deal_date):
        current_time_object = datetime.now().date()
        if deal_date < current_time_object:
            error_message = "Vous ne pouvez pas faire une transaction dans le passé"
            raise TransactionException(error_message)

    def __get_account_number_from_email(self, email): #transaction_info.receiver
        account_number = self.data_access.get_account_number_from_email(email)
        if account_number != 'Null':
            return account_number[0]
        else:
            return False
        
    def __manage_entry_for_transfer(self, transaction_info):
        transaction_info.set_receiver(self.__get_account_number_from_email(transaction_info.get_receiver()))

        if transaction_info.get_receiver() == transaction_info.get_emitter():
            error_message = "Vous ne pouvez pas faire de transfert sur le même compte"
            raise TransactionException(error_message)
            # print("Vous ne pouvez pas faire de transfert sur le même compte")

        self.balance_emitter = self.data_access.get_balance_from_account(transaction_info.get_emitter())
        self.balance_receiver = self.data_access.get_balance_from_account(transaction_info.get_receiver())

        # transaction_info.amount = self.__convert_amount(transaction_info.amount)
        transaction_info.set_amount(self.__convert_amount(transaction_info.get_amount()))

        if transaction_info.get_amount() == False:
            error_message = "Vous devez entrer un montant en chiffre"
            raise TransactionException(error_message)

    def __manage_entry_for_withdrawal(self, transaction_info): #emitter and no receiver
        self.balance_emitter = self.data_access.get_balance_from_account(transaction_info.get_emitter()) #convert balance into float
        # transaction_info.amount = self.__convert_amount(transaction_info.amount)

        transaction_info.set_amount(self.__convert_amount(transaction_info.get_amount()))
        print(transaction_info.get_amount())
        if transaction_info.get_amount() == False:
            error_message = "Vous devez entrer un montant en chiffre"
            raise TransactionException(error_message)
        
    def __manage_entry_for_deposit(self, transaction_info): #receiver and no emitter
        self.balance_receiver = self.data_access.get_balance_from_account(transaction_info.get_receiver())
        # transaction_info.amount = self.__convert_amount(transaction_info.amount)

        transaction_info.set_amount(self.__convert_amount(transaction_info.get_amount()))

        if transaction_info.get_amount() == False:
            error_message = "Vous devez entrer un montant en chiffre"
            raise TransactionException(error_message)

    def __convert_amount(self, amount):
        try:
            amount_regex = re.search("((\d)+.?(\d)+)", amount)
            final_amount = amount_regex.group()
            return float(final_amount)
        except:
            return False

    def manage_transaction(self, transaction_info):
        # check if transaction_info.amount > 0, else error !!! Regex already take care of it ???
        self.__check_date(transaction_info.date)

        print(f"TYPE EN DEBUT DE MANAGE TRANACTION {transaction_info.type}")

        if transaction_info.type == 'Transfert':     
            self.__manage_entry_for_transfer(transaction_info)
            self.query.transfer_transaction(transaction_info, self.balance_emitter, self.balance_receiver)

        elif transaction_info.type == 'Retrait':
            self.__manage_entry_for_withdrawal(transaction_info)
            self.query.withdrawal_transaction(transaction_info, self.balance_emitter)
        else:
            self.__manage_entry_for_deposit(transaction_info)
            self.query.deposit_transaction(transaction_info, self.balance_receiver)

    def manage_transfer(self, transaction_info):
        self.__manage_entry_for_transfer(transaction_info)
        self.query.transfer_transaction(transaction_info, self.balance_emitter, self.balance_receiver)

import re
from datetime import datetime
from model.customexception import TransactionException
from data_access.write_transactionquery import TransactionQuery
from data_access.read_data_access import DataAccess

class TransactionManager():
    def __init__(self):
        self.__query = TransactionQuery()
        self.__data_access = DataAccess()
        self.__balance_emitter = 0
        self.__balance_receiver = 0

    
    def __check_date(self, deal_date):
        current_time_object = datetime.now().date()
        if deal_date < current_time_object:
            error_message = "Vous ne pouvez pas faire une transaction dans le passé"
            raise TransactionException(error_message)

    def __get_account_number_from_email(self, email): #transaction_info.receiver
        account_number = self.__data_access.get_account_number_from_email(email)
        if account_number != 'Null':
            return account_number[0]
        else:
            return False
        
    def __manage_entry_for_transfer(self, transaction_info):
        transaction_info.set_receiver(self.__get_account_number_from_email(transaction_info.get_receiver()))

        if transaction_info.get_receiver() == transaction_info.get_emitter():
            error_message = "Vous ne pouvez pas faire de transfert sur le même compte"
            raise TransactionException(error_message)

        self.__balance_emitter = self.__data_access.get_balance_from_account(transaction_info.get_emitter())
        self.__balance_receiver = self.__data_access.get_balance_from_account(transaction_info.get_receiver())
        transaction_info.set_amount(self.__convert_amount(transaction_info.get_amount()))

        if transaction_info.get_amount() == False:
            error_message = "Vous devez entrer un montant en chiffre"
            raise TransactionException(error_message)

    def __manage_entry_for_withdrawal(self, transaction_info): #emitter and no receiver
        self.__balance_emitter = self.__data_access.get_balance_from_account(transaction_info.get_emitter()) #convert balance into float

        transaction_info.set_amount(self.__convert_amount(transaction_info.get_amount()))
        print(transaction_info.get_amount())
        if transaction_info.get_amount() == False:
            error_message = "Vous devez entrer un montant en chiffre"
            raise TransactionException(error_message)
        
    def __manage_entry_for_deposit(self, transaction_info): #receiver and no emitter
        self.__balance_receiver = self.__data_access.get_balance_from_account(transaction_info.get_receiver())

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
        
    def __manage_entry_self_transfer(self, transaction_info):
        receiver = transaction_info.get_receiver()
        transaction_info.set_receiver(self.__clean_receiver_data(receiver))

        if transaction_info.get_receiver() == transaction_info.get_emitter():
            error_message = "Vous ne pouvez pas faire de transfert sur le même compte"
            raise TransactionException(error_message)
        
        self.__balance_emitter = self.__data_access.get_balance_from_account(transaction_info.get_emitter())
        self.__balance_receiver = self.__data_access.get_balance_from_account(transaction_info.get_receiver())

        transaction_info.set_amount(self.__convert_amount(transaction_info.get_amount()))

        if transaction_info.get_amount() == False:
            error_message = "Vous devez entrer un montant en chiffre"
            raise TransactionException(error_message)

    def __clean_receiver_data(self, data_receiver):
        data = re.search("^(\[(\d)+\])", data_receiver)
        account_id = re.search("(\d)+", data.group())
        final_account_id = account_id.group()
        print(final_account_id)
        return int(final_account_id)
        
    def manage_transaction(self, transaction_info):
        self.__check_date(transaction_info.get_date())
        print(transaction_info.get_receiver())

        print(f"TYPE EN DEBUT DE MANAGE TRANACTION {transaction_info.get_type()}")

        if transaction_info.get_type() == 'Virement':     
            self.__manage_entry_for_transfer(transaction_info)
            self.__query.transfer_transaction(transaction_info, self.__balance_emitter, self.__balance_receiver)

        elif transaction_info.get_type() == 'Transfert':
            self.__manage_entry_self_transfer(transaction_info)
            self.__query.transfer_transaction(transaction_info, self.__balance_emitter, self.__balance_receiver)

            
        elif transaction_info.get_type() == 'Retrait':
            self.__manage_entry_for_withdrawal(transaction_info)
            self.__query.withdrawal_transaction(transaction_info, self.__balance_emitter)
        else:
            self.__manage_entry_for_deposit(transaction_info)
            self.__query.deposit_transaction(transaction_info, self.__balance_receiver)

    def manage_transfer(self, transaction_info):
        self.__manage_entry_for_transfer(transaction_info)
        self.__query.transfer_transaction(transaction_info, self.__balance_emitter, self.__balance_receiver)

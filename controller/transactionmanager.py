# from view.transactions import TransactionView
from model.transactionquery import TransactionQuery
from data_access.account_data_access import DataAccess
import re
from datetime import datetime

class TransactionManager():
    def __init__(self):
        self.query = TransactionQuery()
        self.data_access = DataAccess()
        self.balance_emitter = 0
        self.balance_receiver = 0
        self.error_message = ""
        # self.view = TransactionView(window_title, column_number, current_session)
        # self.view.screen_build()
    
    def __check_date(self, deal_date):
        # deal_date_string = deal_date.split("-")
        deal_date_string = deal_date.strftime('%Y-%m-%d')
        deal_date_string = deal_date_string.split("-")

        year = int(deal_date_string[0])
        month = int(deal_date_string[1])
        day = int(deal_date_string[2])

        # current_time = datetime.now().strftime('%Y-%m-%d')
        # current_time = current_time.split("-")

        current_time_object = datetime.now() # current date and time

        current_time = current_time_object.strftime("%y-%m-%d").split("-")

        if year < int(current_time[0]):
            return "Vous ne pouvez pas faire une transaction dans le passé"
        else:
            if month < int(current_time[1]):
                return "Vous ne pouvez pas faire une transaction dans le passé"
            else:
                if day < int(current_time[2]):
                    return "Vous ne pouvez pas faire une transaction dans le passé"

    def __get_account_number_from_email(self, email): #transaction_info.receiver
        account_number = self.data_access.get_account_number_from_email(email)
        if account_number != 'Null':
            return account_number[0]
        else:
            return False
        
    def __manage_entry_for_transfer(self, transaction_info):
        transaction_info.receiver = self.__get_account_number_from_email(transaction_info.receiver)

        if transaction_info.receiver == transaction_info.emitter:
            self.error_message = "Vous ne pouvez pas faire de transfert sur le même compte"
            # print("Vous ne pouvez pas faire de transfert sur le même compte")
            return

        self.balance_emitter = self.data_access.get_balance_from_account(transaction_info.emitter)
        self.balance_receiver = self.data_access.get_balance_from_account(transaction_info.receiver)

        transaction_info.amount = self.__convert_amount(transaction_info.amount)
        if transaction_info.amount == False:
            self.error_message = "Vous devez entrer un montant en chiffre"
            # print("Vous devez entrer un montant en chiffre")
            return 


    def __manage_entry_for_withdrawal(self, transaction_info): #emitter and no receiver
        
        print(f"emetteur : {transaction_info.emitter}")
        self.balance_emitter = self.data_access.get_balance_from_account(transaction_info.emitter) #convert balance into float
        transaction_info.amount = self.__convert_amount(transaction_info.amount)
        if transaction_info.amount == False:
            self.error_message = "Vous devez entrer un montant en chiffre"
            # print("Vous devez entrer un montant en chiffre")
            return
        
    def __manage_entry_for_deposit(self, transaction_info): #receiver and no emitter
        self.balance_receiver = self.data_access.get_balance_from_account(transaction_info.receiver)
        transaction_info.amount = self.__convert_amount(transaction_info.amount)
        if transaction_info.amount == False:
            self.error_message = "Vous devez entrer un montant en chiffre"
            # print("Vous devez entrer un montant en chiffre")
            return


    # def __get_account_number_email(self, cursor, email):
    #     cursor.execute("SELECT MIN(id_account) FROM Bank_account " +
    #                     "JOIN Users u USING(id_user) " +
    #                     f"WHERE u.email = '{email}';")           
    #     return cursor.fetchone()

    def __convert_amount(self, amount):
        try:
            # is_not_digital = re.search("[^((\d)+.?(\d)+)]", amount)
            amount_regex = re.search("((\d)+.?(\d)+)", amount)
            final_amount = amount_regex.group()
            return float(final_amount)
        except:
            return False
    
    def __convert_date(self):
        pass
    # def __manage_deposit(self, transaction_info):
    #     pass

    # def __manage_withdrawal(self, transaction_info):
    #     pass
    
    # def __manage_transfer(self, transaction_info):
    #     pass

    def manage_transaction(self, transaction_info):
        # check if transaction_info.amount > 0, else error !!! Regex already take care of it ???
        print(transaction_info.date)
        self.error_message = self.__check_date(transaction_info.date)
        print(f"TYPE EN DEBUT DE MANAGE TRANACTION {transaction_info.type}")
        if transaction_info.type == 'Transfert':     
            self.__manage_entry_for_transfer(transaction_info)
            if self.error_message == "":
                return self.query.transfer_transaction(transaction_info, self.balance_emitter, self.balance_receiver)
            else:
                return self.error_message
        elif transaction_info.type == 'Retrait':
            self.__manage_entry_for_withdrawal(transaction_info)
            if self.error_message == "":
                print(f"balance_emitter in manage transaction = {self.balance_emitter}")
                return self.query.withdrawal_transaction(transaction_info, self.balance_emitter)
            else:
                return self.error_message
        else:
            self.__manage_entry_for_deposit(transaction_info)
            if self.error_message == "":
                return self.query.deposit_transaction(transaction_info, self.balance_receiver)
            else:
                return self.error_message

    def manage_transfer(self, transaction_info):
        self.__manage_entry_for_transfer(transaction_info)
        if self.error_message == "":
            return self.query.transfer_transaction(transaction_info, self.balance_emitter, self.balance_receiver)
        else:
            return self.error_message

    def run(self):
        # self.manage_transfer()
        self.view.mainloop()
        

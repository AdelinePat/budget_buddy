# from view.transactions import TransactionView
from model.transactionquery import TransactionQuery
from data_access.account_data_access import DataAccess
import re

class TransactionManager():
    def __init__(self):
        self.query = TransactionQuery()
        self.data_access = DataAccess()
        self.balance_emitter = 0
        self.balance_receiver = 0
        self.error_message = ""
        # self.view = TransactionView(window_title, column_number, current_session)
        # self.view.screen_build()
    
    def manage_deposit(self):
        if self.view.receiver == self.view.current_session:
            self.query.method_inexistant()
    
    def manage_withdrawal(self):
        pass
    
    def __get_account_number_from_email(self, email): #transaction_info.receiver
        account_number = self.data_access.get_account_number_from_email(email)
        if account_number != 'Null':
            return account_number[0]
        else:
            return False
        
    def __manage_entry(self, transaction_info):
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
    
      

        

    

    def manage_transfer(self, transaction_info):
        self.__manage_entry(transaction_info)
        if self.error_message == "":
            return self.query.transfer_transaction(transaction_info, self.balance_emitter, self.balance_receiver)
        else:
            return self.error_message

    def run(self):
        # self.manage_transfer()
        self.view.mainloop()
        

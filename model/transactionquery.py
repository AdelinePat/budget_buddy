# from view.transactions import TransactionView
from model.server import ServerDatabase
import re

# CURRENT SESSION = id_user

class TransactionQuery():
    def __init__(self):
        self.database = ServerDatabase()

    def __is_balance_valid(self, final_balance):
        if final_balance >= 0:
            return True
        else:
            return False
        
    def __update_balance_query(self, id_account, new_balance):
        database = self.database.database_connection()

        if database.is_connected():
            cursor = database.cursor()
            deposit_query = f"UPDATE Bank_account SET balance = {new_balance} WHERE id_account = {id_account};"
            cursor.execute(deposit_query)
            database.commit()
            cursor.close()
        database.close()

    def transfer_transaction(self, transaction_info, balance_emitter, balance_receiver):
        # check if email exist => use main account for transfert
        # check if amount < balance¨+ check if balance - amount < 0

        final_balance = balance_emitter - transaction_info.amount

        if self.__is_balance_valid(final_balance):
            self.__update_balance_query(transaction_info.emitter, final_balance)
            receiver_balance = balance_receiver + transaction_info.amount
            self.__update_balance_query(transaction_info.receiver, receiver_balance)
        else:
            return "Vous ne pouvez pas faire une transaction qui vous mettra à découvert."

        
        # database = self.database.database_connection()

        # if database.is_connected():
        #     cursor = database.cursor()
        #     receiver_account_number = self.__get_account_number(cursor, transaction_info.receiver)
        #     print(f"compte récepteur : n° {receiver_account_number}")
        #     print(type(receiver_account_number))

        #     if self.__is_account(receiver_account_number):
        #         balance = self.__get_balance_from_user(cursor, transaction_info.current_session)
        #         print(f"balance = {balance} €")

        #         if bool(self.__convert_amount(transaction_info.amount)) == True:
        #             transaction_info.amount = self.__convert_amount(transaction_info.amount)
        #             final_balance = float(balance) - transaction_info.amount

        #             if self.__is_balance_valid(final_balance):
        #                 self.__update_balance_query(cursor, transaction_info.current_session, final_balance)
        #                 # print(f"après la transaction : {final_balance}")
        #                 # cursor.close()
        #                 # cursor = database.cursor()

        #                 receiver_balance = self.__get_balance_from_account(cursor, receiver_account_number)
        #                 new_receiver_balance = float(receiver_balance) + transaction_info.amount
        #                 self.__update_balance_query(cursor, receiver_account_number, new_receiver_balance)
        #                 database.commit()
        #                 # cursor.execute()
        #                 print("transaction réussie")
        #             else:
        #                 print("Vous ne pouvez pas faire une transaction qui vous mettra à découvert.")
        #                 return "Vous ne pouvez pas faire une transaction qui vous mettra à découvert."
        #         else:
        #             print("Vous devez entrer un montant en chiffre")
        #             return "Vous devez entrer un montant en chiffre"
                
        #     cursor.close()
        # database.close()
             

            

            


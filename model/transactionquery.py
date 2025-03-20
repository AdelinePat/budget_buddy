# from view.transactions import TransactionView
from model.server import ServerDatabase
import re

class TransactionQuery():
    def __init__(self):
        self.database = ServerDatabase()

    def is_account(self, email_receiver):
        if email_receiver == "NULL":
            return False
        else:
            return True
            
    def get_email(self, cursor, account):
        cursor.execute("SELECT MIN(id_account) FROM bank_account "
                        "JOIN Users u USING(id_user) "
                        f"WHERE u.email = '{account}';")           
        return cursor.fetchone()[0]

    def get_balance(self, cursor, current_session):
        cursor.execute("SELECT balance FROM bank_account "
                    "JOIN Users u USING(id_user) "
                    f"WHERE id_account = (SELECT MIN(id_account) FROM bank_account WHERE id_user = {current_session});")
        return cursor.fetchone()[0]
    
    # def check_balance(self, final_balance, balance, amount):
    #     final_balance = balance - amount
    #     if final_balance < 0:
    #         return final_balance
    #     else:
    #         return "Vous ne pouvez pas faire une transaction qui vous mettra à découvert."
    def convert_amount(self, amount):
        amount_regex = re.search("((\d)+.?(\d)+)", amount)
        print(f"amount_regex : {amount_regex.group(0)}")
        if float(amount_regex.group(0)) == True:
            return float(amount_regex.group(0))
        else:
            return None

    # def is_amount_input_valid(self, amount):
    #     print(f"amount in is_amount_input_valid = {amount}")
    #     amount_regex = self.convert_amount(amount)
    #     if amount_regex != None:
    #         # if type(amount) is not int or type(amount) is not float:
    #         if float(amount_regex):
    #             return True
    #             #"Vous devez entrer un montant en chiffre"
    #         else:
    #             return False

    def is_balance_valid(self, final_balance):
        if final_balance >= 0:
            return True
        else:
            return False

    def transfer_transaction(self, current_session, email_account, amount):
        # check if email exist => use main account for transfert
        # check if amount < balance¨+ check if balance - amount < 0

        database = self.database.database_connection()

        if database.is_connected():
            cursor = database.cursor()
            receiver_account_number = self.get_email(cursor, email_account)
            print(f"compte récepteur : n° {receiver_account_number}")
            if self.is_account(receiver_account_number):
                balance = self.get_balance(cursor, current_session)
                print(f"balance = {balance} €")
                if self.convert_amount(amount) != None:
                    amount = self.convert_amount(amount)
                    final_balance = float(balance) - amount
                    print(f"après la transaction : {final_balance}")
                    if self.is_balance_valid(final_balance):
                        # cursor = database.cursor()
                        # cursor.execute()
                        print("transaction réussie")
                    else:
                        print("Vous ne pouvez pas faire une transaction qui vous mettra à découvert.")
                        return "Vous ne pouvez pas faire une transaction qui vous mettra à découvert."
                else:
                    print("Vous devez entrer un montant en chiffre")
                    return "Vous devez entrer un montant en chiffre"
                
            cursor.close()
        database.close()
             

            

            


from model.server import ServerDatabase
from model.customexception import TransactionException

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
            deposit_query = "UPDATE Bank_account SET balance = %(balance)s WHERE id_account = %(id_account)s;"

            values = {
                'balance' : new_balance,
                'id_account' : id_account
            }
            
            cursor.execute(deposit_query, values)

            result = cursor.fetchone()
            print(f"RESULTAT UPDATE BALANCE {result}")
   
            database.commit()
            cursor.close()
        database.close()
    
    def __insert_transactions(self, transaction_info):
        database = self.database.database_connection()

        if database.is_connected():
            cursor = database.cursor()
            query = """INSERT INTO Transactions 
            (id_account_emitter, id_account_receiver,
            deal_description, amount, 
            deal_date, deal_type, 
            category) 
            VALUES (%(emitter)s, %(receiver)s,
            %(description)s, %(amount)s,
            %(date)s, %(type)s,
            %(category)s);"""

            values = {'emitter' : transaction_info.get_emitter(),
                      'receiver' : transaction_info.get_receiver(),
                      'description' : transaction_info.get_description(),
                      'amount' : transaction_info.get_amount(),
                      'date': transaction_info.get_date(),
                      'type' : transaction_info.get_type(),
                      'category' : transaction_info.get_category()}

            cursor.execute(query, values)

            result = cursor.fetchone()
            print(f"RESULTAT INSERT TRANSACTION {result}")
   
            database.commit()
            cursor.close()
        database.close()
    
    def withdrawal_transaction(self, transaction_info, balance_emitter):
        final_balance = balance_emitter - transaction_info.get_amount()
        if self.__is_balance_valid(final_balance):
            self.__update_balance_query(transaction_info.get_emitter(), final_balance)
            self.__insert_transactions(transaction_info)
            print("Le retrait a été effecuté avec succès")
        else:
            error_message = "Vous ne pouvez pas faire une transaction qui vous mettra à découvert."
            raise TransactionException(error_message)
        
    def deposit_transaction(self, transaction_info, balance_receiver):
        final_balance = balance_receiver + transaction_info.get_amount()

        self.__update_balance_query(transaction_info.get_receiver(), final_balance)
        self.__insert_transactions(transaction_info)
        print("Le dépôt a été effecuté avec succès")

    def transfer_transaction(self, transaction_info, balance_emitter, balance_receiver):
        final_balance = balance_emitter - transaction_info.get_amount()

        if self.__is_balance_valid(final_balance):
            self.__update_balance_query(transaction_info.get_emitter(), final_balance)
            receiver_balance = balance_receiver + transaction_info.get_amount()
            self.__update_balance_query(transaction_info.get_receiver(), receiver_balance)
            self.__insert_transactions(transaction_info)
            print("Transfert réussie")
        else:
            error_message = "Vous ne pouvez pas faire une transaction qui vous mettra à découvert."
            raise TransactionException(error_message)
            

            


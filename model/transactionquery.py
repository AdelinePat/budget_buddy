from model.server import ServerDatabase

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
    
    def __insert_transactions(self, transaction_info):
        database = self.database.database_connection()
        print(transaction_info.date)

        if database.is_connected():
            cursor = database.cursor()
            query = """INSERT INTO Transactions
            (id_account_emitter, id_account_receiver,
            deal_description, amount, 
            deal_date, deal_type, 
            category)
            VALUES (%s, %s,
            %s, %s,
            %s, %s,
            %s);"""

            values = (transaction_info.emitter, transaction_info.receiver,
                      transaction_info.description, transaction_info.amount,
                      transaction_info.date, transaction_info.type,
                      transaction_info.category)

            cursor.execute(query, values)
   
            database.commit()
            cursor.close()
        database.close()
    
    def withdrawal_transaction(self, transaction_info, balance_emitter):
        print(f"amount : {transaction_info.amount}")
        print(f"balance_emitter = {balance_emitter}")
        final_balance = balance_emitter - transaction_info.amount
        print(f"final balance = {final_balance}")

        if self.__is_balance_valid(final_balance):
            self.__update_balance_query(transaction_info.emitter, final_balance)
            self.__insert_transactions(transaction_info)
        else:
            return "Vous ne pouvez pas faire une transaction qui vous mettra à découvert."
        
    def deposit_transaction(self, transaction_info, balance_receiver):
        final_balance = balance_receiver + transaction_info.amount

        self.__update_balance_query(transaction_info.receiver, final_balance)
        self.__insert_transactions(transaction_info)

    def transfer_transaction(self, transaction_info, balance_emitter, balance_receiver):
        final_balance = balance_emitter - transaction_info.amount

        if self.__is_balance_valid(final_balance):
            self.__update_balance_query(transaction_info.emitter, final_balance)
            receiver_balance = balance_receiver + transaction_info.amount
            self.__update_balance_query(transaction_info.receiver, receiver_balance)
            self.__insert_transactions(transaction_info)
            print("transactions réussie")
        else:
            return "Vous ne pouvez pas faire une transaction qui vous mettra à découvert."
            

            


from model.server import ServerDatabase
from model.customexception import TransactionException

class DataAccess():
    def __init__(self):
        self.database = ServerDatabase()

    def get_account_number_from_email(self, email):
        if email == None or email == "":
            error_message = "Vous devez remplir le champ email"
            raise TransactionException(error_message)
        
        database = self.database.database_connection()

        if database.is_connected():
            cursor = database.cursor()
            query = """SELECT MIN(id_account) FROM Bank_account
                        JOIN Users u USING(id_user) 
                        WHERE u.email = %s;"""

            cursor.execute(query, (email,))

            account = cursor.fetchone()
            cursor.close()
        database.close()     
        
        return account

    def get_account_number_from_id(self, client_id):

        if client_id == None or type(client_id) != int:
            error_message = "L'identifiant client n'est pas valide"
            raise TransactionException(error_message)
        
        database = self.database.database_connection()

        if database.is_connected():
            cursor = database.cursor()
            query = """SELECT MIN(id_account) FROM Bank_account
                    JOIN Users u USING(id_user)
                    WHERE u.id_user = %s;"""
            
            cursor.execute(query, (client_id,))
            
            account = cursor.fetchone()
            cursor.close()
        database.close()
        return account   
   
    def get_balance_from_main_user_account(self, user_id): 
        if user_id == None or type(user_id) != int:
            error_message = "L'identifiant client n'est pas valide"
            raise TransactionException(error_message)
        
        database = self.database.database_connection()

        if database.is_connected():
            cursor = database.cursor()
            query = """SELECT balance FROM Bank_account
                    JOIN Users u USING(id_user)
                    WHERE id_account = (SELECT MIN(id_account)
                    FROM Bank_account WHERE id_user = %s);"""
            
            cursor.execute(query, (user_id,))
            balance = float(cursor.fetchone()[0])
            cursor.close()
        database.close()
        return balance
    
    def get_balance_from_account(self, account_id):

        if account_id == None or type(account_id) != int:
            error_message = "L'identifiant du compte bancaire n'est pas valide"
            raise TransactionException(error_message)
        
        database = self.database.database_connection()

        if database.is_connected():
            cursor = database.cursor()
            balance_query = "SELECT balance FROM Bank_account WHERE id_account = %s;"

            cursor.execute(balance_query, (account_id, ))
            balance = float(cursor.fetchone()[0])
            cursor.close()
        database.close()
        return balance
    
    def get_all_accounts_from_user(self, user_id):
        if user_id == None or type(user_id) != int:
            error_message = "L'identifiant du compte bancaire n'est pas valide"
            raise TransactionException(error_message)
        
        database = self.database.database_connection()

        if database.is_connected():
            cursor = database.cursor()
            accounts_query = "SELECT id_account, account_type FROM Bank_account WHERE id_user =%s;"

            cursor.execute(accounts_query, (user_id, ))
            accounts = cursor.fetchall()
            cursor.close()
        database.close()
        return accounts
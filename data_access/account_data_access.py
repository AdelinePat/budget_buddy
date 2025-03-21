from model.server import ServerDatabase

class DataAccess():
    def __init__(self):
        self.database = ServerDatabase()

    def get_account_number_from_email(self, email):
        database = self.database.database_connection()

        if database.is_connected():
            cursor = database.cursor()
            cursor.execute("SELECT MIN(id_account) FROM Bank_account " +
                            "JOIN Users u USING(id_user) " +
                            f"WHERE u.email = '{email}';")
            
            account = cursor.fetchone()
            cursor.close()
        database.close()     
        
        return account

    def get_account_number_from_id(self, client_id):
        database = self.database.database_connection()

        if database.is_connected():
            cursor = database.cursor()
            cursor.execute("SELECT MIN(id_account) FROM Bank_account " +
                        "JOIN Users u USING(id_user) " +
                        f"WHERE u.id_user = {client_id}")
            
            account = cursor.fetchone()
            cursor.close()
        database.close()
        return account   

    def get_balance_from_user(self, current_session):
        #TODO update this method, when session object exist, current account number will be known and this method will become useless
        # print(type(current_session))
        database = self.database.database_connection()

        if database.is_connected():
            cursor = database.cursor()
            cursor.execute("SELECT balance FROM Bank_account " +
                            "JOIN Users u USING(id_user) " +
                            "WHERE id_account = (SELECT MIN(id_account) " +
                            f"FROM Bank_account WHERE id_user = {current_session});")
            balance = float(cursor.fetchone()[0])
            cursor.close()
        database.close()
        return balance   
    
    def get_balance_from_account(self, account_id):
        database = self.database.database_connection()

        if database.is_connected():
            cursor = database.cursor()
            balance_query = f"SELECT balance FROM Bank_account WHERE id_account = {account_id};"
            cursor.execute(balance_query)

            balance = float(cursor.fetchone()[0])
            cursor.close()
        database.close()
        return balance   
    

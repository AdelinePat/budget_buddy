from model.server import ServerDatabase

class HistoricQuery():
    def __init__(self):
        self.database = ServerDatabase()
        # self.show_all = self.get_historic_all_account( account_id, user_id)
        # self.show_by_categoy = self.historic_query_category(account_id, category)
        # self.show_by_type = se


        self.historic_queries_dict : dict = {
            "Voir tout" : self.historic_query_all,
            "Par catégorie" : self.historic_query_category,
            "Par type" : self.historic_query_type,
            "Par dates" : self.historic_query_dates,
        }

    def historic_query_all(self, user_id, account_id, category) -> list:
        if account_id == '0':
            return self.get_historic_all_account(user_id)
        else:
            return self.get_historic_account(account_id)

    def get_historic_all_account(self, user_id):
        database = self.database.database_connection()

        if database.is_connected():
            cursor = database.cursor()
            accounts_query = """
                SELECT t.deal_description, t.amount, t.deal_date, t.category
                FROM Transactions as t
                INNER JOIN Bank_account as emitter ON t.id_account_emitter = emitter.id_account
                INNER JOIN Bank_account as receiver ON t.id_account_receiver = receiver.id_account
                WHERE emitter.id_user =%s
                OR receiver.id_user =%s;"""
               
            cursor.execute(accounts_query, (user_id, user_id))
            print(accounts_query, user_id)

            accounts = cursor.fetchall()
            cursor.close()
        database.close()
        return accounts
        
    def get_historic_account(self, account_id):
        database = self.database.database_connection()

        if database.is_connected():
            cursor = database.cursor()
            accounts_query = """SELECT deal_description, amount, deal_date, category 
            FROM Transactions 
            WHERE id_account_emitter =%s or id_account_receiver =%s;
            """
               
            cursor.execute(accounts_query, (account_id, account_id))
            accounts = cursor.fetchall()
            cursor.close()
        database.close()

        return accounts

    def historic_query_category(self, user_id, account_id, category) -> list:
        if account_id == '0':
            return self.historic_all_category(user_id, category)
        else:
            return self.historic_by_category(account_id, category)
    
    def historic_all_category(self, user_id, category):
        database = self.database.database_connection()
            
        if database.is_connected():
            cursor = database.cursor()
            accounts_query = """
                SELECT t.deal_description, t.amount, t.deal_date, t.category
                FROM Transactions as t
                INNER JOIN Bank_account as emitter ON t.id_account_emitter = emitter.id_account
                INNER JOIN Bank_account as receiver ON t.id_account_receiver = receiver.id_account
                WHERE (emitter.id_user =%s
                OR receiver.id_user =%s) and category =%s;""" 
            cursor.execute(accounts_query, (user_id, user_id, category))
            accounts = cursor.fetchall()
            print(accounts_query, user_id, category)
            print(accounts)

            cursor.close()
        database.close()
        return accounts

    def historic_by_category(self, account_id, category):
        database = self.database.database_connection()

        if database.is_connected():
            cursor = database.cursor()
            accounts_query = """
                SELECT deal_description, amount, deal_date, category 
                FROM Transactions 
                WHERE (id_account_emitter =%s or id_account_receiver =%s)
                and category =%s;"""
            cursor.execute(accounts_query, (account_id, account_id, category))
            accounts = cursor.fetchall()
            cursor.close()
        database.close()
        return accounts


    def historic_query_type(self, user_id, account_id, deal_type) -> list:
        if account_id == '0':
            return self.historic_all_type(user_id, deal_type)
        else:
            return self.historic_by_type(account_id, deal_type)

    def historic_all_type(self, id_user, deal_type): 
        database = self.database.database_connection()

        if database.is_connected():
            cursor = database.cursor()
            accounts_query = """
                SELECT t.deal_description, t.amount, t.deal_date, t.category
                FROM Transactions as t
                INNER JOIN Bank_account as emitter ON t.id_account_emitter = emitter.id_account
                INNER JOIN Bank_account as receiver ON t.id_account_receiver = receiver.id_account
                WHERE (emitter.id_user =%s
                OR receiver.id_user =%s) and deal_type =%s;
                """
                
            cursor.execute(accounts_query, (id_user, id_user, deal_type))
            accounts = cursor.fetchall()
            cursor.close()
        database.close()
        return accounts

    def historic_by_type(self, account_id, deal_type):
        database = self.database.database_connection()

        if database.is_connected():
            cursor = database.cursor()
            accounts_query = """
                SELECT deal_description, amount, deal_date, category 
                FROM Transactions 
                WHERE (id_account_emitter =%s or id_account_receiver =%s)
                and deal_type =%s;
                """
            cursor.execute(accounts_query, (account_id, account_id, deal_type))
            accounts = cursor.fetchall()
            cursor.close()
        database.close()
        return accounts


    def historic_query_dates(self, account_id, **dates) -> list:
        database = self.database.database_connection()

        if database.is_connected():
            cursor = database.cursor()
            accounts_query = ("""
                SELECT t.deal_description, t.amount, t.deal_date, t.category
                FROM Transactions as t
                INNER JOIN Bank_account as emitter ON t.id_account_emitter = emitter.id_account
                INNER JOIN Bank_account as receiver ON t.id_account_receiver = receiver.id_account
                WHERE emitter.id_user =%s
                OR receiver.id_user =%s and category =%s;
                """ if account_id == 0 else """
                SELECT deal_description, amount, deal_date, category 
                FROM Transactions 
                WHERE id_account_emitter =%s or id_account_receiver =%s;
            """)
            cursor.execute(accounts_query, (account_id, account_id))
            accounts = cursor.fetchall()
            cursor.close()
        database.close()
        return accounts
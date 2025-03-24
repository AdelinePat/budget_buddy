from model.server import ServerDatabase

class HistoricQuery():
    def __init__(self):
        self.database = ServerDatabase()
        self.historic_queries_dict : dict = {
            "Voir tout" : self.historic_query_all,
            "Par catégorie" : self.historic_query_category,
            "Par type" : self.historic_query_type,
            "Par dates" : self.historic_query_dates,
        }

    def historic_query_all(self, account_id, none) -> list:
        database = self.database.database_connection()

        if database.is_connected():
            cursor = database.cursor()
            accounts_query = ("""
                SELECT t.deal_description, t.amount, t.deal_date, t.category
                FROM Transactions as t
                INNER JOIN Bank_account as emitter ON t.id_account_emitter = emitter.id_account
                INNER JOIN Bank_account as receiver ON t.id_account_receiver = receiver.id_account
                WHERE emitter.id_user =%s
                OR receiver.id_user =%s;
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
    
    def historic_query_category(self, account_id, category) -> list:
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
                WHERE id_account_emitter =%s or id_account_receiver =%s
                and category =%s;
            """)
            cursor.execute(accounts_query, (account_id, account_id, category))
            accounts = cursor.fetchall()
            cursor.close()
        database.close()
        return accounts

    def historic_query_type(self, account_id, type) -> list:
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
                WHERE id_account_emitter =%s or id_account_receiver =%s
                and deal_type =%s;
            """)
            cursor.execute(accounts_query, (account_id, account_id, type))
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
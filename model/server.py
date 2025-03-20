import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

class ServerDatabase():
    def __init__(self):
        self.password = os.getenv("PASS")
        self.user = os.getenv("USER")
        self.database_name = "budget_buddy"

        pass
    def server_connection(self):
        server = mysql.connector.connect(
            host="localhost",
            user= self.user,
            password= self.password
        )
        return server

    def database_connection(self):
        database_connection = mysql.connector.connect(
            host="localhost",
            user= self.user,
            password= self.password,
            database= self.database_name
        )
        return database_connection
    
# conn = object_server.database_connection()

    def create_database(self):
        server = self.server_connection()

        if server.is_connected():
            self.cursor = server.cursor()
            # self.cursor.execute(f"DROP DATABASE IF EXISTS {self.database_name};")
            self.cursor.execute("SHOW DATABASES;")
            databases = self.cursor.fetchall()
            all_data_bases = []
            for database in databases:
                all_data_bases.append(database[0])

            if self.database_name not in all_data_bases:
                self.cursor.execute(f"CREATE DATABASE {self.database_name};")
                self.cursor.execute(f"USE {self.database_name};")

                self.create_client_table()
                self.create_account_table()
                self.create_transactions_table()


            # self.cursor.execute(f"CREATE DATABASE IF NOT EXISTS {self.database_name};")
            # self.cursor.execute(f"USE {self.database_name};")

            self.cursor.close()
        server.close()
    
    def create_client_table(self):
        database = self.database_connection()
        if database.is_connected():
            self.cursor = database.cursor()
            self.cursor.execute("DROP TABLE IF EXISTS Users;")
            self.cursor.execute("CREATE TABLE Users"
            "(id_user INT AUTO_INCREMENT NOT NULL, lastname VARCHAR(255) NOT NULL,"
            "firstname VARCHAR(255) NOT NULL,"
            " email VARCHAR(255) UNIQUE NOT NULL,"
            "password VARCHAR(255) NOT NULL,"
            "PRIMARY KEY (id_user));")
            self.cursor.close()
        database.close()

    def create_account_table(self):
        database = self.database_connection()

        if database.is_connected():
            self.cursor = database.cursor() 
            self.cursor.execute("DROP TABLE IF EXISTS Bank_account;")
            self.cursor.execute("CREATE TABLE Bank_account"
            "(id_account INT PRIMARY KEY AUTO_INCREMENT NOT NULL,"
            "id_user INT NOT NULL,"
            "account_type VARCHAR(100) NOT NULL,"
            "account_name VARCHAR(100) NULL,"
            "balance DECIMAL(13, 2) NOT NULL,"
            "min_balance INT UNSIGNED NOT NULL,"
            "FOREIGN KEY (id_user) REFERENCES Users(id_user) ON DELETE CASCADE);")
            self.cursor.close()
        database.close()

    def create_transactions_table(self):
        database = self.database_connection()

        if database.is_connected():
            self.cursor = database.cursor() 
            self.cursor.execute("DROP TABLE IF EXISTS Transactions;")
            self.cursor.execute("CREATE TABLE Transactions"
            "(id_transaction INT PRIMARY KEY AUTO_INCREMENT NOT NULL,"
            "id_account_emitter INT NULL,"
            "id_account_receiver INT NULL,"
            "deal_description VARCHAR(100) NOT NULL, amount DECIMAL(13, 2) UNSIGNED NOT NULL,"
            "deal_date DATE NOT NULL,"
            "deal_type VARCHAR(100) NOT NULL,"
            "frequency INT UNSIGNED NULL,"
            "category VARCHAR(100) NULL,"
            "charges DECIMAL(13, 2) NULL,"
            "FOREIGN KEY (id_account_emitter) REFERENCES Bank_account(id_account),"
            "FOREIGN KEY (id_account_receiver) REFERENCES Bank_account(id_account));")
            self.cursor.close()
        database.close()
    
    def update_database_data(self):
        pass
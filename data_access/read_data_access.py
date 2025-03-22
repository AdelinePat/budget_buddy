from model.server import ServerDatabase
from model.customexception import TransactionException, LogInDataException

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
   
    def get_balance_from_main_user_account(self, user_id): #not used ?
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
    
    ### Florence methods

    def get_user_id_from_email(self, email):
        if email == None or type(email) != str:
            error_message = "Le mail doit être une chaîne de caractères"
            raise LogInDataException(error_message)
        
        conn = self.database.database_connection()
        if conn.is_connected():
            cursor = conn.cursor()
            query = "SELECT id_user FROM Users WHERE email = %s"
            cursor.execute(query, (email,))
            result = cursor.fetchone()
            cursor.close()
        conn.close()
        
        return result[0] if result else None
    
    def get_password_from_id_user(self, id_user):
        if id_user == None or type(id_user) != int:
            error_message = "L'identifiant utilisateur n'existe pas ou n'est pas valide"
            raise LogInDataException(error_message)
               
        conn = self.database.database_connection()
        if conn.is_connected():
            cursor = conn.cursor()
            query = "SELECT password FROM Users WHERE id_user = %s"
            cursor.execute(query, (id_user,))
            result = cursor.fetchone()
            cursor.close()
        conn.close()

        if result:
            return result[0]
        return None
    
    def get_all_users(self):
        conn = self.database.database_connection()
        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute("SELECT id_user, firstname, lastname, email, password FROM Users")
            users = cursor.fetchall()  
            cursor.close()
        conn.close()        
        return users
    
    def does_email_already_exist(self, firstname, lastname, email):
        conn = self.database.database_connection()
        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute(
                "SELECT COUNT(*) FROM Users WHERE firstname = %s AND lastname = %s AND email = %s",
                (firstname, lastname, email)
            )
            result = cursor.fetchone()
            count = result[0]
        if count != 0:
            error_messasge = "Ce mail est déjà utilisé"
            raise LogInDataException(error_messasge)
        
    def get_user_id_from_names_email(self, firstname, lastname, email):
        conn = self.database.database_connection()
        if conn.is_connected():
            cursor = conn.cursor()
            query = "SELECT id_user FROM Users WHERE firstname = %s AND lastname = %s AND email = %s"
            values = (firstname, lastname, email)
            cursor.execute(query, values)
            id_user = cursor.fetchone()

            cursor.close()
        conn.close()

        if id_user[0] is None:
            error_message = "L'utilisateur n'existe pas. Impossible de créer un compte bancaire."
            raise LogInDataException(error_message)
        return id_user[0]

        # cursor.execute(
        #                 "SELECT id_user FROM Users WHERE firstname = %s AND lastname = %s AND email = %s",
        #                 (firstname, lastname, email)
        #             )


    def print_all_users_and_accounts(self):
        conn = self.database.database_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id_user, firstname, lastname, email FROM Users")
        users = cursor.fetchall()  # Récupère tous les utilisateurs
        if users:
            for user in users:
                user_id, firstname, lastname, email = user
                print(f"Utilisateur: ID: {user_id}, Prénom: {firstname}, Nom: {lastname}, Email: {email}")

                # Récupère et affiche les comptes associés à cet utilisateur
                cursor.execute("SELECT account_type, account_name, balance FROM Bank_account WHERE id_user = %s", (user_id,))
                accounts = cursor.fetchall()
                if accounts:
                    for account in accounts:
                        account_type, account_name, balance = account
                        print(f"\tCompte: Type: {account_type}, Nom: {account_name}, Solde: {balance}")
                else:
                    print("\tAucun compte bancaire associé.")
        else:
            print("Aucun utilisateur trouvé.")
        cursor.close()
        conn.close()
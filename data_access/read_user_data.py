from model.server import ServerDatabase
from model.customexception import LogInDataException

class UserDataAcess():
    def __init__(self):
        self.database = ServerDatabase()

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
    
    def get_fullname_from_id(self, id_user): ### DASHBOARD DATA MANAGER
        if id == None or type(id_user) != int:
            error_message = "L'identifiant n'est pas reconnu ou est incorrect"
            raise LogInDataException(error_message)
        
        conn = self.database.database_connection()
        if conn.is_connected():
            cursor = conn.cursor()
            query = "SELECT lastname, firstname FROM Users WHERE id_user = %s"
            cursor.execute(query, (id_user,))
            result = cursor.fetchone()
            cursor.close()
        conn.close()
        
        if result == None:
            raise LogInDataException("Le nom et prénom n'ont pas été trouvé")
        fullname = result[0] + " " + result[1]
        return fullname
        
        # return result[0] if result else None
    
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
    
    def does_email_already_exist(self, email):
        conn = self.database.database_connection()
        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute(
                "SELECT COUNT(*) FROM Users WHERE email = %s",
                (email,)
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
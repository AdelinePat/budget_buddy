from model.server import ServerDatabase
from model.customexception import LogInDataException
from data_access.read_user_data import UserDataAcess

class LoginQuery():
    def __init__(self):
        self.database = ServerDatabase()
        self.__data_access = UserDataAcess()

    def __create_user(self, login_info):
        conn = self.database.database_connection()
        if conn.is_connected():
            cursor = conn.cursor()
            query = "INSERT INTO Users (firstname, lastname, email, password) VALUES (%(firstname)s, %(lastname)s, %(email)s, %(password)s)"
            values = {
                'firstname' : login_info.get_firstname(),
                'lastname' : login_info.get_lastname(),
                'email' : login_info.get_email(),
                'password' : login_info.get_password()}
            cursor.execute(query, values)
            conn.commit()
            cursor.close()
        conn.close()
    
    def create_banck_account_when_connected(self, user_id, account_type):
        conn = self.database.database_connection()
        if conn.is_connected():
            cursor = conn.cursor()

            query = """INSERT INTO Bank_account (id_user, account_type, account_name, balance, min_balance) 
                    VALUES (%(id_user)s, %(account_type)s, %(account_name)s, %(balance)s, %(min_balance)s)"""
            values = {
                'id_user' : user_id,
                'account_type' : account_type,
                'account_name' : None,
                'balance' : 0,
                'min_balance' : 0
            }
            cursor.execute(query, values)
              
            conn.commit()
            cursor.close()
        conn.close()

    def get_fullname_from_id(self, user_id):
        pass
    
    def __create_bank_acount(self, login_info):
        conn = self.database.database_connection()
        if conn.is_connected():
            cursor = conn.cursor()

            query = """INSERT INTO Bank_account (id_user, account_type, account_name, balance, min_balance) 
                    VALUES (%(id_user)s, %(account_type)s, %(account_name)s, %(balance)s, %(min_balance)s)"""
            values = {
                'id_user' : login_info.get_user_id(),
                'account_type' : 'Compte Courant',
                'account_name' : None,
                'balance' : 0,
                'min_balance' : 0
            }
            cursor.execute(query, values)
              
            conn.commit()
            cursor.close()
        conn.close()
                                                # print(f"L'utilisateur a été créé avec succès et un compte bancaire lui a été associé (ID: {id_user}).")

                                                # self.error_label.configure(text="Compte créé avec succès !", text_color="green")
    def register_user(self, login_info):
        # try:
        self.__create_user(login_info)
        login_info.set_id_user(self.__data_access.get_user_id_from_names_email(login_info.get_firstname(),\
                                                                            login_info.get_lastname(), \
                                                                            login_info.get_email()))
        
        self.__create_bank_acount(login_info)

            
        #         else:
        #             print("L'utilisateur existe déjà !!")
        #             self.error_label.configure(text="Cet email est déjà utilisé.", text_color="red")
        #         cursor.close()
        #     conn.close()
        
        # except Exception as error:
        #     print(f"[LogInOut][register_user] Erreur : {error}")
        #     self.error_label.configure(text="Une erreur s'est produite. Réessayez.", text_color="red")
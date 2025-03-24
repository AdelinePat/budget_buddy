from data_access.read_user_data import UserDataAcess
from data_access.write_loginquery import LoginQuery
from model.customexception import LogInDataException
import re
import bcrypt

class LoginManager():
    def __init__(self):
        self.__data_access = UserDataAcess()
        self.__query = LoginQuery()
    
    def validate_email(self, email):
        email_regex = r"^[\w\.\+-]+@[a-zA-Z0-9\.\-]+\.[a-zA-Z]{2,}$"
        result = re.match(email_regex, email)
        if result == None:
            error_message = "Email invalide. Format attendu : exemple@domaine.com"
            raise LogInDataException(error_message)
        return result.group()
    
    def __hash_password__(self, password):
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed_password.decode('utf-8')
    
    def check_password(self, stored_hashed_password, input_password):
        return bcrypt.checkpw(input_password.encode('utf-8'), stored_hashed_password.encode('utf-8'))

    def validate_password(self, password):
        password_regex = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&_\-])[A-Za-z\d@$!%*?&_\-\_]{10,}$"
        result_password = re.match(password_regex, password)
        if result_password == None:
            error_message = """Mot de passe invalide. Il doit contenir au moins:\n
                - Une majuscule\n
                - Une minuscule\n
                - Un chiffre\n\
                - Un caractère spécial (!@#$%^&*.._.)\n
                - 10 caractères"""
            raise LogInDataException(error_message)
        return result_password.group()
    
    def __check_names__(self, firstname, lastname):
        if (firstname == None or firstname == "") or (lastname == None or lastname == ""):
            error_message = "Le prénom et le nom sont obligatoires."
            raise LogInDataException(error_message)

    def __clean_register_user_data__(self, login_info):
        self.__check_names__(login_info.get_firstname(), login_info.get_lastname())
        
        valid_email = self.validate_email(login_info.get_email())
        login_info.set_email(valid_email)

        valid_password = self.validate_password(login_info.get_password())
        login_info.set_password(valid_password)

        if login_info.get_password() != login_info.get_confirm_password():
            error_message="Les mots de passe ne correspondent pas."
            raise LogInDataException(error_message)
        
        self.__data_access.does_email_already_exist(login_info.get_email())


    def register_user(self, login_info):
        self.__clean_register_user_data__(login_info)

        login_info.set_password(self.__hash_password__(login_info.get_password())) # hash password

        self.__query.register_user(login_info)

        
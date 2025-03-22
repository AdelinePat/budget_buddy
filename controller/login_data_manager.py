from data_access.account_data_access import DataAccess
import re
import bcrypt

class LoginManager():
    def __init__(self):
        self.__data_access = DataAccess()
    
    def validate_email(self, email):
        email_regex = r"^[\w\.\+-]+@[a-zA-Z0-9\.\-]+\.[a-zA-Z]{2,}$"
        return re.match(email_regex, email)
    
    def hash_password(self, password):
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed_password.decode('utf-8')
    
    def check_password(self, stored_hashed_password, input_password):
        return bcrypt.checkpw(input_password.encode('utf-8'), stored_hashed_password.encode('utf-8'))

    def validate_password(self, password):
        password_regex = r"^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&_\-])[A-Za-z\d@$!%*?&_\-\_]{8,}$"
        return re.match(password_regex, password)
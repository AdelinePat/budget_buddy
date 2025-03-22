class LoginInfo():
    def __init__(self, email="", password="", lastname="", firstname="", current_user=None):
        self.__id_user = None
        self.__email = email
        self.__password = password
        self.__lastname = lastname
        self.__firstname = firstname
        self.__current_account = None
        self.__confirm_password = None

    def get_user_id(self):
        return self.__id_user
    
    def get_email(self):
        return self.__email
    
    def get_password(self):
        return self.__password
    
    def get_confirm_password(self):
        return self.__confirm_password
    
    def get_lastname(self):
        return self.__lastname
    
    def get_firstname(self):
        return self.__firstname
    
    def get_current_account(self):
        return self.__current_account
    
    def set_id_user(self, new_value):
        self.__id_user = new_value

    def set_email(self, new_value):
        self.__email = new_value
    
    def set_password(self, new_value):
        self.__password = new_value

    def set_confirm_password(self, new_value):
        self.__confirm_password = new_value
        
    def set_lastname(self, new_value):
        self.__lastname = new_value

    def set_firstname(self, new_value):
        self.__firstname = new_value
    
    def set_current_account(self, new_value):
        self.__lastname = new_value

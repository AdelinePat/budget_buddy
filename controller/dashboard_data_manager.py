from data_access.read_user_data import UserDataAcess
from data_access.write_loginquery import LoginQuery
from model.customexception import LogInDataException
import re

class DashboardManager():
    def __init__(self):
        self.__data_access = UserDataAcess()
        self.__query = LoginQuery() # create account
        self.__read_data = UserDataAcess()

    def create_account_from_user_id(self, id_user, account_type):
        self.__query.create_banck_account_when_connected(id_user, account_type)

    def get_name_from_id(self, user_id):
        return self.__read_data.get_fullname_from_id(user_id)

from data_access.read_user_data import UserDataAcess
from data_access.write_loginquery import LoginQuery
from model.customexception import LogInDataException
import re

class DashboardManager():
    def __init__(self):
        self.__data_access = UserDataAcess()
        self.__query = LoginQuery() # create account

    def create_account_from_user_id(self, id_user, account_type):
        self.__query.create_banck_account_when_connected(id_user, account_type)

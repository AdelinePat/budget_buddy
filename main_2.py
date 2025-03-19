import mysql.connector
import customtkinter
# import hashlib 
# import secrets


# from view.interface import Interface
from view.login_out import LogInOut
from view.transactions import TransactionView
from view.__settings__ import DARK_BLUE, SOFT_BLUE, LIGHT_BLUE, YELLOW, SOFT_YELLOW, PINK

class ViewTransactions():
    pass


login_view = LogInOut("Connexion Client", 0)
login_view.mainloop()
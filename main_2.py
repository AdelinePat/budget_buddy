import mysql.connector
import customtkinter
import hashlib 
import secrets
# from view.interface import Interface
from view.login_out import LogInOut
from view.transactions import TransactionView
from controller.transactionmanager import TransactionManager
from view.__settings__ import DARK_BLUE, SOFT_BLUE, LIGHT_BLUE, YELLOW, SOFT_YELLOW, PINK

from model.server import ServerDatabase

server_connection = ServerDatabase()
server_connection.server_connection()
server_connection.create_database()
# server_connection.create_client_table()
# server_connection.create_account_table()
# server_connection.create_transactions_table()

# login_view = TransactionView("Transactions", 0, 2) # window_title, column_number, current_session (id_user)
# login_view.mainloop()

# view_test = TransactionManager("Transactions", 0, 2) # window_title, column_number, current_session (id_user)
view_test = TransactionView("Transactions", 0, 2)
view_test.mainloop()
# view_test.run()

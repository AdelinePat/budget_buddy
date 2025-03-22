import mysql.connector
import customtkinter
import hashlib 
import secrets
# from view.interface import Interface
from view.login_out import LogInOut
from view.interface import Interface
from view.dashboard import Dashboard
from view.__settings__ import DARK_BLUE, SOFT_BLUE, LIGHT_BLUE, YELLOW, SOFT_YELLOW, PINK

from model.server import ServerDatabase

server_connection = ServerDatabase()
server_connection.server_connection()
server_connection.create_database()

view = LogInOut("Connexion Client", 0)
view.mainloop()
interface = Interface("Budget Buddy", 1)
dashboard = Dashboard(interface)
dashboard.build_dashboard()
# transaction = TransactionView(dashboard)


interface.mainloop()

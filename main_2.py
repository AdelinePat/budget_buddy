import mysql.connector
import customtkinter
import hashlib 
import secrets
from view.interface import Interface
from view.login_out import LogInOut
from view.interface import Interface
from view.dashboard import Dashboard
from view.__settings__ import DARK_BLUE, SOFT_BLUE, LIGHT_BLUE, YELLOW, SOFT_YELLOW, PINK
from view.transactions import TransactionView

from model.server import ServerDatabase

server_connection = ServerDatabase()
server_connection.server_connection()
server_connection.create_database()

view = LogInOut("Budget Buddy - Connexion Client", 0)
view.mainloop()

# interface = Interface("Budget Buddy", 1)
# dashboard = Dashboard("Budget Buddy - Dashboard", 1)
# dashboard.build_dashboard()
# transaction = TransactionView(dashboard)
# view = TransactionView("Budget Buddy - Transaction", 0, 6, 7)
# view.mainloop()


# dashboard.mainloop()

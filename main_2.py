
from view.login_out import LogInOut
from view.dashboard import Dashboard

from model.server import ServerDatabase

server_connection = ServerDatabase()
server_connection.server_connection()
server_connection.create_database()

view = LogInOut("Budget Buddy - Connexion Client", 0)
view.mainloop()

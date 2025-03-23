
from view.login_out import LogInOut
from view.dashboard import Dashboard

from model.server import ServerDatabase

server_connection = ServerDatabase()
server_connection.server_connection()
server_connection.create_database()

connected = [False, None]
view = LogInOut("Budget Buddy - Connexion Client", 0, connected)
view.mainloop()

if connected[0]:
    board = LogInOut("Budget Buddy - Dashboard", 1, connected)
    board.mainloop()

import mysql.connector
import customtkinter
import hashlib 
import secrets
# from view.interface import Interface
from view.login_out import LogInOut
from view.transactions import TransactionView
from controller.transactionmanager import TransactionManager
from view.interface_frames import Interface_frames
from view.historic import Historic
from view.__settings__ import DARK_BLUE, SOFT_BLUE, LIGHT_BLUE, YELLOW, SOFT_YELLOW, PINK

from model.server import ServerDatabase

server_connection = ServerDatabase()
server_connection.server_connection()
server_connection.create_database()

# view = LogInOut("Connexion Client", 0)

# view_test = TransactionManager("Transactions", 0, 2) # window_title, column_number, current_session (id_user)
view_test = TransactionView("Transactions", 0, 2)
view_test.mainloop()
# login_view = Historic("HIHIAHHEIAHIIFEZHFEZ", 1)

# login_view.interface_frame = Interface_frames(login_view, bg_color=DARK_BLUE, fg_color=LIGHT_BLUE, width=200, corner_radius=20)
# login_view.interface_frame.columnconfigure(0, weight=1)
# login_view.interface_frame.grid(row=0, column=0, padx=20, pady=20, sticky="ew")
# login_view.interface_frame.box = customtkinter.CTkLabel(
#     login_view.interface_frame, text="fegfeer", 
#     height=50, width=200, bg_color=DARK_BLUE, corner_radius=20,
#     fg_color=SOFT_BLUE, text_color=LIGHT_BLUE
# )
# login_view.interface_frame.box.grid(row=0, column=0)

# login_view.mainloop()

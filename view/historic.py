import customtkinter
# import tkcalendar
# from CTkDatePicker import CTkDatePicker
from tkcalendar import Calendar
from view.interface import Interface
from view.interface_frames import Interface_frames
from view.__settings__ import DARK_BLUE, SOFT_BLUE, LIGHT_BLUE, YELLOW, SOFT_YELLOW, PINK
from model.historic_account import Historic_Account

class Historic(Interface):
    def __init__(self, window_title, column_number):
        self.list_accounts : list = [
            (0,1,"Tous les comptes", "NULL", 0,0),
            (1,1,"Compte courant", "NULL", 100,0),
            (2,1,"Livret A", "NULL", 100,0),
            (3,1,"Compte épargne", "NULL", 100,0),
            (4,1,"Compte hihi", "NULL", 100,0),
            (5,1,"Compte haha", "NULL", 100,0),
            (6,1,"Compte courant", "NULL", 100,0),
            (7,1,"Compte courant", "NULL", 100,0)
        ]
        self.shown_historic = "0"
        self.recover_accounts()
        self.list_all_accounts()

        super().__init__(window_title, column_number)
        self.historic_frame = Interface_frames(self, fg_color=LIGHT_BLUE, width=200, bg_color=DARK_BLUE, corner_radius=20)
        self.historic_frame.columnconfigure(0, weight=1)
        self.historic_frame.grid(row=0, column=1, padx=20, pady=20, sticky="ew")
        self.build_historic_interface()
    
    def build_historic_interface(self):
        self.historic_frame.historic_title = customtkinter.CTkLabel(
            self.historic_frame, text="Historique des transactions", 
            height=50,
            fg_color=SOFT_BLUE, text_color=LIGHT_BLUE
        )
        self.historic_frame.historic_title.grid(row=0, column=0, pady=20, sticky="ew")
        # self.recover_accounts()
        self.historic_frame.historic_account_choice = customtkinter.CTkComboBox(
            self.historic_frame, corner_radius=15, values=self.display_accounts, command=self.flip_historic_account
        )
        self.historic_frame.historic_account_choice.grid(row=1, column=0, padx=20, sticky="ew")

        self.historic_dict_account[self.shown_historic].build(
            self.historic_frame,
            self.display_accounts[list(self.historic_dict_account.keys()).index(self.shown_historic)]
        )
    
    def recover_accounts(self):
        self.historic_dict_account : dict = {}
        for index, account in enumerate(self.list_accounts):
            historic_account = Historic_Account(self.list_accounts[index])
            self.historic_dict_account.update(
                {str(account[0]) : historic_account}
            )
    
    def list_all_accounts(self):
        self.display_accounts : list = []
        for account in self.list_accounts:
            display = str(account[0]) + " " + account[2]
            self.display_accounts.append(display)

    def flip_historic_account(self, choice):
        self.historic_dict_account[self.shown_historic].destroy(self.historic_frame)
        self.shown_historic = choice[0]
        self.historic_dict_account[self.shown_historic].build(
            self.historic_frame,
            self.display_accounts[list(self.historic_dict_account.keys()).index(self.shown_historic)]
        )
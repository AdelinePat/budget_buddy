import customtkinter

from view.interface import Interface

from view.historic import Historic
from view.interface_frames import Interface_frames
from view.__settings__ import DARK_BLUE, SOFT_BLUE, LIGHT_BLUE, YELLOW, SOFT_YELLOW, PINK

class Dashboard(Interface):
    def __init__(self, master):
        self.master = master
        self.account_id = "0"
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
        self.list_all_accounts()
    
    def build_dashboard(self):
        self.master.interface_frame = Interface_frames(self.master, bg_color=DARK_BLUE, fg_color=LIGHT_BLUE, width=400,corner_radius=20)
        self.master.interface_frame.columnconfigure(0, weight=1)
        self.master.interface_frame.grid(row=0, column=0, padx=20, pady=20, sticky="snew")
    
        self.master.interface_frame.box = customtkinter.CTkLabel(
            self.master.interface_frame, text="Bienvenue".upper(), 
            height=50, width=350, bg_color=DARK_BLUE,
            fg_color=SOFT_BLUE, text_color=LIGHT_BLUE,
            font=self.master.subtitle_font
        )
        self.master.interface_frame.account_choice = customtkinter.CTkComboBox(
            self.master.interface_frame, corner_radius=15, values=self.display_accounts, command=self.flip_account,
            font=self.master.text_font
        )
        self.master.interface_frame.transaction_button = customtkinter.CTkButton(
            self.master.interface_frame, text="Initier un virement depuis ce compte",
            height=60, bg_color=SOFT_BLUE,
            fg_color=SOFT_BLUE, text_color=LIGHT_BLUE,
            font=self.master.text_font, command=self.init_transaction
        )
        self.master.interface_frame.box.grid(row=0, column=0, pady=20, sticky="ew")
        self.master.interface_frame.account_choice.grid(row=1, column=0, padx=10, pady=20, sticky="ew")
        self.master.interface_frame.transaction_button.grid(row=2, column=0, padx=10, pady=5, sticky="ew")

        self.historic = Historic(self.master, self.list_accounts, self.display_accounts, self.account_id)
    
    def init_transaction(self):
        pass

    def flip_account(self, choice):
        self.historic.flip_historic_account(choice)
        self.account_id = choice[0]

    def list_all_accounts(self):
        self.display_accounts : list = []
        for account in self.list_accounts:
            display = str(account[0]) + " " + account[2]
            self.display_accounts.append(display)
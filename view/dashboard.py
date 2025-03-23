import customtkinter

from view.interface import Interface

from view.historic import Historic
from view.interface_frames import Interface_frames
from view.__settings__ import DARK_BLUE, SOFT_BLUE, LIGHT_BLUE, YELLOW, SOFT_YELLOW, PINK
from data_access.read_data_access import DataAccess
from view.transactions import TransactionView

class Dashboard(Interface):
    def __init__(self, window_title, column_number, login_info):
        super().__init__(window_title, column_number)
        self.login_info = login_info[1]
        self.database = DataAccess()
        self.list_accounts : list = self.database.get_all_accounts_from_user(self.login_info.get_user_id())
        self.list_accounts.insert(0, (0, "Tous les comptes"))
        # self.master = master
        # self.master = self
        
        self.account_id = "0"
        self.interface_frame = Interface_frames(self, bg_color=DARK_BLUE, fg_color=LIGHT_BLUE, width=400,corner_radius=20)
        self.interface_frame.columnconfigure(0, weight=1)
        self.interface_frame.grid(row=0, column=0, padx=20, pady=20, sticky="snew")

        self.list_all_accounts()
        self.build_dashboard()
    
    def build_dashboard(self):
        # self.interface_frame = Interface_frames(self, bg_color=DARK_BLUE, fg_color=LIGHT_BLUE, width=400,corner_radius=20)
        # self.interface_frame.columnconfigure(0, weight=1)
        # self.interface_frame.grid(row=0, column=0, padx=20, pady=20, sticky="snew")
    
        self.interface_frame.box = customtkinter.CTkLabel(
            self.interface_frame, text="Bienvenue".upper(), 
            height=50, width=350, bg_color=DARK_BLUE,
            fg_color=SOFT_BLUE, text_color=LIGHT_BLUE,
            font=self.subtitle_font
        )
        self.interface_frame.account_choice = customtkinter.CTkComboBox(
            self.interface_frame, corner_radius=15, values=self.display_accounts, command=self.flip_account,
            font=self.text_font
        )
        self.interface_frame.transaction_button = customtkinter.CTkButton(
            self.interface_frame, text="Initier un virement depuis ce compte",
            height=60, bg_color=SOFT_BLUE,
            fg_color=SOFT_BLUE, text_color=LIGHT_BLUE,
            font=self.text_font, command=self.init_transaction
        )
        self.interface_frame.box.grid(row=0, column=0, pady=20, sticky="ew")
        self.interface_frame.account_choice.grid(row=1, column=0, padx=10, pady=20, sticky="ew")
        self.interface_frame.transaction_button.grid(row=2, column=0, padx=10, pady=5, sticky="ew")

        self.historic = Historic(self, self.list_accounts, self.display_accounts, self.account_id)
    
    def init_transaction(self):
        # window_title, column_number, current_session, current_account
        transaction = TransactionView(
            "Budget Buddy - Transaction",
            0,
            self.login_info.get_user_id(),
            self.login_info.get_current_account()
        )
        transaction.mainloop()

    def flip_account(self, choice):
        self.historic.flip_historic_account(choice)
        self.account_id = choice[0]

    def list_all_accounts(self):
        self.display_accounts : list = []
        for account in self.list_accounts:
            display = str(account[0]) + " " + account[1]
            self.display_accounts.append(display)
import customtkinter
from view.historic import Historic
from view.transactions import TransactionView
from view.interface_frames import Interface_frames
from view.__settings__ import DARK_BLUE, SOFT_BLUE,\
                            LIGHT_BLUE, YELLOW,\
                            SOFT_YELLOW, ACCOUNT_TYPE_LIST
from data_access.read_data_access import DataAccess
from controller.dashboard_data_manager import DashboardManager

class Dashboard():
    def __init__(self, master, window_title, column_number, login_info):
        # super().__init__(window_title, column_number)
        self.login_info = login_info
        self.master = master
        self.database = DataAccess()
        self.list_accounts = self.database.get_all_accounts_from_user(self.login_info.get_user_id())
        self.list_accounts.insert(0, (0, "Tous les comptes"))
        self.controller = DashboardManager()
        self.account_type_list = ACCOUNT_TYPE_LIST
        
        # self.master = master
        # self.master = self
        
        self.account_id = "0"
        
        self.main_frame = Interface_frames(self.master, bg_color=DARK_BLUE, fg_color=DARK_BLUE)
        self.main_frame.grid(columnspan=2, row=0, column=0, sticky="snew")
        # self.main_frame.grid_configure(columnspan=2, row=0, column=0, padx=20, pady=20, sticky="snew")
        

        self.interface_frame = Interface_frames(self.main_frame, bg_color=DARK_BLUE, fg_color=LIGHT_BLUE, width=400,corner_radius=20)
        self.interface_frame.columnconfigure(0, weight=1)
        self.interface_frame.grid(row=2, column=0, padx=20, pady=20, sticky="snew")
        # self.interface_frame.grid_configure(columnspan=1)
        # self.interface_frame.grid_propagate(True)

        ### DOIT ETRE HISTORIC()
        self.historic_frame = Interface_frames(self.main_frame, fg_color=LIGHT_BLUE, width=200, bg_color=DARK_BLUE, corner_radius=20)
        self.historic_frame.columnconfigure(0, weight=1)
        self.historic_frame.grid(row=2, column=1, padx=20, pady=20, sticky="snew")

        self.display_accounts = self.list_all_accounts()
        self.build_dashboard()

    def build_account_choice_combobox(self):
        if self.display_accounts != self.list_all_accounts():
            self.display_accounts = self.list_all_accounts()
            self.interface_frame.account_choice.destroy()
            self.historic_frame.list_accounts = self.list_all_accounts()

        self.interface_frame.account_choice = customtkinter.CTkComboBox(
            self.interface_frame,
            values=self.display_accounts,
            command=self.flip_account,
            font=self.master.text_font,
            text_color=DARK_BLUE,
            dropdown_text_color = DARK_BLUE,
            bg_color=LIGHT_BLUE,
            fg_color=SOFT_YELLOW,
            dropdown_fg_color = SOFT_YELLOW, 
            dropdown_font= self.master.text_font,
            dropdown_hover_color = SOFT_BLUE,
            corner_radius=15
        )

        self.interface_frame.account_choice.grid(row=3, column=0, padx=10, pady=20, sticky="ew")

        
    def build_dashboard(self):
        self.title = self.build_label("Budget Buddy",
                                             0,
                                             color=YELLOW,
                                             bg_color=DARK_BLUE,
                                             custom_font=self.master.title_font,
                                             padvertical=(20,5))
        
        
        # self.interface_frame = Interface_frames(self, bg_color=DARK_BLUE, fg_color=LIGHT_BLUE, width=400,corner_radius=20)
        # self.interface_frame.columnconfigure(0, weight=1)
        # self.interface_frame.grid(row=0, column=0, padx=20, pady=20, sticky="snew")
        
        user_name = self.controller.get_name_from_id(self.login_info.get_user_id())
        welcome_message = "Bienvenue " + user_name
        self.subtitle = self.build_label(f"Dashboard de {user_name}".upper(), 1, color=YELLOW, bg_color=DARK_BLUE, custom_font=self.master.subtitle_font)

        self.interface_frame.box = customtkinter.CTkLabel(
            self.interface_frame, text=welcome_message.upper(), 
            height=50, width=350, bg_color=SOFT_BLUE,
            fg_color=SOFT_BLUE, text_color=LIGHT_BLUE,
            font=self.master.subtitle_font
        )

        self.build_account_choice_combobox()
        
        self.interface_frame.transaction_button = customtkinter.CTkButton(
            self.interface_frame, text="Initier un virement depuis ce compte",
            height=60, bg_color=SOFT_BLUE,
            fg_color=SOFT_BLUE, text_color=DARK_BLUE,
            font=self.master.text_font, command=self.init_transaction
        )
        self.interface_frame.box.grid(row=2, column=0, pady=20, sticky="ew")
        
        self.interface_frame.transaction_button.grid(row=4, column=0, padx=10, pady=5, sticky="ew")

        self.interface_frame.create_bank_account_button = customtkinter.CTkButton(
            self.interface_frame, text="Création d'un nouveau compte bancaire",
            height=60, bg_color=SOFT_BLUE,
            fg_color=SOFT_BLUE, text_color=DARK_BLUE,
            font=self.master.text_font, command=self.create_account_callback
        )
        self.interface_frame.create_bank_account_button.grid(row=5, column=0, padx=10, pady=5, sticky="ew")
        
        self.create_logout_button(7) ### if create_bank_account -> row_position 5 already taken ###
        
        self.list_accounts = self.list_all_accounts()
        self.historic = Historic(self.historic_frame, self.list_accounts, self.display_accounts, self.login_info)
        print("j'essaye de print historic à sa création")
        print(self.historic)

    def create_logout_button(self, row_position):
        self.interface_frame.logout_button = customtkinter.CTkButton(
            self.interface_frame, text="Se déconnecter",
            height=60, bg_color=SOFT_BLUE,
            fg_color=SOFT_BLUE, text_color=LIGHT_BLUE,
            font=self.master.text_font, command=self.logout_callback
        )

        self.interface_frame.logout_button.grid(row=row_position, column=0, padx=10, pady=5, sticky="ew")

    def logout_callback(self):
        print("Déconnexion réussie")
        self.login_info.set_id_user(None)
        self.dashboard_screen_destroy()
        self.master.connected = False
        return
        # self.interface_screen_destroy()
        # self.login_screen_build()
        # if hasattr(self, 'login_text'):
        #     self.login_text.destroy()

    def dashboard_screen_destroy(self):
        self.title.destroy()
        self.interface_frame.destroy()
        if hasattr(self, 'historic'):
            delattr(self, 'historic')
        self.master.login_screen_build()
        # self.historic.historic_destroy()
        # self.historic.historic_frame.destroy()
        # self.historic.destroy()

    def create_account_callback(self):

        self.interface_frame.account_type_choice = customtkinter.CTkComboBox(master=self.interface_frame,
            values=self.account_type_list, state="readonly",
            command=self.account_combobox_callback,
            font=self.master.text_font,
            text_color=DARK_BLUE,
            dropdown_text_color = DARK_BLUE,
            bg_color=LIGHT_BLUE,
            fg_color=SOFT_YELLOW,
            dropdown_fg_color = SOFT_YELLOW, 
            dropdown_font= self.master.text_font,
            dropdown_hover_color = SOFT_BLUE,
            corner_radius=15)

        self.interface_frame.account_type_choice.grid(row=6, column=0, sticky="sew", padx=20, pady=0)
        self.interface_frame.account_type_choice.set(self.account_type_list[0])

    def account_combobox_callback(self, choice):
        account_type = choice
        id_user = self.login_info.get_user_id()
        self.controller.create_account_from_user_id(id_user, account_type)
        self.interface_frame.account_type_choice.destroy()
        self.interface_frame.create_account_message = self.build_label("Compte créé avec succès", 6, self.interface_frame)
        
        self.build_account_choice_combobox()

    def build_label(self, label_text, row_number, master=None, color=DARK_BLUE, bg_color=LIGHT_BLUE, custom_font=None, padvertical=(5,2), justify="center", anchor="center"):
        if custom_font == None:
            custom_font = self.master.text_font

        if justify != "center":
            anchor=justify
        if master==None:
            master = self.main_frame

        if bg_color != LIGHT_BLUE:
            bg_color = bg_color
        
        my_label = customtkinter.CTkLabel(master=master,
                                          text=label_text,
                                          font=custom_font, 
                                          text_color=color, 
                                          bg_color=bg_color, 
                                          justify=justify,
                                          anchor=anchor)
        my_label.grid(row=row_number, column=0, sticky="ew", padx=20, pady=padvertical)
        return my_label

    def init_transaction(self):
        # window_title, column_number, current_session, current_account
        if hasattr(self.interface_frame, 'create_account_message'):
            self.interface_frame.create_account_message.destroy()

        if hasattr(self.interface_frame, 'account_type_choice'):
            self.interface_frame.account_type_choice.destroy()

        self.login_info.set_current_account(self.interface_frame.account_choice.get())
        
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

        self.login_info.set_current_account(choice[0])

        self.historic.login_info.set_current_account(choice[0])
        

        if hasattr(self.interface_frame, 'account_type_choice'):
            self.interface_frame.account_type_choice.destroy()

    def list_all_accounts(self):
        if self.list_accounts != self.database.get_all_accounts_from_user(self.login_info.get_user_id()):
            self.list_accounts = self.database.get_all_accounts_from_user(self.login_info.get_user_id())
            self.list_accounts.insert(0, (0, "Tous les comptes"))

        display_accounts : list = []
        for account in self.list_accounts:
            display = str(account[0]) + " " + account[1]
            display_accounts.append(display)

        return display_accounts
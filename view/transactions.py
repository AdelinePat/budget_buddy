import customtkinter
# import tkcalendar
# from CTkDatePicker import CTkDatePicker
from tkcalendar import Calendar, DateEntry
# from CTkDatePicker import CTkDatePicker
from view.interface import Interface
# from model.transactionquery import TransactionQuery
from controller.transactionmanager import TransactionManager
from model.transactioninfo import TransactionInfo
from model.transactionexception import TransactionException
from data_access.account_data_access import DataAccess
from view.transactions_frame import Scrollable_frame
from view.__settings__ import DARK_BLUE, SOFT_BLUE, LIGHT_BLUE, YELLOW, SOFT_YELLOW, PINK, SOFT_BLUE2, SOFT_BLUE3, DARK_PINK

class TransactionView(Interface): 
    def __init__(self,window_title, column_number, current_session, current_account):
        super().__init__(window_title, column_number)
        self.controller = TransactionManager()
        self.__data_access = DataAccess()
        self.transaction_frame = Scrollable_frame(self, bg_color=DARK_BLUE, fg_color=DARK_BLUE)
        self.transaction_frame.columnconfigure(0, weight=1)
        self.transaction_frame.pack(fill='both', expand=1)
        self.deal_type_list = ['Retrait', 'Dépôt', 'Transfert', 'Virement']
        self.category_list = ['Alimentaire', 'Loisirs', 'Prélèvement', 'Transport', 'Santé', 'Dealing', 'Activités illicites', 'Consommation de café']
        self.transaction_info = TransactionInfo(current_session, current_account, "", "", None, None, "", "", "")
        # self.transaction_info.type = ""
        # self.transaction_info.date = ""
        # # self.current_session = current_session
        # self.transaction_info.emitter = ""
        # self.transaction_info.receiver = ""
        # self.transaction_info.description = ""
        # self.transaction_info.category = ""
        self.__accounts_list = self.__data_access.get_all_accounts_from_user(self.transaction_info.get_current_session())
        self.__accounts_list_string = self.get_accounts_list_string()
        self.last_choice = ""
        self.screen_build()

    def get_accounts_list_string(self):        
        account_str_list = []
        for account in self.__accounts_list:
            string = f"[{str(account[0])}] {account[1]}"
            account_str_list.append(string)

        return account_str_list
    
    def deal_type_callback(self, choice):
        self.last_choice = self.transaction_info.get_type()
        self.transaction_info.set_type(choice)
        self.display_field_from_type(self.transaction_info.get_type())

    def deal_receiver_callback(self, choice):
        self.transaction_info.set_receiver(choice)

    def display_field_from_type(self, deal_type):

        if deal_type == 'Virement':
            if self.last_choice == 'Transfert':
                self.transaction_frame.receiver_label.destroy()
                self.transaction_frame.receiver_choice.destroy()
            self.build_receiver_field(6, 7)
        elif deal_type == 'Transfert':
            if self.last_choice == 'Virement':
                self.transaction_frame.receiver_text.destroy()
                self.transaction_frame.receiver_box.destroy()
            self.build_internal_receiver_field(6, 7)
        else:
            if self.last_choice == 'Virement':
                self.transaction_frame.receiver_text.destroy()
                self.transaction_frame.receiver_box.destroy()
                print("devrait détruire le bénéficiaire du virement")
            elif self.last_choice == 'Transfert':
                self.transaction_frame.receiver_label.destroy()
                self.transaction_frame.receiver_choice.destroy()
                print("devrait détruire le bénéficiaire du transfert")

    def category_callback(self, choice):
        self.transaction_info.set_category(choice)

    def deal_date_callback(self, choice):
        self.transaction_info.set_date(choice)

    def confirm_form_callback(self):

        self.get_fields_deposit_withdrawal()

        self.transaction_info.set_date(self.transaction_frame.chose_date.get_date())
        self.transaction_info.set_type(self.transaction_frame.deal_type_choice.get().strip())

        self.transaction_info.set_description(self.transaction_frame.description_box.get("0.0", "end").strip())

        self.transaction_info.set_amount(self.transaction_frame.amount_box.get("0.0", "end"))
        self.transaction_info.set_category(self.transaction_frame.category_choice.get())

        if self.transaction_info.get_type() == 'Virement':
            self.transaction_info.set_receiver(self.transaction_frame.receiver_box.get("0.0", "end").strip())
        elif self.transaction_info.get_type() == 'Transfert':
            self.transaction_info.set_receiver(self.transaction_frame.receiver_choice.get())
        try:
            if hasattr(self.transaction_frame, 'error_message_text'):
                self.transaction_frame.error_message_text.destroy()
            self.controller.manage_transaction(self.transaction_info)
            self.build_transaction_result("Transaction réussie")
        except TransactionException as e:
            self.build_transaction_result(e)

    def build_transaction_result(self, error_message):
        self.transaction_frame.error_message_text = customtkinter.CTkLabel(master=self.transaction_frame, text=error_message, font=self.text_font, text_color=SOFT_BLUE, bg_color=DARK_BLUE)
        self.transaction_frame.error_message_text.grid(row=14, column=0, sticky="sn", padx=20, pady=5)

    def get_fields_deposit_withdrawal(self):
        if self.transaction_info.get_type() == 'Dépôt':
            self.transaction_info.set_receiver(self.transaction_info.get_current_account())
            self.transaction_info.set_emitter(None)
        else:
            self.transaction_info.set_receiver(None)
            self.transaction_info.set_emitter(self.transaction_info.get_current_account())

    def build_type_field(self, row1, row2):
        self.transaction_frame.deal_type_text = customtkinter.CTkLabel(master=self.transaction_frame, text="Choisissez le type de transaction :", font=self.text_font, text_color=SOFT_YELLOW, bg_color=DARK_BLUE, justify="left", anchor="w")
        self.transaction_frame.deal_type_text.grid(row=row1, column=0, sticky="sew", padx=20, pady=5)

        self.transaction_frame.deal_type_choice = customtkinter.CTkComboBox(master=self.transaction_frame,
            values=self.deal_type_list, state="readonly",
            command=self.deal_type_callback, font=self.text_font, text_color=DARK_BLUE,
            bg_color=DARK_BLUE, fg_color=SOFT_YELLOW, dropdown_fg_color = SOFT_YELLOW, 
            dropdown_text_color = DARK_BLUE, dropdown_font= self.text_font,
            dropdown_hover_color = SOFT_BLUE, corner_radius=10)

        self.transaction_frame.deal_type_choice.grid(row=row2, column=0, sticky="sew", padx=20, pady=0)
        self.transaction_frame.deal_type_choice.set(self.deal_type_list[-1])

        self.transaction_info.set_type(self.transaction_frame.deal_type_choice.get())
        print(f"dropdown type avant callback: {self.transaction_info.get_type()}")
    
    def build_category_field(self, row1, row2):
        category_text = customtkinter.CTkLabel(master=self.transaction_frame, text="Choisissez la catégorie de votre transaction :", font=self.text_font, text_color=SOFT_YELLOW, bg_color=DARK_BLUE, justify="left", anchor="w")
        category_text.grid(row=row1, column=0, sticky="sew", padx=20, pady=5)

        self.transaction_frame.category_choice = customtkinter.CTkComboBox(master=self.transaction_frame,
            values=self.category_list, state="readonly", command=self.category_callback,
            font=self.text_font, text_color=DARK_BLUE, bg_color=DARK_BLUE, fg_color=SOFT_YELLOW,
            dropdown_fg_color = SOFT_YELLOW, dropdown_text_color = DARK_BLUE,
            dropdown_font= self.text_font, dropdown_hover_color = SOFT_BLUE,
            corner_radius=10)

        self.transaction_frame.category_choice.grid(row=row2, column=0, sticky="sew", padx=20, pady=0)
        self.transaction_frame.category_choice.set(self.category_list[-1])
        self.transaction_info.set_category(self.transaction_frame.category_choice.get())
        print(f"dropdown categorie avant callback: {self.transaction_info.get_type()}")
     
    def build_date_entry(self, row1, row2):
        self.transaction_frame.deal_date_text = customtkinter.CTkLabel(master=self.transaction_frame, text="Choisissez la date de votre transaction :", font=self.text_font, text_color=SOFT_YELLOW, bg_color=DARK_BLUE, justify="left", anchor="w")
        self.transaction_frame.deal_date_text.grid(row=row1, column=0, sticky="sew", padx=20, pady=5)
        self.transaction_frame.chose_date = DateEntry(master=self.transaction_frame, date_pattern="yyyy-mm-dd",
            font=self.text_font, text_color=DARK_BLUE, bg_color=DARK_BLUE, fg_color=SOFT_YELLOW,
            dropdown_fg_color = SOFT_YELLOW, dropdown_text_color = DARK_BLUE,
            dropdown_font= self.text_font,
            borderwidth=2, bordercolor=DARK_BLUE,
            background=DARK_BLUE, foreground=SOFT_YELLOW, headersbackground=PINK,
            selectbackground=PINK, normalbackground=LIGHT_BLUE, weekendbackground=SOFT_BLUE, corner_radius=10,
            othermonthbackground=SOFT_BLUE2, othermonthwebackground=SOFT_BLUE3, othermonthforeground=DARK_BLUE, othermonthweforeground=DARK_BLUE)
        self.transaction_frame.chose_date.grid(row=row2, column=0, sticky="sew", padx=20, pady=5)

    def build_calendar(self, row1, row2):
        self.transaction_frame.deal_date_text = customtkinter.CTkLabel(master=self.transaction_frame, text="Choisissez la date de votre transaction :", font=self.text_font, text_color=SOFT_YELLOW, bg_color=DARK_BLUE, justify="left", anchor="w")
        self.transaction_frame.deal_date_text.grid(row=row1, column=0, sticky="sew", padx=20, pady=5)

        self.transaction_frame.chose_date = Calendar(master=self.transaction_frame, selectmode='day', font=self.text_font,
            command=self.deal_date_callback,
            showweeknumbers=False, cursor="hand2", date_pattern= 'y-mm-dd',
            borderwidth=2, bordercolor=DARK_BLUE,
            background=DARK_BLUE, foreground=SOFT_YELLOW, headersbackground=PINK,
            selectbackground=PINK, normalbackground=LIGHT_BLUE, weekendbackground=SOFT_BLUE, corner_radius=10,
            othermonthbackground=SOFT_BLUE2, othermonthwebackground=SOFT_BLUE3, othermonthforeground=DARK_BLUE, othermonthweforeground=DARK_BLUE
            )
        
        self.transaction_frame.chose_date.grid(row=row2,column=0, padx=30, pady=10, sticky='sew')

    def build_description(self, row1, row2):
        self.transaction_frame.description_text = customtkinter.CTkLabel(master=self.transaction_frame, text="Description de la transaction :", font=self.text_font, text_color=SOFT_YELLOW, bg_color=DARK_BLUE, justify="left", anchor="w")
        self.transaction_frame.description_text.grid(row=row1, column=0, sticky="sew", padx=20, pady=5)

        self.transaction_frame.description_box = customtkinter.CTkTextbox(master=self.transaction_frame, font=self.text_font, width=200, height=48, corner_radius=10, bg_color= DARK_BLUE, fg_color= SOFT_YELLOW, text_color = DARK_BLUE) # champs "email"
        self.transaction_frame.description_box.grid(row=row2, column=0, sticky="sew", padx=20, pady=0)
        self.transaction_frame.description_box.insert("0.0", "")

    def build_receiver_field(self, row1, row2):
        self.transaction_frame.receiver_text = customtkinter.CTkLabel(master=self.transaction_frame, text="Bénéficiaire (email) :", font=self.text_font, text_color=SOFT_YELLOW, bg_color=DARK_BLUE, justify="left", anchor="w")
        self.transaction_frame.receiver_text.grid(row=row1, column=0, sticky="sew", padx=20, pady=5)

        self.transaction_frame.receiver_box = customtkinter.CTkTextbox(master=self.transaction_frame, font=self.text_font, width=200, height=48, corner_radius=10, bg_color= DARK_BLUE, fg_color= SOFT_YELLOW, text_color = DARK_BLUE) # champs "email"
        self.transaction_frame.receiver_box.grid(row=row2, column=0, sticky="sew", padx=20, pady=0)
        self.transaction_frame.receiver_box.insert("0.0", "")

    def build_internal_receiver_field(self, row1, row2):
        self.transaction_frame.receiver_label = customtkinter.CTkLabel(master=self.transaction_frame, text="Choisissez le compte bénéficiaire :", font=self.text_font, text_color=SOFT_YELLOW, bg_color=DARK_BLUE, justify="left", anchor="w")
        self.transaction_frame.receiver_label.grid(row=row1, column=0, sticky="sew", padx=20, pady=5)

        self.transaction_frame.receiver_choice = customtkinter.CTkComboBox(master=self.transaction_frame,
            values=self.__accounts_list_string, state="readonly",
            command=self.deal_receiver_callback, font=self.text_font, text_color=DARK_BLUE,
            bg_color=DARK_BLUE, fg_color=SOFT_YELLOW, dropdown_fg_color = SOFT_YELLOW, 
            dropdown_text_color = DARK_BLUE, dropdown_font= self.text_font,
            dropdown_hover_color = SOFT_BLUE, corner_radius=10)

        self.transaction_frame.receiver_choice.grid(row=row2, column=0, sticky="sew", padx=20, pady=0)
        self.transaction_frame.receiver_choice.set(self.__accounts_list_string[0])

    def build_amount_field(self, row1, row2):
        self.transaction_frame.amount_text = customtkinter.CTkLabel(master=self.transaction_frame, text="Montant :", font=self.text_font, text_color=SOFT_YELLOW, bg_color=DARK_BLUE, justify="left", anchor="w")
        self.transaction_frame.amount_text.grid(row=row1, column=0, sticky="sew", padx=20, pady=5)

        self.transaction_frame.amount_box = customtkinter.CTkTextbox(master=self.transaction_frame, font=self.text_font, width=200, height=48, corner_radius=10, bg_color= DARK_BLUE, fg_color= SOFT_YELLOW, text_color = DARK_BLUE) # champs "email"
        self.transaction_frame.amount_box.grid(row=row2, column=0, sticky="sew", padx=20, pady=0)
        self.transaction_frame.amount_box.insert("0.0", "")

    def screen_build(self):
        self.transaction_frame.title_text = customtkinter.CTkLabel(master=self.transaction_frame, text="Budget Buddy", font=self.title_font, text_color=YELLOW, bg_color=DARK_BLUE)
        self.transaction_frame.title_text.grid(row=0, column=0, sticky="sew", padx=20, pady=0)

        self.transaction_frame.subtitle_text = customtkinter.CTkLabel(master=self.transaction_frame, text="Transactions".upper(), font=self.subtitle_font, text_color=YELLOW, bg_color=DARK_BLUE)
        self.transaction_frame.subtitle_text.grid(row=1, column=0, sticky="sew", padx=20, pady=0)

        self.build_type_field(2, 3)
        self.build_category_field(4, 5)
        self.get_fields_deposit_withdrawal()

        self.display_field_from_type(self.transaction_info.get_type())

        self.build_date_entry(8, 9)
        self.build_description(10, 11)
        self.build_amount_field(12, 13)
        self.transaction_frame.button = customtkinter.CTkButton(master=self.transaction_frame, text="Confirmer la transaction".upper(), font=self.text_font, command=self.confirm_form_callback, corner_radius=7, bg_color= DARK_BLUE, fg_color = PINK) # bouton se connecter
        self.transaction_frame.button.grid(row=15, column=0, sticky="snew", padx=20, pady=(20,5))
        self.transaction_frame.button_return = customtkinter.CTkButton(master=self.transaction_frame, text="Retour".upper(), font=self.text_font, command=self.return_button_callbck, corner_radius=7, bg_color= DARK_BLUE, fg_color = PINK) # bouton se connecter
        self.transaction_frame.button_return.grid(row=16, column=0, sticky="snew", padx=20, pady=5)

    def return_button_callbck(self):
        self.destroy()
    
    def login_screen_destroy(self):
        self.email_text.destroy()
        self.email_box.destroy()
        self.password_text.destroy()
        self.password_box.destroy()
        self.subtitle_text.destroy()
        self.button_create_account.destroy()
        self.button.destroy()
    
    def interface_screen_build(self):
        self.button = customtkinter.CTkButton(self, text="Se déconnecter".upper(), font=self.text_font, command=self.button_callbck_logout, corner_radius=10, bg_color=DARK_BLUE, fg_color = PINK)
        self.button.grid(row=1, column=0, padx=20, pady=20)

    def interface_screen_destroy(self):
        self.button.destroy()

    def button_callbck(self):
        print("Connexion réussie")
        self.login_screen_destroy()
        self.interface_screen_build()
        self.confirmed = True

    def button_callbck_logout(self):
        print("Déconnexion réussie")
        self.interface_screen_destroy()
        self.login_screen_build()
        # self.confirmed = True
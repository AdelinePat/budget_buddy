import customtkinter
from tkcalendar import Calendar, DateEntry
import re
from view.interface import Interface
from view.scrollable_frame import Scrollable_frame
from view.__settings__ import DARK_BLUE, SOFT_BLUE,\
                            LIGHT_BLUE, YELLOW, SOFT_YELLOW,\
                            PINK, SOFT_BLUE2, SOFT_BLUE3,\
                            DEAL_TYPE_LIST, CATEGORY_LIST
from model.transactioninfo import TransactionInfo
from model.customexception import TransactionException
from controller.transactionmanager import TransactionManager
from data_access.read_data_access import DataAccess

class TransactionView(Interface): 
    def __init__(self, window_title, column_number, current_session, current_account):
        super().__init__(window_title, column_number)
        self.controller = TransactionManager()
        self.__data_access = DataAccess()

        self.scrollable_frame = Scrollable_frame(self, bg_color=DARK_BLUE, fg_color=DARK_BLUE)
        self.scrollable_frame.columnconfigure(0, weight=1)
        self.scrollable_frame.pack(fill='both', expand=1)

        self.deal_type_list = DEAL_TYPE_LIST
        self.category_list = CATEGORY_LIST
        self.transaction_info = TransactionInfo(current_session, current_account, "", "", None, None, "", "", "")
        self.get_actual_account_id_from_string()
        
        self.__accounts_list = self.__data_access.get_all_accounts_from_user(self.transaction_info.get_current_session())
        self.__accounts_list_string = self.get_accounts_list_string()
        self.last_choice = ""
        self.screen_build()

    def get_actual_account_id_from_string(self):
        id = self.transaction_info.get_current_account()

        id_regex = re.search(r"^(\d)+", id)
        final_id = id_regex.group()
        final_id = int(final_id)

        self.transaction_info.set_current_account(final_id)

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
                self.scrollable_frame.receiver_label.destroy()
                self.scrollable_frame.receiver_choice.destroy()
            self.build_receiver_field(6, 7)
        elif deal_type == 'Transfert':
            if self.last_choice == 'Virement':
                self.scrollable_frame.receiver_text.destroy()
                self.scrollable_frame.receiver_box.destroy()
            self.build_internal_receiver_field(6, 7)
        else:
            if self.last_choice == 'Virement':
                self.scrollable_frame.receiver_text.destroy()
                self.scrollable_frame.receiver_box.destroy()
                print("devrait détruire le bénéficiaire du virement")
            elif self.last_choice == 'Transfert':
                self.scrollable_frame.receiver_label.destroy()
                self.scrollable_frame.receiver_choice.destroy()
                print("devrait détruire le bénéficiaire du transfert")

    def category_callback(self, choice):
        self.transaction_info.set_category(choice)

    def deal_date_callback(self, choice):
        self.transaction_info.set_date(choice)

    def confirm_form_callback(self):

        self.get_fields_deposit_withdrawal()

        self.transaction_info.set_date(self.scrollable_frame.chose_date.get_date())
        self.transaction_info.set_type(self.scrollable_frame.deal_type_choice.get().strip())

        self.transaction_info.set_description(self.scrollable_frame.description_box.get("0.0", "end").strip())

        self.transaction_info.set_amount(self.scrollable_frame.amount_box.get("0.0", "end"))
        self.transaction_info.set_category(self.scrollable_frame.category_choice.get())

        if self.transaction_info.get_type() == 'Virement':
            self.transaction_info.set_receiver(self.scrollable_frame.receiver_box.get("0.0", "end").strip())
        elif self.transaction_info.get_type() == 'Transfert':
            self.transaction_info.set_receiver(self.scrollable_frame.receiver_choice.get())
        try:
            if hasattr(self.scrollable_frame, 'error_message_text'):
                self.scrollable_frame.error_message_text.destroy()
            self.controller.manage_transaction(self.transaction_info)
            self.build_transaction_result("Transaction réussie")
        except TransactionException as e:
            self.build_transaction_result(e)

    def build_transaction_result(self, error_message):
        self.scrollable_frame.error_message_text = customtkinter.CTkLabel(master=self.scrollable_frame, text=error_message, font=self.text_font, text_color=SOFT_BLUE, bg_color=DARK_BLUE)
        self.scrollable_frame.error_message_text.grid(row=14, column=0, sticky="sn", padx=20, pady=5)

    def get_fields_deposit_withdrawal(self):
        if self.transaction_info.get_type() == 'Dépôt':
            self.transaction_info.set_receiver(self.transaction_info.get_current_account())
            self.transaction_info.set_emitter(None)
        else:
            self.transaction_info.set_receiver(None)
            self.transaction_info.set_emitter(self.transaction_info.get_current_account())

    def build_type_field(self, row1, row2):
        self.scrollable_frame.deal_type_text = customtkinter.CTkLabel(master=self.scrollable_frame, text="Choisissez le type de transaction :", font=self.text_font, text_color=SOFT_YELLOW, bg_color=DARK_BLUE, justify="left", anchor="w")
        self.scrollable_frame.deal_type_text.grid(row=row1, column=0, sticky="sew", padx=20, pady=5)

        self.scrollable_frame.deal_type_choice = customtkinter.CTkComboBox(master=self.scrollable_frame,
            values=self.deal_type_list, state="readonly",
            command=self.deal_type_callback, font=self.text_font, text_color=DARK_BLUE,
            bg_color=DARK_BLUE, fg_color=SOFT_YELLOW, dropdown_fg_color = SOFT_YELLOW, 
            dropdown_text_color = DARK_BLUE, dropdown_font= self.text_font,
            dropdown_hover_color = SOFT_BLUE, corner_radius=10)

        self.scrollable_frame.deal_type_choice.grid(row=row2, column=0, sticky="sew", padx=20, pady=0)
        self.scrollable_frame.deal_type_choice.set(self.deal_type_list[-1])

        self.transaction_info.set_type(self.scrollable_frame.deal_type_choice.get())
        print(f"dropdown type avant callback: {self.transaction_info.get_type()}")
    
    def build_category_field(self, row1, row2):
        category_text = customtkinter.CTkLabel(master=self.scrollable_frame, text="Choisissez la catégorie de votre transaction :", font=self.text_font, text_color=SOFT_YELLOW, bg_color=DARK_BLUE, justify="left", anchor="w")
        category_text.grid(row=row1, column=0, sticky="sew", padx=20, pady=5)

        self.scrollable_frame.category_choice = customtkinter.CTkComboBox(master=self.scrollable_frame,
            values=self.category_list, state="readonly", command=self.category_callback,
            font=self.text_font, text_color=DARK_BLUE, bg_color=DARK_BLUE, fg_color=SOFT_YELLOW,
            dropdown_fg_color = SOFT_YELLOW, dropdown_text_color = DARK_BLUE,
            dropdown_font= self.text_font, dropdown_hover_color = SOFT_BLUE,
            corner_radius=10)

        self.scrollable_frame.category_choice.grid(row=row2, column=0, sticky="sew", padx=20, pady=0)
        self.scrollable_frame.category_choice.set(self.category_list[-1])
        self.transaction_info.set_category(self.scrollable_frame.category_choice.get())
        print(f"dropdown categorie avant callback: {self.transaction_info.get_type()}")
     
    def build_date_entry(self, row1, row2):
        self.scrollable_frame.deal_date_text = customtkinter.CTkLabel(master=self.scrollable_frame, text="Choisissez la date de votre transaction :", font=self.text_font, text_color=SOFT_YELLOW, bg_color=DARK_BLUE, justify="left", anchor="w")
        self.scrollable_frame.deal_date_text.grid(row=row1, column=0, sticky="sew", padx=20, pady=5)
        self.scrollable_frame.chose_date = DateEntry(master=self.scrollable_frame, date_pattern="yyyy-mm-dd",
            font=self.text_font, text_color=DARK_BLUE, bg_color=DARK_BLUE, fg_color=SOFT_YELLOW,
            dropdown_fg_color = SOFT_YELLOW, dropdown_text_color = DARK_BLUE,
            dropdown_font= self.text_font,
            borderwidth=2, bordercolor=DARK_BLUE,
            background=DARK_BLUE, foreground=SOFT_YELLOW, headersbackground=PINK,
            selectbackground=PINK, normalbackground=LIGHT_BLUE, weekendbackground=SOFT_BLUE, corner_radius=10,
            othermonthbackground=SOFT_BLUE2, othermonthwebackground=SOFT_BLUE3, othermonthforeground=DARK_BLUE, othermonthweforeground=DARK_BLUE)
        self.scrollable_frame.chose_date.grid(row=row2, column=0, sticky="sew", padx=20, pady=5)

    def build_calendar(self, row1, row2):
        self.scrollable_frame.deal_date_text = customtkinter.CTkLabel(master=self.scrollable_frame, text="Choisissez la date de votre transaction :", font=self.text_font, text_color=SOFT_YELLOW, bg_color=DARK_BLUE, justify="left", anchor="w")
        self.scrollable_frame.deal_date_text.grid(row=row1, column=0, sticky="sew", padx=20, pady=5)

        self.scrollable_frame.chose_date = Calendar(master=self.scrollable_frame, selectmode='day', font=self.text_font,
            command=self.deal_date_callback,
            showweeknumbers=False, cursor="hand2", date_pattern= 'y-mm-dd',
            borderwidth=2, bordercolor=DARK_BLUE,
            background=DARK_BLUE, foreground=SOFT_YELLOW, headersbackground=PINK,
            selectbackground=PINK, normalbackground=LIGHT_BLUE, weekendbackground=SOFT_BLUE, corner_radius=10,
            othermonthbackground=SOFT_BLUE2, othermonthwebackground=SOFT_BLUE3, othermonthforeground=DARK_BLUE, othermonthweforeground=DARK_BLUE
            )
        
        self.scrollable_frame.chose_date.grid(row=row2,column=0, padx=30, pady=10, sticky='sew')

    def build_description(self, row1, row2):
        self.scrollable_frame.description_text = customtkinter.CTkLabel(master=self.scrollable_frame, text="Description de la transaction :", font=self.text_font, text_color=SOFT_YELLOW, bg_color=DARK_BLUE, justify="left", anchor="w")
        self.scrollable_frame.description_text.grid(row=row1, column=0, sticky="sew", padx=20, pady=5)

        self.scrollable_frame.description_box = customtkinter.CTkTextbox(master=self.scrollable_frame, font=self.text_font, width=200, height=48, corner_radius=10, bg_color= DARK_BLUE, fg_color= SOFT_YELLOW, text_color = DARK_BLUE) # champs "email"
        self.scrollable_frame.description_box.grid(row=row2, column=0, sticky="sew", padx=20, pady=0)
        self.scrollable_frame.description_box.insert("0.0", "")

    def build_receiver_field(self, row1, row2):
        self.scrollable_frame.receiver_text = customtkinter.CTkLabel(master=self.scrollable_frame, text="Bénéficiaire (email) :", font=self.text_font, text_color=SOFT_YELLOW, bg_color=DARK_BLUE, justify="left", anchor="w")
        self.scrollable_frame.receiver_text.grid(row=row1, column=0, sticky="sew", padx=20, pady=5)

        self.scrollable_frame.receiver_box = customtkinter.CTkTextbox(master=self.scrollable_frame, font=self.text_font, width=200, height=48, corner_radius=10, bg_color= DARK_BLUE, fg_color= SOFT_YELLOW, text_color = DARK_BLUE) # champs "email"
        self.scrollable_frame.receiver_box.grid(row=row2, column=0, sticky="sew", padx=20, pady=0)
        self.scrollable_frame.receiver_box.insert("0.0", "")

    def build_internal_receiver_field(self, row1, row2):
        self.scrollable_frame.receiver_label = customtkinter.CTkLabel(master=self.scrollable_frame, text="Choisissez le compte bénéficiaire :", font=self.text_font, text_color=SOFT_YELLOW, bg_color=DARK_BLUE, justify="left", anchor="w")
        self.scrollable_frame.receiver_label.grid(row=row1, column=0, sticky="sew", padx=20, pady=5)

        self.scrollable_frame.receiver_choice = customtkinter.CTkComboBox(master=self.scrollable_frame,
            values=self.__accounts_list_string, state="readonly",
            command=self.deal_receiver_callback, font=self.text_font, text_color=DARK_BLUE,
            bg_color=DARK_BLUE, fg_color=SOFT_YELLOW, dropdown_fg_color = SOFT_YELLOW, 
            dropdown_text_color = DARK_BLUE, dropdown_font= self.text_font,
            dropdown_hover_color = SOFT_BLUE, corner_radius=10)

        self.scrollable_frame.receiver_choice.grid(row=row2, column=0, sticky="sew", padx=20, pady=0)
        self.scrollable_frame.receiver_choice.set(self.__accounts_list_string[0])

    def build_amount_field(self, row1, row2):
        self.scrollable_frame.amount_text = customtkinter.CTkLabel(master=self.scrollable_frame, text="Montant :", font=self.text_font, text_color=SOFT_YELLOW, bg_color=DARK_BLUE, justify="left", anchor="w")
        self.scrollable_frame.amount_text.grid(row=row1, column=0, sticky="sew", padx=20, pady=5)

        self.scrollable_frame.amount_box = customtkinter.CTkTextbox(master=self.scrollable_frame, font=self.text_font, width=200, height=48, corner_radius=10, bg_color= DARK_BLUE, fg_color= SOFT_YELLOW, text_color = DARK_BLUE) # champs "email"
        self.scrollable_frame.amount_box.grid(row=row2, column=0, sticky="sew", padx=20, pady=0)
        self.scrollable_frame.amount_box.insert("0.0", "")

    def screen_build(self):
        self.scrollable_frame.title_text = customtkinter.CTkLabel(master=self.scrollable_frame, text="Budget Buddy", font=self.title_font, text_color=YELLOW, bg_color=DARK_BLUE)
        self.scrollable_frame.title_text.grid(row=0, column=0, sticky="sew", padx=20, pady=0)

        self.scrollable_frame.subtitle_text = customtkinter.CTkLabel(master=self.scrollable_frame, text="Transactions".upper(), font=self.subtitle_font, text_color=YELLOW, bg_color=DARK_BLUE)
        self.scrollable_frame.subtitle_text.grid(row=1, column=0, sticky="sew", padx=20, pady=0)

        self.build_type_field(2, 3)
        self.build_category_field(4, 5)
        self.get_fields_deposit_withdrawal()

        self.display_field_from_type(self.transaction_info.get_type())

        self.build_date_entry(8, 9)
        self.build_description(10, 11)
        self.build_amount_field(12, 13)
        self.scrollable_frame.button = customtkinter.CTkButton(master=self.scrollable_frame, text="Confirmer la transaction".upper(), font=self.text_font, command=self.confirm_form_callback, corner_radius=7, bg_color= DARK_BLUE, fg_color = PINK) # bouton se connecter
        self.scrollable_frame.button.grid(row=15, column=0, sticky="snew", padx=20, pady=(20,5))
        self.scrollable_frame.button_return = customtkinter.CTkButton(master=self.scrollable_frame, text="Retour".upper(), font=self.text_font, command=self.return_button_callbck, corner_radius=7, bg_color= DARK_BLUE, fg_color = PINK) # bouton se connecter
        self.scrollable_frame.button_return.grid(row=16, column=0, sticky="snew", padx=20, pady=5)

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
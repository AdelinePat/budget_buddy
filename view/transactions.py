import customtkinter
# import tkcalendar
# from CTkDatePicker import CTkDatePicker
from tkcalendar import Calendar
# from CTkDatePicker import CTkDatePicker
from view.interface import Interface
from view.__settings__ import DARK_BLUE, SOFT_BLUE, LIGHT_BLUE, YELLOW, SOFT_YELLOW, PINK, DARK_PINK

class TransactionView(Interface):
    def __init__(self,window_title, column_number, current_session):
        super().__init__(window_title, column_number)
        self.deal_type_list = ['Retrait', 'Dépôt', 'Transfert']
        self.category_list = ['Alimentaire', 'Loisirs', 'Prélèvement', 'Transport', 'Santé', 'Dealing', 'Activités illicites', 'Consommation de café']
        self.type_selected = ""
        self.date_selected = ""
        self.current_session = current_session
        self.emitter = ""
        self.receiver = ""
        self.deal_description = ""
        self.category = ""
        self.last_choice = "Transfert"
        self.amount = 0
        self.get_fields_deposit_withdrawal()

        self.screen_build()
    
    def deal_type_callback(self, choice):
        if self.last_choice == 'Transfert' and self.type_selected != 'Transfert':
            self.receiver_text.destroy()
            self.receiver_box.destroy()
            self.last_choice = self.type_selected

        self.type_selected = choice
        if self.type_selected == 'Transfert':
            self.build_receiver_field(6, 7)
        else:
            if bool(self.receiver_text):
                self.receiver_text.destroy()
                self.receiver_box.destroy()
        print(self.type_selected)
    
    def category_callback(self, choice):
        self.category = choice

    def deal_date_callback(self, choice):
        self.date_selected = choice
        print(self.date_selected)

    def confirm_form_callback(self):

        self.get_fields_deposit_withdrawal()

        self.date_selected = self.chose_date.get_date()
        self.type_selected = self.deal_type_choice.get()
        self.description = self.description_box.get("0.0", "end")
        if self.type_selected == 'Transfert':
            self.receiver = self.receiver_box.get("0.0", "end")
        self.amount = self.amount_box.get("0.0", "end")
        self.category = self.category_choice.get()
        
        
        print(f"type : {self.type_selected}\n"
             f"date : {self.date_selected}\n"
             f"catégorie : {self.category}\n"
             f"émetteur : {self.emitter}\n"
             f"récepteur : {self.receiver}\n"
             f"description : {self.description}\n"
             f"montant : {self.amount}")

    def generate_form(self):
        pass

    def get_fields_deposit_withdrawal(self):
        if self.type_selected == 'Dépôt':
            self.receiver = self.current_session
            self.emitter = ""
        else:
            self.receiver = ""
            self.emitter = self.current_session
            
# id_account_emitter, OK
# id_account_receiver, OK
# deal_description, OK
# amount, 
# deal_date, OK
# deal_type, OK
# frequency,
# category, 
# charges
    def build_type_field(self, row1, row2):
        self.deal_type_text = customtkinter.CTkLabel(master=self, text="Choisissez le type de transaction :", font=self.text_font, text_color=SOFT_YELLOW, bg_color=DARK_BLUE, justify="left", anchor="w")
        self.deal_type_text.grid(row=row1, column=0, sticky="sew", padx=20, pady=5)

        self.deal_type_choice = customtkinter.CTkComboBox(master=self,
            values=self.deal_type_list, state="readonly",
            command=self.deal_type_callback, font=self.text_font, text_color=DARK_BLUE,
            bg_color=DARK_BLUE, fg_color=SOFT_YELLOW, dropdown_fg_color = SOFT_YELLOW, 
            dropdown_text_color = DARK_BLUE, dropdown_font= self.text_font,
            dropdown_hover_color = SOFT_BLUE, corner_radius=10)

        self.deal_type_choice.grid(row=row2, column=0, sticky="sew", padx=20, pady=0)
        self.deal_type_choice.set(self.deal_type_list[-1])
        self.type_selected = self.deal_type_choice.get()
    
    def build_category_field(self, row1, row2):
        category_text = customtkinter.CTkLabel(master=self, text="Choisissez la catégorie de votre transaction :", font=self.text_font, text_color=SOFT_YELLOW, bg_color=DARK_BLUE, justify="left", anchor="w")
        category_text.grid(row=row1, column=0, sticky="sew", padx=20, pady=5)

        self.category_choice = customtkinter.CTkComboBox(master=self,
            values=self.category_list, state="readonly", command=self.category_callback,
            font=self.text_font, text_color=DARK_BLUE, bg_color=DARK_BLUE, fg_color=SOFT_YELLOW,
            dropdown_fg_color = SOFT_YELLOW, dropdown_text_color = DARK_BLUE,
            dropdown_font= self.text_font, dropdown_hover_color = SOFT_BLUE,
            corner_radius=10)

        self.category_choice.grid(row=row2, column=0, sticky="sew", padx=20, pady=0)
        self.category_choice.set(self.category_list[-1])
        
    
    def build_calendar(self, row1, row2):
        self.deal_date_text = customtkinter.CTkLabel(master=self, text="Choisissez la date de votre transactions :", font=self.text_font, text_color=SOFT_YELLOW, bg_color=DARK_BLUE, justify="left", anchor="w")
        self.deal_date_text.grid(row=row1, column=0, sticky="sew", padx=20, pady=5)

        self.chose_date = Calendar(master=self, selectmode='day', font=self.text_font,
            command=self.deal_date_callback,
            showweeknumbers=False, cursor="hand2", date_pattern= 'y-mm-dd',
            borderwidth=2, bordercolor=DARK_BLUE,
            background=DARK_BLUE, foreground=SOFT_YELLOW, headersbackground=PINK,
            selectbackground=PINK, normalbackground=LIGHT_BLUE, weekendbackground=SOFT_BLUE, corner_radius=10,
            othermonthbackground="grey", othermonthwebackground=SOFT_BLUE, othermonthforeground="white", othermonthweforeground="white"
            )
        
        self.chose_date.grid(row=row2,column=0, padx=30, pady=10, sticky='sew')

    def build_description(self, row1, row2):
        self.description_text = customtkinter.CTkLabel(master=self, text="Description de la transaction :", font=self.text_font, text_color=SOFT_YELLOW, bg_color=DARK_BLUE, justify="left", anchor="w")
        self.description_text.grid(row=row1, column=0, sticky="sew", padx=20, pady=5)

        self.description_box = customtkinter.CTkTextbox(master=self, font=self.text_font, width=200, height=48, corner_radius=10, bg_color= DARK_BLUE, fg_color= SOFT_YELLOW, text_color = DARK_BLUE) # champs "email"
        self.description_box.grid(row=row2, column=0, sticky="sew", padx=20, pady=0)
        self.description_box.insert("0.0", "")

    def build_receiver_field(self, row1, row2):
        self.receiver_text = customtkinter.CTkLabel(master=self, text="Bénéficiaire (email) :", font=self.text_font, text_color=SOFT_YELLOW, bg_color=DARK_BLUE, justify="left", anchor="w")
        self.receiver_text.grid(row=row1, column=0, sticky="sew", padx=20, pady=5)

        self.receiver_box = customtkinter.CTkTextbox(master=self, font=self.text_font, width=200, height=48, corner_radius=10, bg_color= DARK_BLUE, fg_color= SOFT_YELLOW, text_color = DARK_BLUE) # champs "email"
        self.receiver_box.grid(row=row2, column=0, sticky="sew", padx=20, pady=0)
        self.receiver_box.insert("0.0", "")

    def build_amount_field(self, row1, row2):
        self.amount_text = customtkinter.CTkLabel(master=self, text="Montant :", font=self.text_font, text_color=SOFT_YELLOW, bg_color=DARK_BLUE, justify="left", anchor="w")
        self.amount_text.grid(row=row1, column=0, sticky="sew", padx=20, pady=5)

        self.amount_box = customtkinter.CTkTextbox(master=self, font=self.text_font, width=200, height=48, corner_radius=10, bg_color= DARK_BLUE, fg_color= SOFT_YELLOW, text_color = DARK_BLUE) # champs "email"
        self.amount_box.grid(row=row2, column=0, sticky="sew", padx=20, pady=0)
        self.amount_box.insert("0.0", "")

    def screen_build(self):
        self.title_text = customtkinter.CTkLabel(master=self, text="Budget Buddy", font=self.title_font, text_color=YELLOW, bg_color=DARK_BLUE)
        self.title_text.grid(row=0, column=0, sticky="sew", padx=20, pady=0)

        self.subtitle_text = customtkinter.CTkLabel(master=self, text="Transactions", font=self.text_font, text_color=YELLOW, bg_color=DARK_BLUE)
        self.subtitle_text.grid(row=1, column=0, sticky="sew", padx=20, pady=0)

        self.build_type_field(2, 3)
        self.build_category_field(4, 5)
        # if self.type_selected == 'Transfert':
        #     self.build_receiver_field(6, 7)
        self.build_calendar(8, 9)
        self.build_description(10, 11)
        self.build_amount_field(12, 13)

        

        self.button = customtkinter.CTkButton(self, text="Confirmer la transaction".upper(), font=self.text_font, command=self.confirm_form_callback, corner_radius=7, bg_color= DARK_BLUE, fg_color = PINK) # bouton se connecter
        self.button.grid(row=14, column=0, padx=20, pady=20)

        # self.button_create_account = customtkinter.CTkButton(self, text="Créer un compte".upper(), font=self.text_font, command=self.button_callbck, corner_radius=7, bg_color= DARK_BLUE, fg_color = PINK) # bouton se connecter
        # self.button_create_account.grid(row=8, column=0, padx=20, pady=20)
        
    
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
import customtkinter
# import tkcalendar
# from CTkDatePicker import CTkDatePicker
from tkcalendar import Calendar
# from CTkDatePicker import CTkDatePicker
from view.interface import Interface
from view.__settings__ import DARK_BLUE, SOFT_BLUE, LIGHT_BLUE, YELLOW, SOFT_YELLOW, PINK

class TransactionView(Interface):
    def __init__(self,window_title, column_number):
        super().__init__(window_title, column_number)
        self.deal_type_list = ['Retrait', 'Dépôt', 'Transfert']
        self.type_selected = ""
        self.date_selected = ""

        self.screen_build()
    
    def deal_type_callback(self, choice):
        self.type_selected = choice
        print(self.type_selected)

    def deal_date_callback(self, choice):
        # self.date_selected = self.chose_date.get_date()
        self.date_selected = choice
        print(self.date_selected)

    def confirm_form_callback(self):
        self.date_selected = self.chose_date.get_date()
        self.type_selected = self.type_selected

        print(self.date_selected, self.type_selected)

    def screen_build(self):
        self.title_text = customtkinter.CTkLabel(master=self, text="Budget Buddy", font=self.title_font, text_color=YELLOW, bg_color=DARK_BLUE)
        self.title_text.grid(row=0, column=0, sticky="sew", padx=20, pady=0)

        self.subtitle_text = customtkinter.CTkLabel(master=self, text="Transactions", font=self.text_font, text_color=YELLOW, bg_color=DARK_BLUE)
        self.subtitle_text.grid(row=1, column=0, sticky="sew", padx=20, pady=0)

        self.deal_type_text = customtkinter.CTkLabel(master=self, text="Choisissez le type de transaction :", font=self.text_font, text_color=SOFT_YELLOW, bg_color=DARK_BLUE, justify="left", anchor="w")
        self.deal_type_text.grid(row=2, column=0, sticky="sew", padx=20, pady=5)

        self.deal_type_choice = customtkinter.CTkComboBox(master=self,
                                    values=self.deal_type_list,
                                    state="readonly",
                                    command=self.deal_type_callback,
                                    font=self.text_font, text_color=DARK_BLUE, bg_color=DARK_BLUE, fg_color=SOFT_YELLOW,
                                    dropdown_fg_color = SOFT_YELLOW, dropdown_text_color = DARK_BLUE, dropdown_font= self.text_font,
                                    dropdown_hover_color = SOFT_BLUE
                                    )

        self.deal_type_choice.grid(row=3, column=0, sticky="sew", padx=20, pady=0)
        self.deal_type_choice.set(self.deal_type_list[1])


        self.deal_date_text = customtkinter.CTkLabel(master=self, text="Choisissez la date de votre transactions :", font=self.text_font, text_color=SOFT_YELLOW, bg_color=DARK_BLUE, justify="left", anchor="w")
        self.deal_date_text.grid(row=4, column=0, sticky="sew", padx=20, pady=5)

        self.chose_date = Calendar(master=self, selectmode='day', font=self.text_font,
            command=self.deal_date_callback,
            showweeknumbers=False, cursor="hand2", date_pattern= 'y-mm-dd',
            borderwidth=0, bordercolor='white',
            background=DARK_BLUE, foreground="red", headersbackground=SOFT_BLUE)
        
        self.chose_date.grid(row= 6,column=0, padx=30, pady=10, sticky='sew')
        # print(f"date choisie ?? : {self.chose_date.get_date()}")
        # self.date_selected = self.chose_date.get_date()
        print(f"test : {self.date_selected}")

        # self.email_box = customtkinter.CTkTextbox(master=self, font=self.text_font, width=200, height=48, corner_radius=10, bg_color= DARK_BLUE, fg_color= SOFT_YELLOW, text_color = DARK_BLUE) # champs "email"
        # self.email_box.grid(row=3, column=0, sticky="sew", padx=20, pady=0)
        # self.email_box.insert("0.0", "")


        # self.password_text = customtkinter.CTkLabel(master=self, text="Votre mot de passe :", font=self.text_font, text_color=SOFT_YELLOW, bg_color=DARK_BLUE, justify="left", anchor="w")
        # self.password_text.grid(row=4, column=0, sticky="sew", padx=20, pady=5)

        # self.password_box = customtkinter.CTkTextbox(master=self, font=self.text_font, width=200, height=48, corner_radius=10, bg_color= DARK_BLUE, fg_color= SOFT_YELLOW, text_color = DARK_BLUE) # champs "email"
        # self.password_box.grid(row=5, column=0, sticky="sew", padx=20, pady=0)
        # self.password_box.insert("0.0", "")

        self.button = customtkinter.CTkButton(self, text="Confirmer la transaction".upper(), font=self.text_font, command=self.confirm_form_callback, corner_radius=7, bg_color= DARK_BLUE, fg_color = PINK) # bouton se connecter
        self.button.grid(row=7, column=0, padx=20, pady=20)

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
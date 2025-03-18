import customtkinter
# import tkcalendar
from CTkDatePicker import CTkDatePicker
from view.interface import Interface
from view.__settings__ import DARK_BLUE, SOFT_BLUE, LIGHT_BLUE, YELLOW, SOFT_YELLOW, PINK

class TransactionView(Interface):
    def __init__(self,window_title, column_number):
        super().__init__(window_title, column_number)
        self.screen_build()
    
    def deal_type_callback(choice):
        print("DEAL TYPE : combobox dropdown clicked:")

    def screen_build(self):
        self.title_text = customtkinter.CTkLabel(master=self, text="Budget Buddy", font=self.title_font, text_color=YELLOW, bg_color=DARK_BLUE)
        self.title_text.grid(row=0, column=0, sticky="sew", padx=20, pady=0)

        self.subtitle_text = customtkinter.CTkLabel(master=self, text="Transactions", font=self.text_font, text_color=YELLOW, bg_color=DARK_BLUE)
        self.subtitle_text.grid(row=1, column=0, sticky="sew", padx=20, pady=0)

        self.deal_type_text = customtkinter.CTkLabel(master=self, text="Choisissez le type de transaction :", font=self.text_font, text_color=SOFT_YELLOW, bg_color=DARK_BLUE, justify="left", anchor="w")
        self.deal_type_text.grid(row=2, column=0, sticky="sew", padx=20, pady=5)

        self.deal_type_choice = customtkinter.CTkComboBox(master=self,
                                    values=['Retrait', 'Dépôt', 'Transfert'],
                                    command=self.deal_type_callback(),
                                    font=self.text_font, text_color=DARK_BLUE, bg_color=DARK_BLUE, fg_color=SOFT_YELLOW,
                                    dropdown_fg_color = SOFT_YELLOW, dropdown_text_color = DARK_BLUE, dropdown_font= self.text_font,
                                    dropdown_hover_color = SOFT_BLUE
                                    )
        
        self.deal_type_choice.grid(row=3, column=0, sticky="sew", padx=20, pady=0)
        self.deal_type_choice.set("Dépôt")

        self.chose_date = 

        # self.email_box = customtkinter.CTkTextbox(master=self, font=self.text_font, width=200, height=48, corner_radius=10, bg_color= DARK_BLUE, fg_color= SOFT_YELLOW, text_color = DARK_BLUE) # champs "email"
        # self.email_box.grid(row=3, column=0, sticky="sew", padx=20, pady=0)
        # self.email_box.insert("0.0", "")


        self.password_text = customtkinter.CTkLabel(master=self, text="Votre mot de passe :", font=self.text_font, text_color=SOFT_YELLOW, bg_color=DARK_BLUE, justify="left", anchor="w")
        self.password_text.grid(row=4, column=0, sticky="sew", padx=20, pady=5)

        self.password_box = customtkinter.CTkTextbox(master=self, font=self.text_font, width=200, height=48, corner_radius=10, bg_color= DARK_BLUE, fg_color= SOFT_YELLOW, text_color = DARK_BLUE) # champs "email"
        self.password_box.grid(row=5, column=0, sticky="sew", padx=20, pady=0)
        self.password_box.insert("0.0", "")

        self.button = customtkinter.CTkButton(self, text="Se connecter".upper(), font=self.text_font, command=self.button_callbck, corner_radius=7, bg_color= DARK_BLUE, fg_color = PINK) # bouton se connecter
        self.button.grid(row=7, column=0, padx=20, pady=20)

        self.button_create_account = customtkinter.CTkButton(self, text="Créer un compte".upper(), font=self.text_font, command=self.button_callbck, corner_radius=7, bg_color= DARK_BLUE, fg_color = PINK) # bouton se connecter
        self.button_create_account.grid(row=8, column=0, padx=20, pady=20)
    
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
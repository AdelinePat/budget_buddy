import customtkinter
# import tkinter
# import time
from model.server import ServerDatabase
import re
import bcrypt
# import sqlite3
from data_access.read_user_data import UserDataAcess

from view.scrollable_frame import Scrollable_frame

from controller.login_data_manager import LoginManager
from model.login_info import LoginInfo
from model.customexception import LogInDataException
from view.__settings__ import DARK_BLUE, SOFT_BLUE, LIGHT_BLUE, YELLOW, SOFT_YELLOW, PINK
from model.server import ServerDatabase
# from view.utiltool import UtilTool
from view.interface import Interface

class LogInOut(Interface):
    def __init__(self, window_title, column_number, connected):
        super().__init__(window_title, column_number)
        self.controller = LoginManager()
        self.password_visible = False
        self.connected = connected
        self.eye_open, self.eye_closed = self.util.get_eye_icons()
        self.log_info = LoginInfo()
        self.database = ServerDatabase()

        self.scrollable_frame = Scrollable_frame(self, bg_color=DARK_BLUE, fg_color=DARK_BLUE)
        self.scrollable_frame.columnconfigure(0, weight=1)
        self.scrollable_frame.pack(fill='both', expand=1)

        self.login_screen_build()
        self.lift() 
        self.attributes("-topmost", True)
        self.__data_acces = UserDataAcess()
        self.__all_users = self.__data_acces.get_all_users()


    def login_screen_build(self):
        # self.title_text = customtkinter.CTkLabel(master=self, text="Budget Buddy", font=self.text_font, text_color=SOFT_YELLOW, bg_color=DARK_BLUE, justify="left", anchor="w")
        # self.title_text.grid(row=0, column=0, sticky="sew", padx=20, pady=0)

        # self.scrollable_frame.title_text = customtkinter.CTkLabel(master=self, text="Votre application bancaire préférée", font=self.text_font, text_color=SOFT_YELLOW, bg_color=DARK_BLUE, justify="left", anchor="w")
        # self.scrollable_frame.title_text.grid(row=1, column=0, sticky="sew", padx=20, pady=0)


        self.scrollable_frame.title_text = customtkinter.CTkLabel(master=self.scrollable_frame, text="Budget Buddy", font=self.title_font, text_color=YELLOW, bg_color=DARK_BLUE)
        self.scrollable_frame.title_text.grid(row=0, column=0, sticky="sew", padx=20, pady=(20,10))

        self.scrollable_frame.title_text = customtkinter.CTkLabel(master=self.scrollable_frame, text="Votre application bancaire préférée".upper(), font=self.subtitle_font, text_color=YELLOW, bg_color=DARK_BLUE)
        self.scrollable_frame.title_text.grid(row=1, column=0, sticky="sew", padx=20, pady=(5,20))


        self.scrollable_frame.email_entry = customtkinter.CTkLabel(master=self.scrollable_frame, text="Votre adresse email :", font=self.text_font, text_color=SOFT_YELLOW, bg_color=DARK_BLUE, justify="left", anchor="w")
        self.scrollable_frame.email_entry.grid(row=2, column=0, sticky="sew", padx=20, pady=(5,2))

        self.scrollable_frame.email_box = customtkinter.CTkTextbox(master=self.scrollable_frame, font=self.text_font, width=200, height=48, corner_radius=10, bg_color= DARK_BLUE, fg_color= SOFT_YELLOW, text_color = DARK_BLUE)
        self.scrollable_frame.email_box.grid(row=3, column=0, sticky="sew", padx=20, pady=(2,5))
        self.scrollable_frame.email_box.insert("0.0", "")

        self.scrollable_frame.password_entry = customtkinter.CTkLabel(master=self.scrollable_frame, text="Votre mot de passe :", font=self.text_font, text_color=SOFT_YELLOW, bg_color=DARK_BLUE, justify="left", anchor="w")
        self.scrollable_frame.password_entry.grid(row=4, column=0, sticky="sew", padx=20, pady=(5,2))

        self.scrollable_frame.password_box = customtkinter.CTkEntry(master=self.scrollable_frame, font=self.text_font, width=200, height=48, corner_radius=10, bg_color= DARK_BLUE, fg_color= SOFT_YELLOW, text_color = DARK_BLUE, show="*")
        self.scrollable_frame.password_box.grid(row=5, column=0, sticky="sew", padx=20, pady=(2,5))

        self.scrollable_frame.show_password_button = customtkinter.CTkButton(
            master=self.scrollable_frame, 
            text="",  
            width=40, 
            image=self.eye_closed,  
            command=self.toggle_password,
            fg_color=SOFT_YELLOW,  
            hover = False,
            border_width=0,
            corner_radius=0,
        )

        self.scrollable_frame.show_password_button.grid(row=5, column=0, padx=30, sticky="e")

        self.scrollable_frame.button = customtkinter.CTkButton(master=self.scrollable_frame, text="Se connecter".upper(), font=self.text_font, command=self.button_callback, corner_radius=7, bg_color=DARK_BLUE, fg_color=PINK)
        self.scrollable_frame.button.grid(row=6, column=0, padx=20, pady=(10,5))

        # self.error_label = customtkinter.CTkLabel(self, text="", text_color="red")
        # self.error_label.grid(row=6, column=0, padx=20, pady=5)

        self.scrollable_frame.button_create_account = customtkinter.CTkButton(master=self.scrollable_frame, text="Créer un compte".upper(), font=self.text_font, command=self.register_screen_build, corner_radius=7, bg_color=DARK_BLUE, fg_color=PINK)
        self.scrollable_frame.button_create_account.grid(row=7, column=0, padx=20, pady=5)

        self.build_quit_button()
    

    def build_quit_button(self):
        self.scrollable_frame.button_quit = customtkinter.CTkButton(master=self.scrollable_frame,
                                            text="Quitter".upper(),
                                            font=self.text_font,
                                            command=self.quit_app,
                                            corner_radius=7,
                                            bg_color= DARK_BLUE,
                                            fg_color = PINK) # button for quitting app
        
        self.scrollable_frame.button_quit.grid(row=18, column=0, sticky="", padx=20, pady=(5,10))

    def quit_app(self):
        self.destroy()

    def build_return_button(self):
        self.scrollable_frame.button_return = customtkinter.CTkButton(master=self.scrollable_frame,
                                            text="Retour".upper(),
                                            font=self.text_font,
                                            command=self.return_app,
                                            corner_radius=7,
                                            bg_color= DARK_BLUE,
                                            fg_color = PINK) # Return to login screen
        
        self.scrollable_frame.button_return.grid(row=17, column=0, sticky="", padx=20, pady=5)

    def return_app(self):
        self.destroy_register_screen()
        self.login_screen_build()
        
    def destroy_register_screen(self):
        self.scrollable_frame.title_text.destroy()

        self.scrollable_frame.firstname_label.destroy()
        self.scrollable_frame.firstname_box.destroy()

        self.scrollable_frame.lastname_label.destroy()
        self.scrollable_frame.lastname_box.destroy()

        self.scrollable_frame.email_label.destroy()
        self.scrollable_frame.email_box.destroy()

        self.scrollable_frame.password_label.destroy()
        self.scrollable_frame.password_box.destroy()

        self.scrollable_frame.confirm_password_label.destroy()
        self.scrollable_frame.confirm_password_box.destroy()

        self.scrollable_frame.show_password_button.destroy()

        self.scrollable_frame.button_register.destroy()

        self.scrollable_frame.button_return.destroy()
        # self.scrollable_frame.destroy()

        # if hasattr(self, 'error_label'):
        #     self.error_label.destroy()
        # if hasattr(self, 'login_text'):
        #     self.login_text.destroy()

    def register_screen_build(self):
        self.login_screen_destroy()

        # self.scrollable_frame = customtkinter.CTkScrollableFrame(self, width=400, height=500)  
        # self.scrollable_frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)
        

        # self.scrollable_frame.grid_columnconfigure(0, weight=1)

        # Titre
        self.scrollable_frame.title_text = customtkinter.CTkLabel(master=self.scrollable_frame, text="Créer un compte", font=self.title_font, text_color=YELLOW, bg_color=DARK_BLUE)
        self.scrollable_frame.title_text.grid(row=0, column=0, sticky="ew", padx=20, pady=(20,10))

        # Nom
        self.scrollable_frame.lastname_label = customtkinter.CTkLabel(self.scrollable_frame, text="Nom :", font=self.text_font, text_color=SOFT_YELLOW, bg_color=DARK_BLUE)
        self.scrollable_frame.lastname_label.grid(row=1, column=0, sticky="ew", padx=20, pady=(5,2))

        self.scrollable_frame.lastname_box = customtkinter.CTkEntry(self.scrollable_frame, font=self.text_font, height=48, corner_radius=10, bg_color=DARK_BLUE, fg_color=SOFT_YELLOW, text_color=DARK_BLUE)
        self.scrollable_frame.lastname_box.grid(row=2, column=0, sticky="ew", padx=20, pady=(2,5))

        # Prénom
        self.scrollable_frame.firstname_label = customtkinter.CTkLabel(self.scrollable_frame, text="Prénom :", font=self.text_font, text_color=SOFT_YELLOW, bg_color=DARK_BLUE)
        self.scrollable_frame.firstname_label.grid(row=3, column=0, sticky="ew", padx=20, pady=(5,2))

        self.scrollable_frame.firstname_box = customtkinter.CTkEntry(self.scrollable_frame, font=self.text_font, height=48, corner_radius=10, bg_color=DARK_BLUE, fg_color=SOFT_YELLOW, text_color=DARK_BLUE)
        self.scrollable_frame.firstname_box.grid(row=4, column=0, sticky="ew", padx=20, pady=(2,5))

        # Email
        self.scrollable_frame.email_label = customtkinter.CTkLabel(self.scrollable_frame, text="Email :", font=self.text_font, text_color=SOFT_YELLOW, bg_color=DARK_BLUE)
        self.scrollable_frame.email_label.grid(row=5, column=0, sticky="ew", padx=20, pady=(5,2))

        self.scrollable_frame.email_box = customtkinter.CTkEntry(self.scrollable_frame, font=self.text_font, height=48, corner_radius=10, bg_color=DARK_BLUE, fg_color=SOFT_YELLOW, text_color=DARK_BLUE)
        self.scrollable_frame.email_box.grid(row=6, column=0, sticky="ew", padx=20, pady=(2,5))

        # Mot de passe
        self.scrollable_frame.password_label = customtkinter.CTkLabel(self.scrollable_frame, text="Mot de passe :", font=self.text_font, text_color=SOFT_YELLOW, bg_color=DARK_BLUE)
        self.scrollable_frame.password_label.grid(row=7, column=0, sticky="ew", padx=20, pady=(5,2))

        self.scrollable_frame.password_box = customtkinter.CTkEntry(self.scrollable_frame, font=self.text_font, height=48, corner_radius=10, bg_color=DARK_BLUE, fg_color=SOFT_YELLOW, text_color=DARK_BLUE, show="*")
        self.scrollable_frame.password_box.grid(row=8, column=0, sticky="ew", padx=20, pady=(2,5))

        # Bouton montrer/masquer mot de passe
        self.scrollable_frame.show_password_button = customtkinter.CTkButton(
            master=self.scrollable_frame, 
            text="",  
            width=40, 
            image=self.eye_closed,  
            command=self.toggle_password,
            fg_color=SOFT_YELLOW,  
            hover=False,
            border_width=0,
            corner_radius=0,
        )
        self.scrollable_frame.show_password_button.grid(row=8, column=0, padx=20, pady=(2,5), sticky="e")

        # Confirmer le mot de passe
        self.scrollable_frame.confirm_password_label = customtkinter.CTkLabel(self.scrollable_frame,
                                                        text="Confirmez le mot de passe :",
                                                        font=self.text_font,
                                                        text_color=SOFT_YELLOW,
                                                        bg_color=DARK_BLUE)
        
        self.scrollable_frame.confirm_password_label.grid(row=9, column=0, sticky="ew", padx=20, pady=(5,2))

        self.scrollable_frame.confirm_password_box = customtkinter.CTkEntry(self.scrollable_frame, font=self.text_font, height=48, corner_radius=10, bg_color=DARK_BLUE, fg_color=SOFT_YELLOW, text_color=DARK_BLUE, show="*")
        self.scrollable_frame.confirm_password_box.grid(row=10, column=0, sticky="ew", padx=20, pady=(2,5))

        # Bouton S'inscrire
        self.scrollable_frame.button_register = customtkinter.CTkButton(master=self.scrollable_frame,
                                                text="S'inscrire".upper(),
                                                font=self.text_font,
                                                command=self.register_callback, 
                                                corner_radius=7,
                                                bg_color=DARK_BLUE,
                                                fg_color=PINK)
        
        self.scrollable_frame.button_register.grid(row=11, column=0, padx=20, pady=10, sticky="")

        # Bouton Retour (ajouté dans le scroll_frame)
        # self.scrollable_frame.return_button = customtkinter.CTkButton(
        #     master=self.scrollable_frame, 
        #     text="Retour", 
        #     command=self.return_app,  # Appelle directement return_app
        #     corner_radius=7, 
        #     fg_color=PINK
        # )
        # self.scrollable_frame.return_button.grid(row=12, column=0, padx=20, pady=(5,2), sticky="")
        
        self.build_return_button()
        self.build_quit_button()

    def register_callback(self):
        """
        a utiliser pour ton IHM
        """
        if hasattr(self, 'login_text'):
            self.login_text.destroy()

        try:
            self.log_info.set_firstname(self.scrollable_frame.firstname_box.get().strip())
            self.log_info.set_lastname(self.scrollable_frame.lastname_box.get().strip())
            self.log_info.set_email(self.scrollable_frame.email_box.get().strip())
            self.log_info.set_password(self.scrollable_frame.password_box.get().strip())
            self.log_info.set_confirm_password(self.scrollable_frame.confirm_password_box.get().strip())
        
            self.controller.register_user(self.log_info)#accoun_type,account_name,balance,min_balance
            self.build_login_result(20, "Compte créé avec succès !")
        except LogInDataException as e:
            self.build_login_result(20, e)



    def toggle_password(self):
        if self.scrollable_frame.password_box.cget('show') == '*':
            self.scrollable_frame.password_box.configure(show="")
            if hasattr(self, 'confirm_password_box'):
                self.scrollable_frame.confirm_password_box.configure(show="")
            self.scrollable_frame.show_password_button.configure(image=self.eye_open)
        else:
            self.scrollable_frame.password_box.configure(show="*")
            if hasattr(self, 'confirm_password_box'):
                self.scrollable_frame.confirm_password_box.configure(show="*")
            self.scrollable_frame.show_password_button.configure(image=self.eye_closed)


    def login_screen_destroy(self):
        self.scrollable_frame.email_entry.destroy()
        self.scrollable_frame.email_box.destroy()
        self.scrollable_frame.password_entry.destroy()
        self.scrollable_frame.password_box.destroy()
        self.scrollable_frame.show_password_button.destroy()  
        self.scrollable_frame.button.destroy()
        self.scrollable_frame.button_create_account.destroy()
        self.scrollable_frame.title_text.destroy()
        self.scrollable_frame.title_text.destroy()

    def build_logout_button(self):
        self.scrollable_frame.button = customtkinter.CTkButton(master=self.scrollable_frame, text="Se déconnecter".upper(), font=self.text_font, command=self.scrollable_frame.button_callbck_logout, corner_radius=10, bg_color=DARK_BLUE, fg_color=PINK)
        self.scrollable_frame.button.grid(row=1, column=0, padx=20, pady=20)

    def logout(self):
        self.interface_screen_destroy()
        self.login_screen_build()
        if hasattr(self, 'login_text'):
            self.login_text.destroy()

    def interface_screen_destroy(self):
        self.scrollable_frame.button.destroy()

    def button_callback(self):
        if hasattr(self, 'login_text'):
            self.login_text.destroy()

        email = self.scrollable_frame.email_box.get("1.0", "end").strip()
        password = self.scrollable_frame.password_box.get().strip()
        try:
            self.controller.validate_email(email)
            self.log_info.set_id_user(self.__data_acces.get_user_id_from_email(email))

            self.controller.validate_password(password)
            stored_hashed_password = self.__data_acces.get_password_from_id_user(self.log_info.get_user_id())

            if self.controller.check_password(stored_hashed_password, password):
                self.login_screen_destroy()
                self.build_logout_button()
                self.build_login_result(10, "Vous êtes connecté !")
                self.connected[0] = True
                self.connected[1] = self.log_info
                
                self.destroy()
               
        except LogInDataException as e:
            self.build_login_result(20, e)


    def build_login_result(self, row1, error_message):
        self.login_text = customtkinter.CTkLabel(master=self.scrollable_frame, text=error_message, font=self.text_font, text_color=SOFT_YELLOW, bg_color=DARK_BLUE, justify="left", anchor="w")
        self.login_text.grid(row=row1, column=0, sticky="sn", padx=20, pady=5)
    
    def print_all_users(self):
        if self.__all_users:
            for user in self.__all_users:
                user_id, firstname, lastname, email, password = user  
                print(f"ID: {user_id}, Prénom: {firstname}, Nom: {lastname}, Email: {email}, Hash: {password}")
        else:
            print("Aucun utilisateur trouvé.")


    def button_callbck(self):
        print("Connexion réussie")
        self.login_screen_destroy()
        self.build_logout_button()
        self.confirmed = True
        

    def button_callbck_logout(self):
        print("Déconnexion réussie")
        self.interface_screen_destroy()
        self.login_screen_build()
        if hasattr(self, 'login_text'):
            self.login_text.destroy()



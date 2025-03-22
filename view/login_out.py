import customtkinter
# import tkinter
# import time
from model.server import ServerDatabase
import re
import bcrypt
# import sqlite3
from data_access.read_user_data import UserDataAcess

from controller.login_data_manager import LoginManager
from model.login_info import LoginInfo
from model.customexception import LogInDataException
from view.dashboard import Dashboard

from view.__settings__ import DARK_BLUE, SOFT_BLUE, LIGHT_BLUE, YELLOW, SOFT_YELLOW, PINK
from model.server import ServerDatabase
# from view.utiltool import UtilTool
from view.interface import Interface

class LogInOut(Interface):
    def __init__(self, window_title, column_number):
        super().__init__(window_title, column_number)
        self.controller = LoginManager()
        self.password_visible = False 
        self.eye_open, self.eye_closed = self.util.get_eye_icons()
        self.log_info = LoginInfo()
        # self.email = ""
        # self.__password = ""
        # self.lastname = ""
        # self.firstname = ""
        # self.current_user_id = None 
        self.database = ServerDatabase()
        #self.create_users_table_if_not_exists()
        self.login_screen_build()
        self.lift() 
        self.attributes("-topmost", True)
        
        self.__data_acces = UserDataAcess()
        self.__all_users = self.__data_acces.get_all_users()


    def login_screen_build(self):
        self.title_text = customtkinter.CTkLabel(master=self, text="Budget Buddy", font=self.title_font, text_color=YELLOW, bg_color=DARK_BLUE)
        self.title_text.grid(row=0, column=0, sticky="sew", padx=20, pady=0)

        self.subtitle_text = customtkinter.CTkLabel(master=self, text="Votre application bancaire préférée", font=self.text_font, text_color=YELLOW, bg_color=DARK_BLUE)
        self.subtitle_text.grid(row=1, column=0, sticky="sew", padx=20, pady=0)

        self.email_entry = customtkinter.CTkLabel(master=self, text="Votre adresse email :", font=self.text_font, text_color=SOFT_YELLOW, bg_color=DARK_BLUE, justify="left", anchor="w")
        self.email_entry.grid(row=2, column=0, sticky="sew", padx=20, pady=5)

        self.email_box = customtkinter.CTkTextbox(master=self, font=self.text_font, width=200, height=48, corner_radius=10, bg_color=DARK_BLUE, fg_color=SOFT_YELLOW, text_color=DARK_BLUE)
        self.email_box.grid(row=3, column=0, sticky="sew", padx=20, pady=0)
        self.email_box.insert("0.0", "")

        self.password_entry = customtkinter.CTkLabel(master=self, text="Votre mot de passe :", font=self.text_font, text_color=SOFT_YELLOW, bg_color=DARK_BLUE, justify="left", anchor="w")
        self.password_entry.grid(row=4, column=0, sticky="sew", padx=20, pady=5)

        self.password_box = customtkinter.CTkEntry(master=self, font=self.text_font, width=200, height=48, corner_radius=10, bg_color=DARK_BLUE, fg_color=SOFT_YELLOW, text_color=DARK_BLUE, show="*")
        self.password_box.grid(row=5, column=0, sticky="sew", padx=20, pady=0)

        self.show_password_button = customtkinter.CTkButton(
            self, 
            text="",  
            width=40, 
            image=self.eye_closed,  
            command=self.toggle_password,
            fg_color="transparent",  
            hover = False,
            border_width=0,
            corner_radius=0
        )

        self.show_password_button.grid(row=5, column=2, padx=10)

        self.button = customtkinter.CTkButton(self, text="Se connecter".upper(), font=self.text_font, command=self.button_callback, corner_radius=7, bg_color=DARK_BLUE, fg_color=PINK)
        self.button.grid(row=7, column=0, padx=20, pady=20)

        self.error_label = customtkinter.CTkLabel(self, text="", text_color="red")
        self.error_label.grid(row=6, column=0, padx=20, pady=5)

        self.button_create_account = customtkinter.CTkButton(self, text="Créer un compte".upper(), font=self.text_font, command=self.register_screen_build, corner_radius=7, bg_color=DARK_BLUE, fg_color=PINK)
        self.button_create_account.grid(row=8, column=0, padx=20, pady=20)

        self.build_quit_button()
    

    def build_quit_button(self):
        self.button_quit = customtkinter.CTkButton(master=self, text="Quitter".upper(), font=self.text_font, command=self.quit_app, corner_radius=7, bg_color= DARK_BLUE, fg_color = PINK) # bouton se connecter
        self.button_quit.grid(row=18, column=0, sticky="snew", padx=20, pady=5)

    def quit_app(self):
        self.destroy()

    def build_return_button(self):
        self.button_return = customtkinter.CTkButton(master=self, text="Retour".upper(), font=self.text_font, command=self.return_app, corner_radius=7, bg_color= DARK_BLUE, fg_color = PINK) # bouton se connecter
        self.button_return.grid(row=17, column=0, sticky="snew", padx=20, pady=5)

    def return_app(self):
        self.destroy_register_screen()
        self.login_screen_build()
        
    def destroy_register_screen(self):
        self.title_text.destroy()

        self.firstname_label.destroy()
        self.firstname_box.destroy()

        self.lastname_label.destroy()
        self.lastname_box.destroy()

        self.email_label.destroy()
        self.email_box.destroy()

        self.password_label.destroy()
        self.password_box.destroy()

        self.confirm_password_label.destroy()
        self.confirm_password_box.destroy()

        self.show_password_button.destroy()

        self.button_register.destroy()

        self.button_return.destroy()

        if hasattr(self, 'error_label'):
            self.error_label.destroy()

    def register_screen_build(self):
        self.login_screen_destroy()
        # self.geometry("640x600")

        self.title_text = customtkinter.CTkLabel(self, text="Créer un compte", font=self.title_font, text_color=YELLOW, bg_color=DARK_BLUE)
        self.title_text.grid(row=1, column=0, sticky="sew", padx=20, pady=10)

        self.firstname_label = customtkinter.CTkLabel(self, text="Prénom :", font=self.text_font, text_color=SOFT_YELLOW, bg_color=DARK_BLUE)
        self.firstname_label.grid(row=2, column=0, sticky="sew", padx=20, pady=5)

        self.firstname_box = customtkinter.CTkEntry(self, font=self.text_font, width=200, height=30)
        self.firstname_box.grid(row=3, column=0, sticky="sew", padx=20, pady=5)

        self.lastname_label = customtkinter.CTkLabel(self, text="Nom :", font=self.text_font, text_color=SOFT_YELLOW, bg_color=DARK_BLUE)
        self.lastname_label.grid(row=4, column=0, sticky="sew", padx=20, pady=5)

        self.lastname_box = customtkinter.CTkEntry(self, font=self.text_font, width=200, height=30)
        self.lastname_box.grid(row=5, column=0, sticky="sew", padx=20, pady=5)

        self.email_label = customtkinter.CTkLabel(self, text="Email :", font=self.text_font, text_color=SOFT_YELLOW, bg_color=DARK_BLUE)
        self.email_label.grid(row=6, column=0, sticky="sew", padx=20, pady=5)

        self.email_box = customtkinter.CTkEntry(self, font=self.text_font, width=200, height=30)
        self.email_box.grid(row=7, column=0, sticky="sew", padx=20, pady=5)

        self.password_label = customtkinter.CTkLabel(self, text="Mot de passe :", font=self.text_font, text_color=SOFT_YELLOW, bg_color=DARK_BLUE)
        self.password_label.grid(row=8, column=0, sticky="sew", padx=20, pady=5)

        self.password_box = customtkinter.CTkEntry(self, font=self.text_font, width=200, height=30, show="*")
        self.password_box.grid(row=9, column=0, sticky="sew", padx=20, pady=5)

        self.confirm_password_label = customtkinter.CTkLabel(self, text="Confirmez le mot de passe :", font=self.text_font, text_color=SOFT_YELLOW, bg_color=DARK_BLUE)
        self.confirm_password_label.grid(row=10, column=0, sticky="sew", padx=20, pady=5)

        self.confirm_password_box = customtkinter.CTkEntry(self, font=self.text_font, width=200, height=30, show="*")
        self.confirm_password_box.grid(row=11, column=0, sticky="sew", padx=20, pady=5)

        self.show_password_button = customtkinter.CTkButton(
            self, 
            text="",  
            width=40, 
            image=self.eye_closed,  
            command=self.toggle_password,
            fg_color="transparent",  
            hover = False,
            border_width=0,
            corner_radius=0
        )

        self.show_password_button.grid(row=9, column=1, padx=10)

        self.button_register = customtkinter.CTkButton(self, text="S'inscrire".upper(), font=self.text_font, command=self.register_callback, corner_radius=7, bg_color=DARK_BLUE, fg_color=PINK)
        self.button_register.grid(row=14, column=0, padx=20, pady=10)

        self.error_label = customtkinter.CTkLabel(self, text="", text_color="red")
        self.error_label.grid(row=16, column=0, padx=20, pady=5)

        self.build_return_button()
        self.build_quit_button()

    def register_callback(self):
        """
        a utiliser pour ton IHM
        """
        firstname = self.firstname_box.get().strip()
        lastname = self.lastname_box.get().strip()
        email = self.email_box.get().strip()
        password = self.password_box.get().strip()
        confirm_password = self.confirm_password_box.get().strip()
        # account_type = self.account_type_box.get().strip()
        # account_name = self.account_name_box.get().strip()
        # balance = self.balance_box.get().strip()
        # min_balance = self.min_balance_box.get().strip()
        
        self.register_user(firstname, lastname, email, password, confirm_password)#accoun_type,account_name,balance,min_balance


    def toggle_password(self):
        if self.password_box.cget('show') == '*':
            self.password_box.configure(show="")
            self.confirm_password_box.configure(show="")
            self.show_password_button.configure(image=self.eye_open)
        else:
            self.password_box.configure(show="*")
            self.confirm_password_box.configure(show="*")
            self.show_password_button.configure(image=self.eye_closed)


    def login_screen_destroy(self):
        self.email_entry.destroy()
        self.email_box.destroy()
        self.password_entry.destroy()
        self.password_box.destroy()
        self.show_password_button.destroy()  
        self.button.destroy()
        self.button_create_account.destroy()
        self.subtitle_text.destroy()
        self.title_text.destroy()

    def build_logout_button(self):
        self.button = customtkinter.CTkButton(self, text="Se déconnecter".upper(), font=self.text_font, command=self.button_callbck_logout, corner_radius=10, bg_color=DARK_BLUE, fg_color=PINK)
        self.button.grid(row=1, column=0, padx=20, pady=20)

    def logout(self):
        self.interface_screen_destroy()
        self.login_screen_build()
        if hasattr(self, 'login_text'):
            self.login_text.destroy()
        # if self.success_label:  
        #     self.success_label.destroy()
        # self.success_label = None

    def interface_screen_destroy(self):
        self.button.destroy()

    def button_callback(self):
        if hasattr(self, 'login_text'):
            self.login_text.destroy()

        email = self.email_box.get("1.0", "end").strip()
        password = self.password_box.get().strip()
        try:
            self.controller.validate_email(email)
            self.log_info.set_id_user(self.__data_acces.get_user_id_from_email(email))

            self.controller.validate_password(password)
            stored_hashed_password = self.__data_acces.get_password_from_id_user(self.log_info.get_user_id())

            if self.controller.check_password(stored_hashed_password, password):
                self.login_screen_destroy()
                self.build_logout_button()
                self.build_login_result(10, "Vous êtes connecté !")
                
                # self.login_screen_destroy()
                
                board = Dashboard("Budget Buddy - Dashboard", 1, self.log_info)
                # board.mainloop()
                self.destroy()
                # self.success_label = customtkinter.CTkLabel(self, text="Vous êtes connecté !", font=self.text_font, text_color=SOFT_YELLOW, bg_color=DARK_BLUE)
                # self.success_label.grid(row=9, column=0, padx=20, pady=10)
        except LogInDataException as e:
            self.build_login_result(20, e)


    def build_login_result(self, row1, error_message):
        self.login_text = customtkinter.CTkLabel(master=self, text=error_message, font=self.text_font, text_color=SOFT_BLUE, bg_color=DARK_BLUE)
        self.login_text.grid(row=row1, column=0, sticky="sn", padx=20, pady=5)
    
    def print_all_users(self):
        # users = self.get_all_users()
        if self.__all_users:
            for user in self.__all_users:
                user_id, firstname, lastname, email, password = user  
                print(f"ID: {user_id}, Prénom: {firstname}, Nom: {lastname}, Email: {email}, Hash: {password}")
        else:
            print("Aucun utilisateur trouvé.")

        # email = "exemple@domaine.com"  
        # user = get_user_by_email(email)
        # if user:
        #     print(user)  
        # else:
        #     print("Utilisateur non trouvé.")


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
        # if self.success_label: 
        #     self.success_label.destroy()
        # self.success_label = None




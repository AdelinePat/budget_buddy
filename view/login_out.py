import customtkinter
# import tkinter
# import time
from model.server import ServerDatabase
import re
import bcrypt
# import sqlite3

from view.__settings__ import DARK_BLUE, SOFT_BLUE, LIGHT_BLUE, YELLOW, SOFT_YELLOW, PINK
from model.server import ServerDatabase
# from view.utiltool import UtilTool
from view.interface import Interface

class LogInOut(Interface):
    def __init__(self, window_title, column_number):
        super().__init__(window_title, column_number)
        self.password_visible = False 
        self.eye_open, self.eye_closed = self.util.get_eye_icons()
        self.email = ""
        self.__password = ""
        self.lastname = ""
        self.firstname = ""
        self.current_user_id = None 
        self.database = ServerDatabase()
        #self.create_users_table_if_not_exists()
        self.login_screen_build()
        self.lift() 
        self.attributes("-topmost", True)
        self.get_all_users()

    # def create_users_table_if_not_exists(self):
    #     """Crée la table users si elle n'existe pas."""
    #     conn = sqlite3.connect('users.sql')
    #     cursor = conn.cursor()
    #     cursor.execute("""
    #     CREATE TABLE IF NOT EXISTS users (
    #         id INTEGER PRIMARY KEY AUTOINCREMENT,
    #         firstname TEXT NOT NULL,
    #         lastname TEXT NOT NULL,
    #         email TEXT UNIQUE NOT NULL,
    #         password TEXT NOT NULL
    #     );
    #     """)
    #     conn.commit()
    #     conn.close()
    
    def get_user_id_from_db(self, email):
        conn = self.database.database_connection()
        cursor = conn.cursor()
        query = "SELECT id_user FROM Users WHERE email = %s"
        cursor.execute(query, (email,))
        result = cursor.fetchone()
        self.database.close()
        
        return result[0] if result else None


    # conn = sqlite3.connect('users.sql')
    # cursor = conn.cursor()
    # cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    # tables = cursor.fetchall()
    # print(tables)  
    # conn.close()

    def register_user(self, firstname, lastname, email, password, confirm_password):
        if not firstname or not lastname:
            self.error_label.configure(text="Le prénom et le nom sont obligatoires.")
            return
        
        if not bool(self.validate_email(email)):
            self.error_label.configure(text="Email invalide. Format attendu : exemple@domaine.com")
            return

        if not self.validate_password(password):
            self.error_label.configure(text=( 
                "Mot de passe invalide. Il doit contenir :\n"
                "- Une majuscule\n"
                "- Un chiffre\n"
                "- Un caractère spécial (!@#$%^&*.._.)\n"
                "- Au moins 8 caractères"
            ))
            return
        
        if password != confirm_password:
            self.error_label.configure(text="Les mots de passe ne correspondent pas.")
            return

        hashed_password = self.hash_password(password)
        
        
        try:
            conn = self.database.database_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO Users (lastname, firstname, email, password) VALUES (%s, %s, %s, %s)", 
                        (lastname,firstname , email, hashed_password))
            conn.commit()
            conn.close()
            self.error_label.configure(text="Compte créé avec succès !",
                                        text_color="green")
        except Exception as error:
            print(f"[LogInOut][register_user] Mon erreur est : {error}")
            
            self.error_label.configure(text="Cet email est déjà utilisé.",
                                        text_color="red")

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

    def register_screen_build(self):
        self.login_screen_destroy()
        self.geometry("640x600")

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

    def register_callback(self):
        firstname = self.firstname_box.get().strip()
        lastname = self.lastname_box.get().strip()
        email = self.email_box.get().strip()
        password = self.password_box.get().strip()
        confirm_password = self.confirm_password_box.get().strip()
        
        self.register_user(firstname, lastname, email, password, confirm_password)


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

    def interface_screen_build(self):
        self.button = customtkinter.CTkButton(self, text="Se déconnecter".upper(), font=self.text_font, command=self.button_callbck_logout, corner_radius=10, bg_color=DARK_BLUE, fg_color=PINK)
        self.button.grid(row=1, column=0, padx=20, pady=20)

    def logout(self):
        self.interface_screen_destroy()
        self.login_screen_build()
        if self.success_label:  
            self.success_label.destroy()
        self.success_label = None

    def interface_screen_destroy(self):
        self.button.destroy()

    def button_callback(self):
        email = self.email_box.get("1.0", "end").strip()
        password = self.password_box.get().strip()

        if not self.validate_email(email):
            self.error_label.configure(text="Email invalide. Format attendu : exemple@domaine.com")
            return

        if not self.validate_password(password):
            self.error_label.configure(text=(
                "Mot de passe invalide. Il doit contenir :\n"
                "- Une majuscule\n"
                "- Un chiffre\n"
                "- Un caractère spécial (!@#$%^&*.._.)\n"
                "- Au moins 8 caractères"
            ))
            return

        stored_hashed_password = self.get_user_password_from_db(email)
        if stored_hashed_password and self.check_password(stored_hashed_password, password):
            print("Connexion réussie")
            self.error_label.configure(text="")

            # Stocke l'ID utilisateur après connexion
            self.current_user_id = self.get_user_id_from_db(email)
            print(f"Utilisateur connecté : ID {self.current_user_id}")

            self.login_screen_destroy()
            self.interface_screen_build()

        self.success_label = customtkinter.CTkLabel(self, text="Vous êtes connecté !", font=self.text_font, text_color=SOFT_YELLOW, bg_color=DARK_BLUE)
        self.success_label.grid(row=9, column=0, padx=20, pady=10)

    
    def get_user_password_from_db(self, email):
        conn = self.database.database_connection()
        cursor = conn.cursor()
        query = "SELECT password FROM users WHERE email = %s"
        cursor.execute(query, (email,))
        result = cursor.fetchone()
        conn.close()
        if result:
            return result[0]
        return None
    


    def get_all_users(self):
        conn = self.database.database_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id_user, firstname, lastname, email, password FROM Users")
        users = cursor.fetchall()  
        cursor.close()
        conn.close()        
        return users
    
    def print_all_users(self):
        users = self.get_all_users()
        if users:
            for user in users:
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



    def validate_email(self, email):
        email_regex = r"^[\w\.\+-]+@[a-zA-Z0-9\.\-]+\.[a-zA-Z]{2,}$"
        return re.match(email_regex, email)
    
    def hash_password(self, password):
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed_password.decode('utf-8')
    
    def check_password(self, stored_hashed_password, input_password):
        return bcrypt.checkpw(input_password.encode('utf-8'), stored_hashed_password.encode('utf-8'))

    def validate_password(self, password):
        password_regex = r"^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&_\-])[A-Za-z\d@$!%*?&_\-\_]{8,}$"
        return re.match(password_regex, password)

    def button_callbck(self):
        print("Connexion réussie")
        self.login_screen_destroy()
        self.interface_screen_build()
        self.confirmed = True

    def button_callbck_logout(self):
        print("Déconnexion réussie")
        self.interface_screen_destroy()
        self.login_screen_build()
        if self.success_label: 
            self.success_label.destroy()
        self.success_label = None




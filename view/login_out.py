import customtkinter
import tkinter
import time
import re
import bcrypt
import sqlite3
from view.__settings__ import DARK_BLUE, SOFT_BLUE, LIGHT_BLUE, YELLOW, SOFT_YELLOW, PINK
from view.utiltool import UtilTool, get_eye_icons

class Interface_frames:

    pass

class Interface(customtkinter.CTk, Interface_frames):
    def __init__(self):
        super().__init__()
        self.util = UtilTool()
        self.current_scene = "broad_view"
        self.geometry("640x480")
        self.config(background=DARK_BLUE)
        self.title("Connexion Client")
        self.columnconfigure((0), weight=1)
        self.title_font = self.util.get_title_font(30)
        self.text_font = self.util.get_text_font(15)
        self.password_visible = False 
        self.eye_open, self.eye_closed = get_eye_icons()
        self.initialize_database()
        self.login_screen_build()

    def initialize_database(self):
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email TEXT UNIQUE NOT NULL,
                hashed_password TEXT NOT NULL
            )
        ''')
        conn.commit()
        conn.close()

    def initialize_database(self):
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                hashed_password TEXT NOT NULL
            )
        ''')
        conn.commit()
        conn.close()


        
    def get_font(self):
        pass

    def register_user(self, email, password):
    
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

        hashed_password = self.hash_password(password)

        try:
            conn = sqlite3.connect('users.db')
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (email, hashed_password) VALUES (?, ?)", (email, hashed_password))
            conn.commit()
            conn.close()
            self.error_label.configure(text="Compte créé avec succès !", text_color="green")
        except sqlite3.IntegrityError:
            self.error_label.configure(text="Cet email est déjà utilisé.", text_color="red")

    
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

        self.title_text = customtkinter.CTkLabel(self, text="Créer un compte", font=self.title_font, text_color=YELLOW, bg_color=DARK_BLUE)
        self.title_text.grid(row=0, column=0, sticky="sew", padx=20, pady=10)

        self.first_name_label = customtkinter.CTkLabel(self, text="Prénom :", font=self.text_font, text_color=SOFT_YELLOW, bg_color=DARK_BLUE)
        self.first_name_label.grid(row=1, column=0, sticky="w", padx=20, pady=5)

        self.first_name_box = customtkinter.CTkEntry(self, font=self.text_font, width=200, height=30)
        self.first_name_box.grid(row=2, column=0, padx=20, pady=5)

        self.last_name_label = customtkinter.CTkLabel(self, text="Nom :", font=self.text_font, text_color=SOFT_YELLOW, bg_color=DARK_BLUE)
        self.last_name_label.grid(row=3, column=0, sticky="w", padx=20, pady=5)

        self.last_name_box = customtkinter.CTkEntry(self, font=self.text_font, width=200, height=30)
        self.last_name_box.grid(row=4, column=0, padx=20, pady=5)

        self.email_label = customtkinter.CTkLabel(self, text="Email :", font=self.text_font, text_color=SOFT_YELLOW, bg_color=DARK_BLUE)
        self.email_label.grid(row=5, column=0, sticky="w", padx=20, pady=5)

        self.email_box = customtkinter.CTkEntry(self, font=self.text_font, width=200, height=30)
        self.email_box.grid(row=6, column=0, padx=20, pady=5)

        self.password_label = customtkinter.CTkLabel(self, text="Mot de passe :", font=self.text_font, text_color=SOFT_YELLOW, bg_color=DARK_BLUE)
        self.password_label.grid(row=7, column=0, sticky="w", padx=20, pady=5)

        self.password_box = customtkinter.CTkEntry(self, font=self.text_font, width=200, height=30, show="*")
        self.password_box.grid(row=8, column=0, padx=20, pady=5)

   
        self.confirm_password_label = customtkinter.CTkLabel(self, text="Confirmez le mot de passe :", font=self.text_font, text_color=SOFT_YELLOW, bg_color=DARK_BLUE)
        self.confirm_password_label.grid(row=9, column=0, sticky="w", padx=20, pady=5)

        self.confirm_password_box = customtkinter.CTkEntry(self, font=self.text_font, width=200, height=30, show="*")
        self.confirm_password_box.grid(row=10, column=0, padx=20, pady=5)


        self.button_register = customtkinter.CTkButton(self, text="S'inscrire", font=self.text_font, command=self.register_callback, corner_radius=7, fg_color=PINK)
        self.button_register.grid(row=11, column=0, padx=20, pady=10)


        self.button_back = customtkinter.CTkButton(self, text="Retour", font=self.text_font, command=self.login_screen_build, corner_radius=7, fg_color=SOFT_BLUE)
        self.button_back.grid(row=12, column=0, padx=20, pady=10)

        self.error_label = customtkinter.CTkLabel(self, text="", text_color="red")
        self.error_label.grid(row=13, column=0, padx=20, pady=5)

    def register_user(self, first_name, last_name, email, password, confirm_password):
        
        if not first_name or not last_name:
            self.error_label.configure(text="Le prénom et le nom sont obligatoires.")
            return
        
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
        
        if password != confirm_password:
            self.error_label.configure(text="Les mots de passe ne correspondent pas.")
            return

        hashed_password = self.hash_password(password)

        try:
            conn = sqlite3.connect('users.db')
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (first_name, last_name, email, hashed_password) VALUES (?, ?, ?, ?)", 
                        (first_name, last_name, email, hashed_password))
            conn.commit()
            conn.close()
            self.error_label.configure(text="Compte créé avec succès !", text_color="green")
        except sqlite3.IntegrityError:
            self.error_label.configure(text="Cet email est déjà utilisé.", text_color="red")

    def register_callback(self):
        first_name = self.first_name_box.get().strip()
        last_name = self.last_name_box.get().strip()
        email = self.email_box.get().strip()
        password = self.password_box.get().strip()
        confirm_password = self.confirm_password_box.get().strip()
        
        self.register_user(first_name, last_name, email, password, confirm_password)


    def toggle_password(self):
        if self.password_visible:
            self.show_password_button.configure(image=self.eye_closed) 
            self.password_box.configure(show="*")
        else:
            self.show_password_button.configure(image=self.eye_open) 
            self.password_box.configure(show="")  
        
        self.password_visible = not self.password_visible

    def login_screen_destroy(self):
        self.email_entry.destroy()
        self.email_box.destroy()
        self.password_entry.destroy()
        self.password_box.destroy()
        self.show_password_button.destroy()  
        self.button.destroy()
        self.button_create_account.destroy()

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

        stored_hashed_password = self.get_user_password_from_db(email)  # Call the method using self
        if stored_hashed_password and self.check_password(stored_hashed_password, password): 
            print("Connexion réussie")
            self.error_label.configure(text="")  
            self.login_screen_destroy()
            self.interface_screen_build()

        self.success_label = customtkinter.CTkLabel(self, text="Vous êtes connecté !", font=self.text_font, text_color=SOFT_YELLOW, bg_color=DARK_BLUE)
        self.success_label.grid(row=9, column=0, padx=20, pady=10)

    
    def get_user_password_from_db(self, email):
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        query = "SELECT hashed_password FROM users WHERE email = ?"
        cursor.execute(query, (email,))
        result = cursor.fetchone()
        conn.close()
        if result:
            return result[0]
        return None

    def validate_email(self, email):
        email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$"
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

client_account_interface = Interface()
client_account_interface.mainloop()

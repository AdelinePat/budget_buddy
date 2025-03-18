import customtkinter
import tkinter
import time
import re
from __settings__ import DARK_BLUE, SOFT_BLUE, LIGHT_BLUE, YELLOW, SOFT_YELLOW, PINK, get_text_font, get_title_font, get_eye_icons

class Interface_frames:
    pass

class Interface(customtkinter.CTk, Interface_frames):
    def __init__(self):
        super().__init__()
        self.current_scene = "broad_view"
        self.geometry("640x480")
        self.config(background=DARK_BLUE)
        self.title("Connexion Client")
        self.columnconfigure((0), weight=1)
        self.title_font = get_title_font(30)
        self.text_font = get_text_font(15)
        self.password_visible = False 
        self.eye_open, self.eye_closed = get_eye_icons()
        self.login_screen_build()
        
    def get_font(self):
        pass
    
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
        self.error_label.grid(row=2, column=0, padx=20, pady=5)

        self.button_create_account = customtkinter.CTkButton(self, text="Créer un compte".upper(), font=self.text_font, command=self.button_callback, corner_radius=7, bg_color=DARK_BLUE, fg_color=PINK)
        self.button_create_account.grid(row=8, column=0, padx=20, pady=20)


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

        print("Connexion réussie")
        self.error_label.configure(text="")  
        self.login_screen_destroy()
        self.interface_screen_build()

        self.success_label = customtkinter.CTkLabel(self, text="Vous êtes connecté !", font=self.text_font, text_color=SOFT_YELLOW, bg_color=DARK_BLUE)
        self.success_label.grid(row=9, column=0, padx=20, pady=10)  
            
            
    def validate_email(self, email):
        email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$"
        return re.match(email_regex, email)
    
    def validate_password(self, password):
        password_regex = r"^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&_])[A-Za-z\d@$!%*?&_]{8,}$"
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

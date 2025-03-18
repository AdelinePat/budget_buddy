import customtkinter
import tkinter
import time
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

        self.email_text = customtkinter.CTkLabel(master=self, text="Votre adresse email :", font=self.text_font, text_color=SOFT_YELLOW, bg_color=DARK_BLUE, justify="left", anchor="w")
        self.email_text.grid(row=2, column=0, sticky="sew", padx=20, pady=5)

        self.email_box = customtkinter.CTkTextbox(master=self, font=self.text_font, width=200, height=48, corner_radius=10, bg_color=DARK_BLUE, fg_color=SOFT_YELLOW, text_color=DARK_BLUE)
        self.email_box.grid(row=3, column=0, sticky="sew", padx=20, pady=0)
        self.email_box.insert("0.0", "")

        self.password_text = customtkinter.CTkLabel(master=self, text="Votre mot de passe :", font=self.text_font, text_color=SOFT_YELLOW, bg_color=DARK_BLUE, justify="left", anchor="w")
        self.password_text.grid(row=4, column=0, sticky="sew", padx=20, pady=5)

        
        self.password_box = customtkinter.CTkEntry(master=self, font=self.text_font, width=200, height=48, corner_radius=10, bg_color=DARK_BLUE, fg_color=SOFT_YELLOW, text_color=DARK_BLUE, show="*")
        self.password_box.grid(row=5, column=0, sticky="sew", padx=20, pady=0)

       
        self.show_password_button = customtkinter.CTkButton(self, text="👁", width=40, command=self.toggle_password)
        self.show_password_button.grid(row=5, column=2, padx=10)

        self.button = customtkinter.CTkButton(self, text="Se connecter".upper(), font=self.text_font, command=self.button_callbck, corner_radius=7, bg_color=DARK_BLUE, fg_color=PINK)
        self.button.grid(row=7, column=0, padx=20, pady=20)

        self.button_create_account = customtkinter.CTkButton(self, text="Créer un compte".upper(), font=self.text_font, command=self.button_callbck, corner_radius=7, bg_color=DARK_BLUE, fg_color=PINK)
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
        self.email_text.destroy()
        self.email_box.destroy()
        self.password_text.destroy()
        self.password_box.destroy()
        self.show_password_button.destroy()  
        self.button.destroy()

    def interface_screen_build(self):
        self.button = customtkinter.CTkButton(self, text="Se déconnecter".upper(), font=self.text_font, command=self.button_callbck_logout, corner_radius=10, bg_color=DARK_BLUE, fg_color=PINK)
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

client_account_interface = Interface()
client_account_interface.mainloop()

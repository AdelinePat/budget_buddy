import customtkinter
import time
from __settings__ import DARK_BLUE, SOFT_BLUE, LIGHT_BLUE, YELLOW, SOFT_YELLOW, PINK, TITLE_FONT, TEXT_FONT, change_font

class Interface_frames:
    pass

class Interface(customtkinter.CTk, Interface_frames):
    def __init__(self):
        super().__init__()
        self.current_scene = "broad_view"
        self.geometry("640x480")
        self.config(background = DARK_BLUE)
        self.title("Connexion Client")
        self.columnconfigure((0), weight=1)
        self.login_screen_build()

    def get_font(self):
        pass
    
    def login_screen_build(self):

        self.email_text = customtkinter.CTkTextbox(master=self, width=200, height=48, corner_radius=10, bg_color= DARK_BLUE, fg_color= DARK_BLUE, text_color = SOFT_YELLOW) # champs "email"
        self.email_text.grid(row=1, column=0, sticky="sew", padx=20, pady=5)
        self.email_text.insert("0.0", "Votre adresse email : ")
        self.email_text.configure(state='disabled') 

        self.email_box = customtkinter.CTkTextbox(master=self, width=200, height=48, corner_radius=10, bg_color= DARK_BLUE, fg_color= SOFT_YELLOW, text_color = DARK_BLUE) # champs "email"
        self.email_box.grid(row=2, column=0, sticky="sew", padx=20, pady=0)
        self.email_box.insert("0.0", "")

        self.password_text = customtkinter.CTkTextbox(master=self, width=200, height=48, corner_radius=10, bg_color= DARK_BLUE, fg_color= DARK_BLUE, text_color = SOFT_YELLOW) # champs "email"
        self.password_text.grid(row=3, column=0, sticky="sew", padx=20, pady=5)
        self.password_text.insert("0.0", "Votre mot de passe : ")
        self.password_text.configure(state='disabled') 

        self.password_box = customtkinter.CTkTextbox(master=self, width=200, height=48, corner_radius=10, bg_color= DARK_BLUE, fg_color= SOFT_YELLOW, text_color = DARK_BLUE) # champs "email"
        self.password_box.grid(row=4, column=0, sticky="sew", padx=20, pady=0)
        self.password_box.insert("0.0", "")

        # lecker_font = change_font(TITLE_FONT, 30)

        self.button = customtkinter.CTkButton(self, font=(TEXT_FONT, 30), text="Se connecter", command=self.button_callbck, corner_radius=7, bg_color= DARK_BLUE, fg_color = PINK) # bouton se connecter
        self.button.grid(row=6, column=0, padx=20, pady=20)
    
    def login_screen_destroy(self):
        self.email_text.destroy()
        self.email_box.destroy()
        self.password_text.destroy()
        self.password_box.destroy()
        self.button.destroy()
    
    def interface_screen_build(self):
        self.button = customtkinter.CTkButton(self, text="Se déconnecter", command=self.button_callbck_logout, corner_radius=10, bg_color=DARK_BLUE, fg_color = PINK)
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

client_account_interface = Interface()
client_account_interface.mainloop()
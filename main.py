import customtkinter
import time

class Interface_frames:
    pass

class Interface(customtkinter.CTk, Interface_frames):
    def __init__(self):
        super().__init__()
        self.current_scene = "broad_view"
        self.geometry("640x480")
        self.title("Connexion Client")
        self.columnconfigure((0), weight=1)
        self.login_screen_build()
    
    def login_screen_build(self):
        self.textbox = customtkinter.CTkTextbox(master=self, width=200, height=48, corner_radius=10)
        self.textbox.grid(row=0, column=0, sticky="sew", padx=20, pady=20)
        self.textbox.insert("0.0", "adresse mail")
        self.button = customtkinter.CTkButton(self, text="Se connecter", command=self.button_callbck, corner_radius=10)
        self.button.grid(row=1, column=0, padx=20, pady=20)
    
    def login_screen_destroy(self):
        self.textbox.destroy()
        self.button.destroy()
    
    def interface_screen_build(self):
        self.button = customtkinter.CTkButton(self, text="Se déconnecter", command=self.button_callbck, corner_radius=10)
        self.button.grid(row=1, column=0, padx=20, pady=20)

    def interface_screen_destroy(self):
        self.button.destroy()

    def button_callbck(self):
        print("Connexion réussie")
        self.login_screen_destroy()
        self.interface_screen_build()
        self.confirmed = True

client_account_interface = Interface()
client_account_interface.mainloop()
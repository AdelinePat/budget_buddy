import customtkinter
from view.interface import Interface
from view.dashboard import Dashboard
from model.server import ServerDatabase
from model.login_info import LoginInfo
from model.customexception import LogInDataException
from view.scrollable_frame import Scrollable_frame
from view.interface_frames import Interface_frames
from view.__settings__ import DARK_BLUE, YELLOW, SOFT_YELLOW, PINK
from controller.login_data_manager import LoginManager
from data_access.read_user_data import UserDataAcess

class LogInOut(Interface):
    def __init__(self, window_title, column_number):
        super().__init__(window_title, column_number)
        self.controller = LoginManager()
        self.password_visible = False
        self.eye_open, self.eye_closed = self.util.get_eye_icons()
        self.log_info = LoginInfo()
        self.database = ServerDatabase()
        self.connected = False
        self.dashboard = self.create_dashboard()
        self.login_screen_build()
        # self.lift() 
        # self.attributes("-topmost", True)
        self.__data_acces = UserDataAcess()
        self.__all_users = self.__data_acces.get_all_users()

    def create_dashboard(self):
        if self.connected == True:
            self.dashboard = Dashboard(self, "Budget Buddy - Dashboard", 1, self.log_info)
        else:
            self.dashboard = None

    def login_screen_build(self):       
        if hasattr(self, 'scrollable_frame'):
            delattr(self, 'scrollable_frame')
        self.set_interface_frame()

        self.interface_frame.title_text = self.build_label("Budget Buddy", 0, color=YELLOW, custom_font=self.title_font, padvertical=(20,10), justify="center")
        self.interface_frame.subtitle_text = self.build_label("Votre application bancaire préférée".upper(), 1, color=YELLOW, custom_font=self.subtitle_font, padvertical=(5,20), justify="center")

        self.interface_frame.email_entry = self.build_label("Votre adresse email :", 3)

        self.interface_frame.email_box = customtkinter.CTkTextbox(master=self.interface_frame, font=self.text_font, width=200, height=48, corner_radius=10, bg_color= DARK_BLUE, fg_color= SOFT_YELLOW, text_color = DARK_BLUE)
        self.interface_frame.email_box.grid(row=4, column=0, sticky="sew", padx=20, pady=(2,5))
        self.interface_frame.email_box.insert("0.0", "")

        self.interface_frame.password_entry = self.build_label("Votre mot de passe :", 5)

        self.interface_frame.password_box = customtkinter.CTkEntry(master=self.interface_frame, font=self.text_font, width=200, height=48, corner_radius=10, bg_color= DARK_BLUE, fg_color= SOFT_YELLOW, text_color = DARK_BLUE, show="*")
        self.interface_frame.password_box.grid(row=6, column=0, sticky="sew", padx=20, pady=(2,5))

        self.interface_frame.show_password_button = customtkinter.CTkButton(
            master=self.interface_frame, 
            text="",  
            width=40, 
            image=self.eye_closed,  
            command=self.toggle_password,
            fg_color=SOFT_YELLOW,
            bg_color=SOFT_YELLOW,
            hover = False,
            border_width=0,
            corner_radius=0
        )

        self.interface_frame.show_password_button.grid(row=6, column=0, padx=(0,30), sticky="e")

        self.interface_frame.login_button = customtkinter.CTkButton(master=self.interface_frame,
                                                text="Se connecter".upper(),
                                                font=self.text_font,
                                                command=self.login_button_callback,
                                                corner_radius=7,
                                                bg_color=DARK_BLUE,
                                                fg_color=PINK)
        
        self.interface_frame.login_button.grid(row=7, column=0, padx=20, pady=(10,5))

        self.interface_frame.button_create_account = customtkinter.CTkButton(master=self.interface_frame, text="Créer un compte".upper(), font=self.text_font, command=self.signin_button_callback, corner_radius=7, bg_color=DARK_BLUE, fg_color=PINK)
        self.interface_frame.button_create_account.grid(row=8, column=0, padx=20, pady=5)

        self.interface_frame.quit_button = self.build_quit_button(self.interface_frame)

    def build_quit_button(self, master):
        button_quit = customtkinter.CTkButton(master=master,
                                            text="Quitter".upper(),
                                            font=self.text_font,
                                            command=self.quit_app,
                                            corner_radius=7,
                                            bg_color= DARK_BLUE,
                                            fg_color = PINK) # button for quitting app
        
        button_quit.grid(row=18, column=0, sticky="", padx=20, pady=(5,10))
        return button_quit

    def quit_app(self):
        self.destroy()

    def build_return_button(self, master):
        self.scrollable_frame.button_return = customtkinter.CTkButton(master=master,
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

        self.scrollable_frame.lastname_label.destroy()
        self.scrollable_frame.lastname_box.destroy()

        self.scrollable_frame.firstname_label.destroy()
        self.scrollable_frame.firstname_box.destroy()

        
        self.scrollable_frame.email_label.destroy()
        self.scrollable_frame.email_box.destroy()

        self.scrollable_frame.password_label.destroy()
        self.scrollable_frame.password_box.destroy()

        self.scrollable_frame.show_password_button.destroy()

        self.scrollable_frame.confirm_password_label.destroy()
        self.scrollable_frame.confirm_password_box.destroy()

        
        self.scrollable_frame.button_register.destroy()

        self.scrollable_frame.button_return.destroy()

        self.scrollable_frame.quit_button.destroy()

        if hasattr(self, 'login_text'):
            self.login_text.destroy()

        if hasattr(self, 'scrollable_frame'):
            self.scrollable_frame.destroy()
            delattr(self, 'scrollable_frame')

    def build_label_scrollable_frame(self, label_text, row_number, color=SOFT_YELLOW, custom_font=None, padvertical=(5,2), justify="left", anchor="w"):
        if custom_font == None:
            custom_font = self.text_font
        if justify != "left":
            anchor="center"

        my_label = customtkinter.CTkLabel(self.scrollable_frame,
                                          text=label_text,
                                          font=custom_font,
                                          text_color=color,
                                          bg_color=DARK_BLUE,
                                          justify=justify,
                                          anchor=anchor)
        my_label.grid(row=row_number, column=0, sticky="ew", padx=20, pady=padvertical)
        return my_label

    def build_label(self, label_text, row_number, color=SOFT_YELLOW, custom_font=None, padvertical=(5,2), justify="left", anchor="w"):
        if custom_font == None:
            custom_font = self.text_font

        if justify != "left":
            anchor="center"

        my_label = customtkinter.CTkLabel(self.interface_frame,
                                          text=label_text,
                                          font=custom_font, 
                                          text_color=color, 
                                          bg_color=DARK_BLUE, 
                                          justify=justify,
                                          anchor=anchor)
        my_label.grid(row=row_number, column=0, sticky="ew", padx=20, pady=padvertical)
        return my_label

    def set_scrollable_bar(self):
        self.scrollable_frame = Scrollable_frame(self, bg_color=DARK_BLUE, fg_color=DARK_BLUE, height=700)
        self.scrollable_frame.rowconfigure(0, weight=1)
        self.scrollable_frame.columnconfigure(0, weight=1)
        # self.scrollable_frame.pack(fill='both', expand=1)
        self.scrollable_frame.grid(row=0, column=0, sticky="snew")

    def set_interface_frame(self):
        self.interface_frame = Interface_frames(self, bg_color=DARK_BLUE, fg_color=DARK_BLUE)
        self.interface_frame.configure(height=500)
        self.interface_frame.columnconfigure(0, weight=1)
        self.interface_frame.grid(column=0, row=0, sticky="snew")
    
    def signin_button_callback(self):
        self.login_screen_destroy()
        self.register_screen_build()

    def register_screen_build(self):
        self.set_scrollable_bar()

        # Title
        self.scrollable_frame.title_text = self.build_label_scrollable_frame("Créer un compte", 0, color=YELLOW, custom_font=self.title_font, padvertical=(20,10), justify="center")

        # Lastname
        self.scrollable_frame.lastname_label = self.build_label_scrollable_frame("Nom :", 1)

        self.scrollable_frame.lastname_box = customtkinter.CTkEntry(self.scrollable_frame, font=self.text_font, height=48, corner_radius=10, bg_color=DARK_BLUE, fg_color=SOFT_YELLOW, text_color=DARK_BLUE)
        self.scrollable_frame.lastname_box.grid(row=2, column=0, sticky="ew", padx=20, pady=(2,5))

        # Firstname
        self.scrollable_frame.firstname_label = self.build_label_scrollable_frame("Prénom :", 3)

        self.scrollable_frame.firstname_box = customtkinter.CTkEntry(self.scrollable_frame, font=self.text_font, height=48, corner_radius=10, bg_color=DARK_BLUE, fg_color=SOFT_YELLOW, text_color=DARK_BLUE)
        self.scrollable_frame.firstname_box.grid(row=4, column=0, sticky="ew", padx=20, pady=(2,5))

        # Email
        self.scrollable_frame.email_label = self.build_label_scrollable_frame("Email :", 5)

        self.scrollable_frame.email_box = customtkinter.CTkEntry(self.scrollable_frame, font=self.text_font, height=48, corner_radius=10, bg_color=DARK_BLUE, fg_color=SOFT_YELLOW, text_color=DARK_BLUE)
        self.scrollable_frame.email_box.grid(row=6, column=0, sticky="ew", padx=20, pady=(2,5))

        # Password
        self.scrollable_frame.password_label = self.build_label_scrollable_frame("Mot de passe :", 7)

        self.scrollable_frame.password_box = customtkinter.CTkEntry(self.scrollable_frame, font=self.text_font, height=48, corner_radius=10, bg_color=DARK_BLUE, fg_color=SOFT_YELLOW, text_color=DARK_BLUE, show="*")
        self.scrollable_frame.password_box.grid(row=8, column=0, sticky="ew", padx=20, pady=(2,5))

        # Button show/hide password field
        self.scrollable_frame.show_password_button = customtkinter.CTkButton(
            master=self.scrollable_frame, 
            text="",  
            width=40, 
            image=self.eye_closed,  
            command=self.toggle_password_scrollable_frame,
            fg_color=SOFT_YELLOW,
            bg_color=SOFT_YELLOW,
            hover=False,
            border_width=0,
            corner_radius=0,
        )
        self.scrollable_frame.show_password_button.grid(row=8, column=0, padx=(0, 30), pady=(2,5), sticky="e")

        # Confirm password
        self.scrollable_frame.confirm_password_label = self.build_label_scrollable_frame("Confirmez le mot de passe :", 9)

        self.scrollable_frame.confirm_password_box = customtkinter.CTkEntry(self.scrollable_frame, font=self.text_font, height=48, corner_radius=10, bg_color=DARK_BLUE, fg_color=SOFT_YELLOW, text_color=DARK_BLUE, show="*")
        self.scrollable_frame.confirm_password_box.grid(row=10, column=0, sticky="ew", padx=20, pady=(2,5))

        # Signin button
        self.scrollable_frame.button_register = customtkinter.CTkButton(master=self.scrollable_frame,
                                                text="S'inscrire".upper(),
                                                font=self.text_font,
                                                command=self.register_callback, 
                                                corner_radius=7,
                                                bg_color=DARK_BLUE,
                                                fg_color=PINK)
        
        self.scrollable_frame.button_register.grid(row=11, column=0, padx=20, pady=10, sticky="")

        self.build_return_button(self.scrollable_frame)
        self.scrollable_frame.quit_button = self.build_quit_button(self.scrollable_frame)

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
        
            self.controller.register_user(self.log_info) #account_type,account_name,balance,min_balance
            self.build_login_result(self.scrollable_frame, 20, "Compte créé avec succès !")
        except LogInDataException as e:
            self.build_login_result(self.scrollable_frame,20, e)



    def toggle_password_scrollable_frame(self):
        if self.scrollable_frame.password_box.cget('show') == '*':
            self.scrollable_frame.password_box.configure(show="")
            if hasattr(self.scrollable_frame, 'confirm_password_box'):
                self.scrollable_frame.confirm_password_box.configure(show="")
            self.scrollable_frame.show_password_button.configure(image=self.eye_open)
        else:
            self.scrollable_frame.password_box.configure(show="*")
            if hasattr(self.scrollable_frame, 'confirm_password_box'):
                self.scrollable_frame.confirm_password_box.configure(show="*")
            self.scrollable_frame.show_password_button.configure(image=self.eye_closed)

    def toggle_password(self):
        if self.interface_frame.password_box.cget('show') == '*':
            self.interface_frame.password_box.configure(show="")
            if hasattr(self, 'confirm_password_box'):
                self.interface_frame.confirm_password_box.configure(show="")
            self.interface_frame.show_password_button.configure(image=self.eye_open)
        else:
            self.interface_frame.password_box.configure(show="*")
            if hasattr(self, 'confirm_password_box'):
                self.interface_frame.confirm_password_box.configure(show="*")
            self.interface_frame.show_password_button.configure(image=self.eye_closed)

    def login_screen_destroy(self):
        # destroy titles
        self.interface_frame.title_text.destroy()
        self.interface_frame.subtitle_text.destroy()

        # destroy label and box for email
        self.interface_frame.email_entry.destroy()
        self.interface_frame.email_box.destroy()

        # destroy label, box and button for password
        self.interface_frame.password_entry.destroy()
        self.interface_frame.password_box.destroy()
        self.interface_frame.show_password_button.destroy()

        # destroy all buttons
        self.interface_frame.login_button.destroy()
        self.interface_frame.button_create_account.destroy()
        self.interface_frame.quit_button.destroy()
        if hasattr(self, 'interface_frame'):
            self.interface_frame.destroy()
            delattr(self, 'interface_frame')


    def build_logout_button(self):
        self.scrollable_frame.button = customtkinter.CTkButton(master=self.scrollable_frame, text="Se déconnecter".upper(), font=self.text_font, command=self.button_callbck_logout, corner_radius=10, bg_color=DARK_BLUE, fg_color=PINK)
        self.scrollable_frame.button.grid(row=1, column=0, padx=20, pady=20)

    def logout(self):
        self.interface_screen_destroy()
        self.login_screen_build()
        if hasattr(self, 'login_text'):
            self.login_text.destroy()

    def interface_screen_destroy(self):
        self.button.destroy()

    def login_button_callback(self):
        if hasattr(self, 'login_text'):
            self.login_text.destroy()

        email = self.interface_frame.email_box.get("1.0", "end").strip()
        password = self.interface_frame.password_box.get().strip()
        try:
            self.controller.validate_email(email)
            self.log_info.set_id_user(self.__data_acces.get_user_id_from_email(email))

            self.controller.validate_password(password)
            stored_hashed_password = self.__data_acces.get_password_from_id_user(self.log_info.get_user_id())

            if self.controller.check_password(stored_hashed_password, password):
                self.login_screen_destroy()
                self.connected = True
                if hasattr(self, 'scrollable_frame'):
                    delattr(self, 'scrollable_frame')
                self.create_dashboard()
                self.dashboard.build_dashboard()
            elif self.connected == False:
                if not hasattr(self.interface_frame, 'email_entry'):
                    self.login_screen_build()
               
        except LogInDataException as e:
            self.build_login_result(self, 3, e)


    def build_login_result(self, master, row1, error_message):
        self.login_text = customtkinter.CTkLabel(master=master, text=error_message, font=self.text_font, text_color=SOFT_YELLOW, bg_color=DARK_BLUE, justify="left", anchor="w")
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



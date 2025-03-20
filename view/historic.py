import customtkinter
# import tkcalendar
# from CTkDatePicker import CTkDatePicker
from tkcalendar import Calendar
from view.interface import Interface
from view.interface_frames import Interface_frames
from view.__settings__ import DARK_BLUE, SOFT_BLUE, LIGHT_BLUE, YELLOW, SOFT_YELLOW, PINK

class Historic(Interface):
    def __init__(self, window_title, column_number):
        super().__init__(window_title, column_number)
        self.historic_frame = Interface_frames(self, fg_color=LIGHT_BLUE, width=200, bg_color=DARK_BLUE, corner_radius=20)
        self.historic_frame.columnconfigure(0, weight=1)
        self.historic_frame.grid(row=0, column=1, padx=20, pady=20, sticky="ew")
        self.shown_historic = "all_accounts"
        self.build_historic_interface()
    
    def build_historic_interface(self):
        self.historic_frame.historic_title = customtkinter.CTkLabel(
            self.historic_frame, text="Historique des transactions", 
            height=50, corner_radius=20,
            fg_color=SOFT_BLUE, text_color=LIGHT_BLUE, bg_color=DARK_BLUE
        )
        self.historic_frame.historic_title.grid(row=0, column=0, sticky="ew")
        self.recover_accounts()
        self.historic_dict_account[self.shown_historic]()
    
    def recover_accounts(self):
        self.historic_dict_account : dict = {}
        for account in list:
            pass

    def flip_historic_account(self, choice):
        self.historic_dict_account[self.shown_historic].destroy()
        self.shown_historic = choice
        self.historic_dict_account[self.shown_historic].build()
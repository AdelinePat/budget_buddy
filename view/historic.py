import customtkinter
# import tkcalendar
# from CTkDatePicker import CTkDatePicker
from view.interface import Interface
from view.interface_frames import Interface_frames
from view.__settings__ import DARK_BLUE, SOFT_BLUE, LIGHT_BLUE, YELLOW, SOFT_YELLOW, PINK
from view.account_view import Account_view

class Historic():
    def __init__(self, master, account_list, display_accounts, account_id):
        self.master = master
        
        self.shown_historic = account_id
        self.list_accounts = account_list
        self.display_accounts = display_accounts
        self.recover_accounts()

        self.master.historic_frame = Interface_frames(self.master, fg_color=LIGHT_BLUE, width=200, bg_color=DARK_BLUE, corner_radius=20)
        self.master.historic_frame.columnconfigure(0, weight=1)
        self.master.historic_frame.grid(row=0, column=1, padx=20, pady=20, sticky="ew")
        self.build_historic_interface()

    def build_historic_interface(self):
        self.master.historic_frame.historic_title = customtkinter.CTkLabel(
            self.master.historic_frame, text="Historique".upper(), font=self.master.subtitle_font,
            height=50, fg_color=SOFT_BLUE, text_color=LIGHT_BLUE
        )
        self.master.historic_frame.historic_title.grid(row=0, column=0, pady=20, sticky="ew")

        self.historic_dict_account[self.shown_historic].build(
            self.master.historic_frame,
            self.display_accounts[list(self.historic_dict_account.keys()).index(self.shown_historic)],
            self.master
        )
    
    def recover_accounts(self):
        self.historic_dict_account : dict = {}
        for index, account in enumerate(self.list_accounts):
            historic_account = Account_view(self.list_accounts[index][0])
            self.historic_dict_account.update(
                {str(account[0]) : historic_account}
            )

    def flip_historic_account(self, choice):
        self.historic_dict_account[self.shown_historic].destroy(self.master.historic_frame)
        self.historic_dict_account[self.shown_historic].destroy_factors_block_dict[self.historic_dict_account[self.shown_historic].current_filter]()
        self.shown_historic = choice[0]
        self.historic_dict_account[self.shown_historic].build(
            self.master.historic_frame,
            self.display_accounts[list(self.historic_dict_account.keys()).index(self.shown_historic)],
            self.master
        )

    def historic_destroy(self):
        
        # self.historic_dict_account[self.shown_historic].destroy()
        self.master.historic_frame.destroy()
        self.master.historic_frame.historic_title.destroy()

import customtkinter
from view.__settings__ import SOFT_BLUE, LIGHT_BLUE
from view.account_view import Account_view
from view.utiltool import UtilTool

class Historic():
    def __init__(self, master, account_list, display_accounts, account_id):
        self.master = master
        self.util = UtilTool()
        self.title_font = self.util.get_title_font(30)
        self.text_font = self.util.get_text_font(15)
        self.subtitle_font = self.util.get_text_font(25)
        
        self.shown_historic = account_id
        self.list_accounts = account_list
        self.display_accounts = display_accounts
        self.recover_accounts()
        self.build_historic_interface()

    def build_historic_interface(self):
        self.master.historic_title = customtkinter.CTkLabel(
            self.master, text="Historique".upper(), font=self.subtitle_font,
            height=50, fg_color=SOFT_BLUE, text_color=LIGHT_BLUE
        )
        self.master.historic_title.grid(row=0, column=0, pady=20, sticky="ew")

        self.historic_dict_account[self.shown_historic].build(
            self.master,
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
        self.historic_dict_account[self.shown_historic].destroy(self.master)
        self.historic_dict_account[self.shown_historic].destroy_factors_block_dict[self.historic_dict_account[self.shown_historic].current_filter]()
        self.shown_historic = choice[0]
        self.historic_dict_account[self.shown_historic].build(
            self.master,
            self.display_accounts[list(self.historic_dict_account.keys()).index(self.shown_historic)],
            self.master
        )

    def historic_destroy(self):
        self.master.destroy()
        self.master.historic_title.destroy()

import customtkinter
from view.__settings__ import DARK_BLUE, SOFT_BLUE, LIGHT_BLUE, YELLOW, SOFT_YELLOW, PINK

from view.transactions_frame import Transactions_frame

class Historic_Account:
    def __init__(self, list_args):
        self.account_id, self.user_id, self.account_type, self.account_name, self.account_amount, self.account_minimum = list_args
        self.list_transactions : list = [
            (1, 1, "hihi",50,"2025-15-03","virement","nourriture","NULL"),
            (2, 5, "hihi",50,"2025-15-03","virement","nourriture","NULL"),
            (3, 3, "hihi",50,"2025-15-03","virement","nourriture","NULL"),
            (4, 3, "hihi",50,"2025-15-03","virement","nourriture","NULL"),
            (5, 3, "hihi",50,"2025-15-03","virement","nourriture","NULL"),
            (6, 1, "hihi",50,"2025-15-03","virement","nourriture","NULL"),
            (7, 2, "hihi",50,"2025-15-03","virement","nourriture","NULL"),
            (8, 5, "hihi",50,"2025-15-03","virement","nourriture","NULL"),
            (9, 7, "hihi",50,"2025-15-03","virement","nourriture","NULL")
        ]
    
    def build(self, master, title):
        master.account_title = customtkinter.CTkLabel(
            master, text=title, 
            height=50,
            fg_color=SOFT_BLUE, text_color=LIGHT_BLUE
        )
        master.account_title.grid(
            row=2, column=0,
            pady=20, sticky="ew"
        )
        master.transactions_frame = Transactions_frame(master, fg_color=SOFT_BLUE, bg_color=LIGHT_BLUE, corner_radius=5)
        master.transactions_frame.grid(row=4,column=0,padx=15, pady=5, sticky="ew")
        # for index, transaction in enumerate(self.list_transactions):
        #     master.transactions_frame.transactions_element

    def destroy(self, master):
        master.account_title.destroy()
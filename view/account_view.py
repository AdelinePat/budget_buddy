import customtkinter
from view.__settings__ import DARK_BLUE, SOFT_BLUE, LIGHT_BLUE, YELLOW, SOFT_YELLOW, PINK

from view.scrollable_frame import Scrollable_frame
from model.historic_transaction_model import Historic_Transaction

class Account_view:
    def __init__(self, list_args):
        self.account_id, self.user_id, self.account_type, self.account_name, self.account_amount, self.account_minimum = list_args
        self.list_transactions : list = [
            (1, 1, 2, "Virement interne",50,"2025-15-03","virement",1,"Restaurant, café, snack","NULL"),
            (2, 5, 4, "Virement interne",50,"2025-15-03","virement",1,"Restaurant, café, snack","NULL"),
            (3, 3, 45, "Virement interne",50,"2025-15-03","virement",1,"Restaurant, café, snack","NULL"),
            (4, 3, 56, "Virement interne",50,"2025-15-03","virement",1,"Restaurant, café, snack","NULL"),
            (5, 3, 5, "Virement interne",50,"2025-15-03","virement",1,"Restaurant, café, snack","NULL"),
            (6, 1, 2, "Virement interne",50,"2025-15-03","virement",1,"Restaurant, café, snack","NULL"),
            (7, 2, 6, "Virement interne",50,"2025-15-03","virement",1,"Impôts, banque, taxes","NULL"),
            (8, 5, 456, "Virement interne",50,"2025-15-03","virement",1,"Impôts, banque, taxes","NULL"),
            (9, 7, 1, "Virement interne",50,"2025-15-03","virement",1,"Impôts, banque, taxes","NULL"),
            (1, 1, 2, "Virement interne",50,"2025-15-03","virement",1,"Impôts, banque, taxes","NULL"),
            (2, 5, 4, "Virement interne",50,"2025-15-03","virement",1,"Impôts, banque, taxes","NULL"),
            (3, 3, 45, "Virement interne",50,"2025-15-03","virement",1,"Loisirs","NULL"),
            (4, 3, 56, "Virement interne",50,"2025-15-03","virement",1,"Loisirs","NULL"),
            (5, 3, 5, "Virement interne",50,"2025-15-03","virement",1,"Loisirs","NULL"),
            (6, 1, 2, "Virement interne",50,"2025-15-03","virement",1,"Loisirs","NULL"),
            (7, 2, 6, "Virement interne",50,"2025-15-03","virement",1,"Loisirs","NULL"),
            (8, 5, 456, "Virement interne",50,"2025-15-03","virement",1,"Loisirs","NULL"),
            (9, 7, 1, "Virement interne",50,"2025-15-03","virement",1,"Loisirs","NULL")
        ]
    
    def build(self, master, title, interface):
        master.account_title = customtkinter.CTkLabel(
            master, text=title, font=interface.text_font,
            height=50,
            fg_color=SOFT_BLUE, text_color=LIGHT_BLUE
        )
        master.account_title.grid(
            row=2, column=0,
            pady=20, sticky="ew"
        )
        master.transactions_frame = Scrollable_frame(master, fg_color=SOFT_BLUE, bg_color=LIGHT_BLUE, corner_radius=5)
        master.transactions_frame.columnconfigure((0), weight=1)
        master.transactions_frame.grid(row=4,column=0,padx=15, pady=5, sticky="ew")
        self.account_transactions = []
        for index, transaction in enumerate(self.list_transactions):
            if transaction[1] == self.account_id or transaction[2] == self.account_id:
                transaction_element = Historic_Transaction(master.transactions_frame, transaction, interface, fg_color=LIGHT_BLUE, height=60)
                transaction_element.grid(row=index, column=0, sticky="ew", pady=5, padx=2)
                self.account_transactions.append(transaction_element)

    def destroy(self, master):
        master.account_title.destroy()
        master.transactions_frame.destroy()
        for transaction in self.account_transactions:
            transaction.destroy()
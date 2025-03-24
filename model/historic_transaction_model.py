import customtkinter
from view.__settings__ import LIGHT_BLUE

class Historic_Transaction(customtkinter.CTkFrame):
    def __init__(self, master, transaction_infos, interface, **kwargs):
        super().__init__(master, **kwargs)
        self.columnconfigure(1, weight=1)
        self.master = master
        self.interface = interface
        self.transaction_infos = transaction_infos
        self.build()
    
    def build(self):
        self.transaction_description = customtkinter.CTkLabel(
            self, bg_color=LIGHT_BLUE, text=self.transaction_infos[0],
            font=self.interface.text_font, anchor="w"
        )
        self.transaction_amount = customtkinter.CTkLabel(
            self, bg_color=LIGHT_BLUE, text=str(self.transaction_infos[1])+" €",
            font=self.interface.text_font, anchor="e"
        )
        self.transaction_date = customtkinter.CTkLabel(
            self, bg_color=LIGHT_BLUE, text=self.transaction_infos[2],
            font=self.interface.text_font, anchor="w"
        )
        self.transaction_category = customtkinter.CTkLabel(
            self, bg_color=LIGHT_BLUE, text=self.transaction_infos[3],
            font=self.interface.text_font
        )
        self.transaction_description.grid(row=0,column=0, padx=10, sticky="w")
        self.transaction_amount.grid(row=0, column=1, padx=10, sticky="e")
        self.transaction_date.grid(row=1, column=0, padx=10, sticky="w")
        self.transaction_category.grid(row=1, column=1, padx=10, sticky="we")

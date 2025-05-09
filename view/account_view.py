import customtkinter
from view.utiltool import UtilTool
from view.scrollable_frame import Scrollable_frame
from view.__settings__ import DARK_BLUE, SOFT_BLUE,\
                            LIGHT_BLUE, SOFT_YELLOW,\
                            CATEGORY_LIST, DEAL_TYPE_LIST
from model.historic_transaction_model import Historic_Transaction
from data_access.write_historic_query import HistoricQuery

class Account_view:
    def __init__(self, account_id, login_info):
        # self.login_info = login_info
        # self.account_id = login_info.get_current_account()
        self.user_id = login_info.get_user_id()
        self.account_id = account_id
        self.util = UtilTool()

        self.database = HistoricQuery()
        self.build_factors_block_dict : dict = {
            "Voir tout" : self.build_all,
            "Par catégorie" : self.build_category,
            "Par type" : self.build_type,
            "Par dates" : self.build_dates,
        }
        self.destroy_factors_block_dict : dict = {
            "Voir tout" : self.destroy_all,
            "Par catégorie" : self.destroy_category,
            "Par type" : self.destroy_type,
            "Par dates" : self.destroy_dates,
        }
        self.current_filter = "Voir tout"
    
    def build(self, master, title, interface):
        self.master = master
        self.interface = interface
        master.account_title = customtkinter.CTkLabel(
            master, text=title, font=self.util.text_font,
            height=50,
            fg_color=SOFT_BLUE, text_color=LIGHT_BLUE
        )
        master.account_title.grid(
            row=2, column=0,
            pady=20, sticky="ew"
        )
        master.filters = customtkinter.CTkComboBox(
            master,
            values=[
                "Voir tout", "Par catégorie", "Par type", "Par dates"
            ], command=self.flip_filters,
            font=self.util.text_font,
            text_color=DARK_BLUE,
            dropdown_text_color = DARK_BLUE,
            bg_color=LIGHT_BLUE,
            fg_color=SOFT_YELLOW,
            dropdown_fg_color = SOFT_YELLOW, 
            dropdown_font= self.util.text_font,
            dropdown_hover_color = SOFT_BLUE,
            corner_radius=15,
            state="readonly"
            
        )
        master.filters.grid(row=3, column=0, padx=10, pady=10, sticky="ew")
        self.destroy_factors_block_dict[self.current_filter]()
        self.current_filter = "Voir tout"
        self.current_factor = None
        self.build_historic()
    
    def build_historic(self):
        self.build_factors_block_dict[self.current_filter]()
        self.master.transactions_frame = Scrollable_frame(
            self.master,
            fg_color=SOFT_BLUE,
            bg_color=LIGHT_BLUE,
            corner_radius=5)
        
        self.master.transactions_frame.columnconfigure((0), weight=1)
        self.master.transactions_frame.grid(row=5,column=0,padx=15, pady=5, sticky="ew")

        # match self.current_filter:
        #     # "Voir tout", "Par catégorie", "Par type", "Par dates"
        #     case 'Voir tout':
        #         self.database.historic_query_all(self.account_id, self.user_id)
        #     case 'Par catégorie':
        #         self.database.historic_query_category(self.user_id, self.account_id, self.current_factor)
        #     case 'Par type':
        #         self.database.historic_query_type(self.user_id, self.account_id, self.current_factor)
        #         pass
        #     case 'Par dates':
        #         pass

        self.list_transactions = self.database.historic_queries_dict[self.current_filter](self.user_id,
            self.account_id,
            self.current_factor)

        self.account_transactions = []
        for index, transaction in enumerate(self.list_transactions):
            # if transaction[1] == self.account_id or transaction[2] == self.account_id:

                transaction_element = Historic_Transaction(
                    self.master.transactions_frame,
                    transaction,
                    self.interface,
                    fg_color=LIGHT_BLUE,
                    height=60)
                
                transaction_element.grid(row=index, column=0, sticky="ew", pady=5, padx=2)
                self.account_transactions.append(transaction_element)
    
    def destroy_historic(self):
        self.destroy_factors_block_dict[self.current_filter]()
        self.master.transactions_frame.destroy()
    
    def flip_filters(self, choice):
        self.destroy_historic()
        self.current_filter = choice
        self.build_historic()
    
    def flip_factors(self, choice):
        self.destroy_historic()
        self.current_factor = choice
        self.build_historic()
    
    def build_all(self):
        pass
    
    def build_category(self):
        self.master.category = customtkinter.CTkComboBox(
            self.master,
            values=CATEGORY_LIST,
            font=self.util.text_font,
            text_color=DARK_BLUE,
            dropdown_text_color = DARK_BLUE,
            bg_color=LIGHT_BLUE,
            fg_color=SOFT_YELLOW,
            dropdown_fg_color = SOFT_YELLOW, 
            dropdown_font= self.util.text_font,
            dropdown_hover_color = SOFT_BLUE,
            corner_radius=15,
            command=self.flip_factors,
            state="readonly"
        )
        self.master.category.grid(column=0, row=4, padx=10, pady=10, sticky="ew")
        self.master.category.set(CATEGORY_LIST[0])

    def build_type(self):
        self.master.type = customtkinter.CTkComboBox(
            self.master,
            values=DEAL_TYPE_LIST,
            font=self.util.text_font,
            text_color=DARK_BLUE,
            dropdown_text_color = DARK_BLUE,
            bg_color=LIGHT_BLUE,
            fg_color=SOFT_YELLOW,
            dropdown_fg_color = SOFT_YELLOW, 
            dropdown_font= self.util.text_font,
            dropdown_hover_color = SOFT_BLUE,
            corner_radius=15,
            command=self.flip_factors,
            state="readonly"
        )
        self.master.type.grid(column=0, row=4, padx=10, pady=10, sticky="ew")
        self.master.type.set(DEAL_TYPE_LIST[0])

    def build_dates(self):
        pass

    def destroy_all(self):
        pass

    def destroy_category(self):
        self.master.category.destroy()

    def destroy_type(self):
        self.master.type.destroy()
    
    def destroy_dates(self):
        pass

    def destroy(self, master):
        master.account_title.destroy()
        master.transactions_frame.destroy()
        for transaction in self.account_transactions:
            transaction.destroy()
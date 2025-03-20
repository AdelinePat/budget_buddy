from view.transactions import TransactionView
from model.transactionquery import TransactionQuery

class TransactionManager():
    def __init__(self, window_title, column_number, current_session):
        self.query = TransactionQuery()
        self.view = TransactionView(window_title, column_number, current_session)
        self.view.screen_build()
    
    def manage_deposit(self):
        if self.view.receiver == self.view.current_session:
            self.query.method_inexistant()
    
    def manage_withdrawal(self):
        pass

    def manage_transfer(self):
        if self.view.type_selected == 'Transfert':
            self.query.transfer_transaction(self.view.receiver, self.view.current_session)

    def run(self):
        self.manage_transfer()
        self.view.mainloop()
        

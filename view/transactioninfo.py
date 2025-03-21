class TransactionInfo():
    def __init__(self, current_session, deal_type, date, emitter, receiver, description, category, amount):
        self.current_session = current_session
        self.type = deal_type
        self.date = date
        self.__emitter = emitter
        self.__receiver = receiver
        self.description = description
        self.category = category
        self.__amount = amount
    
    def get_emitter(self):
        return self.__emitter
    
    def get_receiver(self):
        return self.__receiver
    
    def get_amount(self):
        return self.__amount
    
    def set_amount(self, new_value):
        self.__amount = new_value

    def set_emitter(self, new_value):
        self.__emitter = new_value

    def set_receiver(self, new_value):
        self.__receiver = new_value


        # self.type = type
        # self.date = date
        # self.emitter = emitter
        # self.receiver = receiver
        # self.description = description
        # self.categoy = category
        # self.amount = amount
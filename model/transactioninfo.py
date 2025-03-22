class TransactionInfo():
    def __init__(self, current_session, current_account, deal_type, date, emitter, receiver, description, category, amount):
        self.__current_session = current_session # user_id
        self.__current_account = current_account # account currently used
        self.__type = deal_type
        self.__date = date
        self.__emitter = emitter
        self.__receiver = receiver
        self.__description = description
        self.__category = category
        self.__amount = amount
    
    def get_current_session(self):
        return self.__current_session
    
    def get_current_account(self):
        return self.__current_account

    def get_type(self):
        return self.__type

    def get_date(self):
        return self.__date

    def get_emitter(self):
        return self.__emitter

    def get_receiver(self):
        return self.__receiver
    
    def get_description(self):
        return self.__description

    def get_category(self):
        return self.__category
    
    def get_amount(self):
        return self.__amount
    

    def set_type(self, new_value):
        self.__type = new_value

    def set_date(self, new_value):
        self.__date = new_value

    def set_emitter(self, new_value):
        self.__emitter = new_value

    def set_receiver(self, new_value):
        self.__receiver = new_value
    
    def set_description(self, new_value):
        self.__description = new_value

    def set_category(self, new_value):
        self.__category = new_value
    
    def set_amount(self, new_value):
        self.__amount = new_value

   
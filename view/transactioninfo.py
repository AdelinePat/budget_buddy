class TransactionInfo():
    def __init__(self, current_session, deal_type, date, emitter, receiver, description, category, amount):
        self.current_session = current_session
        self.type = deal_type
        self.date = date
        self.emitter = emitter
        self.receiver = receiver
        self.description = description
        self.category = category
        self.amount = amount

        # self.type = type
        # self.date = date
        # self.emitter = emitter
        # self.receiver = receiver
        # self.description = description
        # self.categoy = category
        # self.amount = amount
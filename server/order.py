import uuid


class Order(object):
    def __init__(self, stocks, quantity):
        self.orderID = uuid.uuid1()
        self.stocks = stocks
        self.quantity = quantity
        self.status = 'PENDING'

    def update_status(self, status):
        self.status = status

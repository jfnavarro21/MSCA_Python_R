# book, buy / sell side
# 3 functions add modify cancel
# goal is to give top of book()
#dictionary  order={ side": b/s, "quanty":100, , "price": 10, "symbol": MQ, "exchange": E1}
# sort the orders

#order={ "side": B, "quantity":100, "price": 10, "symbol" : MQ, "Exchange": E1, "orderid":1}


class orderbook():
    def __init__(self):
        self.buy = []
        self.sell = []

    def add(self, order):

        if order['side'] == 'B':
            self.buy.append(order)


        if order['side'] == 'S':
            self.sell.append(order)

        else:
            print('ERROR')


    def cancel(self, order):
        for i in self.buy:
            if order['orderid','exchange'] == i['orderid', 'exchange']:
                del i

        for i in self.sell:
            if order['orderid','exchange'] == i['orderid', 'exchange']:
                del i

    def modify(self, order):
        for i in buyside:
            if order['orderid'] == i['orderid'] and order['exchange'] == i['exchange']:
                # replace order['price'], replace order['quantity']



    def top_of_book(self):
        pass # return the best bid and offers
        # self.sell = sorted(self.sell, order['price'])
        # self.buy = sorted(self.buy, order['price'])

#http: // stackoverflow.com / questions / 72899 / how - do - i - sort - a - list - of - dictionaries - by - values - of - the - dictionary - in -python

import socket
import json
import csv
import pandas as pd
from orderbook import Orderbook
from strategy import Strategy
from ordermanager import OrderManager


class ClientConnection:
    def __init__(self, ob, om, strat):
        self.ob = ob
        self.om = om
        self.strat = strat
        self.host_ip, self.server_port = "127.0.0.1", 9995
        self.tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def send(self, order_to_send, order):
        #print (order_to_send)
        if order_to_send == 50:
            print('*************',self.om.execute_order_50)
            print('*************',self.om.hedge_order_50)
            json_order= json.dumps(self.om.execute_order_50)
            encode_order=json_order.encode('utf-8')
            self.tcp_client.send(encode_order)
            self.om.execute_order_50.clear()
            json_order = json.dumps(self.om.hedge_order_50)
            encode_order = json_order.encode('utf-8')
            self.tcp_client.send(encode_order)
            self.om.hedge_order_50.clear()

        elif order_to_send == 100:
            print('*************',self.om.execute_order_100)
            print('*************',self.om.hedge_order_100)
            json_order = json.dumps(self.om.execute_order_100)
            encode_order = json_order.encode('utf-8')
            self.tcp_client.send(encode_order)
            self.om.execute_order_100.clear()
            json_order = json.dumps(self.om.hedge_order_100)
            encode_order = json_order.encode('utf-8')
            self.tcp_client.send(encode_order)
            self.om.hedge_order_100.clear()

        else:
            print("Nothing to trade")

    def start(self):
        try:
            # connects using host and port
            self.tcp_client.connect((self.host_ip, self.server_port))
            while True:
                # stores recieved data in variable received, this is in bytes
                received = self.tcp_client.recv(1024)
                # decode received from bytes into string
                received_s = received.decode('utf8')
                # use json.loads to convert from string to dictionary
                order = (json.loads(received_s))
                print('New order: ' , order)
                # if the Action is A use add()
                if order['Action'] == 'A':
                    #print(self.ob.book)
                    self.ob.add(order)
                    # store order's Symbol as symbol
                    symbol = order['Symbol']
                    # Check that there is at least one order in the Buy and Sell list of the Orderbook
                    # for that symbol
                    if len(self.ob.book[symbol]['B']) > 0 and len(self.ob.book[symbol]['S']) > 0:
                        # run store_price on the order, print out the dicts of best bids and offers
                        self.strat.store_price(order, self.ob.book)
                        print('best bids/offers', self.strat.previous_orders_highest[order['Symbol']], self.strat.previous_orders_lowest[order['Symbol']])
                        # run trade_after_news, store as outcome, print out the orders
                        outcome=self.om.trade_after_news(order, self.strat)
                        # run send() to send orders to the client
                        self.send(outcome, order)
                        self.ob.clear_crossed_book(order, self.strat)
                        #print(self.ob.book)


                    else:
                        print('no trade, just add')

                    self.strat.store_signal(order)
                    print(self.strat.signal_table[order['Symbol']])

                elif order['Action'] == 'M':
                    #print(self.ob.book)
                    self.ob.modify(order)
                    symbol = order['Symbol']

                    if len(self.ob.book[symbol]['B']) > 0 and len(self.ob.book[symbol]['S']) > 0:
                        self.strat.store_price(order, self.ob.book)
                        print('best bids/offers', self.strat.previous_orders_highest[order['Symbol']], self.strat.previous_orders_lowest[order['Symbol']])
                        outcome=self.om.trade_after_news(order, self.strat)
                        self.send(outcome, order)
                        self.ob.clear_crossed_book(order, self.strat)
                        #print(self.ob.book)

                    else:
                        print('no trade, just modify')

                    self.strat.store_signal(order)
                    print(self.strat.signal_table[order['Symbol']])

        finally:
            print('The End!')


if __name__ == '__main__':
    the_strat = Strategy()
    the_om = OrderManager()
    the_ob = Orderbook()
    the_client = ClientConnection(the_ob, the_om, the_strat)
    the_client.start()

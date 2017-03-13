import socket
import json
import csv
import pandas as pd


class Strategy:
    def __init__(self):
        self.signal_table = {}
        self.previous_orders_highest = {}
        self.previous_orders_lowest = {}

    def store_signal(self, order):
        """Store the symbol & news as it's value."""
        self.signal_table[order['Symbol']] = order['News']


    def store_price(self, order, book):
        """Store the lowest and highest price from the orderbook when News > 0 """
        #if order['News'] >= '0':
        lowest = float(book[order['Symbol']]['S'][0]['Price'])
        for order_ in book[order['Symbol']]['S']:
            if float(order_['Price']) < lowest:
                lowest = float(order_['Price'])
        self.previous_orders_lowest[order['Symbol']] = lowest
        #print(type(lowest))
        #print(type(self.previous_orders_lowest[order['Symbol']]))
        highest = float(book[order['Symbol']]['B'][0]['Price'])
        for order_ in book[order['Symbol']]['B']:
            if float(order_['Price']) > highest:
                highest = float(order_['Price'])
        self.previous_orders_highest[order['Symbol']] = highest

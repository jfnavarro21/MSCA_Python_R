import socket
import json
import csv
import pandas as pd


class Orderbook:
    def __init__(self):
        self.book={}

    # def __get__(self):
    #     return: self.book

    # Dictionary of all the orderbooks, each symbol has one key, its values are a list of 2 Buy and Sell.
    # the Buy is a sorted list of dictionaries(the buy orders), the Sell is a sorted list of dictionaries(the sell orders)
    def add(self, order):
        # Add an order to the buy dict or sell dict for a specific Symbol
        # It updates the Orderbook.all in place
        if order['Symbol'] not in self.book:
            self.book[order['Symbol']] = {'B': [], 'S': []}  # make lists
        self.book[order['Symbol']][order['Side']].append(order)

    def modify(self, order):
        # need to make a list, loop through the list, looking at each dict for order ID
        try:
            if order['Symbol'] not in self.book:
                raise Exception("Symbol not in orderbook")
            for order_ in self.book[order['Symbol']][order['Side']]:
                #print(order_['OrderID'], order['OrderID'])
                if order_['OrderID'] == order['OrderID']:
                    order_['Price'] = order['Price']
                    order_['Quantity'] = order['Quantity']
                    order_['Action'] = order['Action']
                    order_['News'] = order['News']
                else:
                    print("order doesn't exist, cant modify")
        except Exception as e:
            print(str(e))

    def clear_crossed_book(self, order, strategy_object):
        if strategy_object.previous_orders_highest[order['Symbol']] > strategy_object.previous_orders_lowest[order['Symbol']]:
            print("book is crossed")
            if order['Side']=='S':
                for order_ in self.book[order['Symbol']]['S']:
                    #print(order_['OrderID'], order['OrderID'])
                    if order_['OrderID'] == order['OrderID']:
                        order_['Price'] = '2000'
                        #print(order_['Price'])
                    else:
                        print("can't set to 2000")


            elif order['Side']=='B':
                for order_ in self.book[order['Symbol']]['B']:
                    #print(order_['OrderID'], order['OrderID'])
                    if order_['OrderID'] == order['OrderID']:
                        order_['Price'] = '1'
                        #print(order_['Price'])
                    else:
                        print("can't set to 1")

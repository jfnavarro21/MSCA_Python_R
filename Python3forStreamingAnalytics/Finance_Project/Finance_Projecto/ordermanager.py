import socket
import json
import csv
import pandas as pd



class OrderManager:
    def __init__(self):
        self.execute_order_50 = {}
        self.execute_order_100 = {}
        self.hedge_order_50 = {}
        self.hedge_order_100 = {}
        # buy 50 sell 100

    def trade_after_news(self, order, strategy_object):
        '''Creates 2 excution orders based on signal_table's value
            and incoming order's Price and Side'''
        print('Calling trade_after_news')
        if order['Symbol'] not in strategy_object.signal_table.keys():
            print('Symbol NOT in signal_table.keys')
            strategy_object.store_signal(order)
        elif order['Symbol'] in strategy_object.signal_table.keys():
            print('Symbol in signal_table.keys')
            if strategy_object.signal_table[order['Symbol']] == '50':
                print('value is 50')
                if float(order['Price']) < strategy_object.previous_orders_highest[order['Symbol']]:
                    #print("price is lower")
                    if order['Side'] == 'S':
                        self.execute_order_50 = order.copy()
                        self.execute_order_50['Side'] = 'B'
                        self.execute_order_50['Action'] = 'A'
                        self.hedge_order_50 = order.copy()
                        self.hedge_order_50['Price'] = strategy_object.previous_orders_highest[order['Symbol']]
                        self.hedge_order_50['Action'] = 'A'
                        print('orders_created_50')
                        return 50

            elif strategy_object.signal_table[order['Symbol']] == '100':
                print('value is 100')
                if float(order['Price']) > strategy_object.previous_orders_lowest[order['Symbol']]:
                    #print("price is higher")
                    if order['Side'] == 'B':
                        print("order is buy side")
                        self.execute_order_100 = order.copy()
                        self.execute_order_100['Side'] = 'S'
                        self.execute_order_100['Action'] = 'A'
                        self.hedge_order_100 = order.copy()
                        self.hedge_order_100['Price'] = strategy_object.previous_orders_lowest[order['Symbol']]
                        self.hedge_order_100['Action'] = 'A'
                        print('orders_created_100')
                        return 100
            elif strategy_object.signal_table[order['Symbol']] == '0':
                print('signal_table is 0')



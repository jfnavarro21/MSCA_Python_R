##  make client, json dumps/loads. client contains the model, execute orders against ones in the book
#client, connect 9995, for loop (true), read data (recv) JSON loads, take string convert to object.  sendall dumps
# classes: connect, orderbook, model, execution

# Task 0: Learn how to connect to rcc

import socket
import json
import csv
import pandas as pd

host_ip, server_port = "127.0.0.1", 9995



data =[]

# function to create a client
def work_with_server():
    global data
    # creates tcp_client as a socket object
    tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # connects using host and port
        tcp_client.connect((host_ip, server_port))

        while True:
            # stores recieved data in variable received, this is in bytes
            received = tcp_client.recv(1024)
            # decode received from bytes into string
            received_s = received.decode( 'utf8')
            # use json.loads to convert from string to dictionary
            received_d = (json.loads(received_s))

            # will break loop if data stops
            if not received:
                break
            # appends received dictionaries into the list data
            data.append(received_d)
            print(len(data))
            if len(data)==20:
                break
    # closes the connection and prints the list
    finally:
        tcp_client.close()
        print(data)


    df = pd.DataFrame(data)
    print(df)
    print(type(df))

    # data_j = json.dumps(data)
    # print(type(data_j))




    # turn data (list of dicts) to a csv
    # from http://stackoverflow.com/questions/3086973/how-do-i-convert-this-list-of-dictionaries-to-a-csv-file-python
    # keys = data[0].keys()
    # with open('orders.csv', 'wb') as output_file:
    #     dict_writer = csv.DictWriter(output_file, keys)
    #     dict_writer.writeheader()
    #     dict_writer.writerows(data)
# calls work_with_server function

# # Create orderbook
#
# class orderbook():
#     def __init__(self):
#         self.buy = []
#         self.sell = []
#
#     def add(self, order):
#
#         if order['side'] == 'B':
#             self.buy.append(order)
#
#
#         if order['side'] == 'S':
#             self.sell.append(order)
#
#         else:
#             print('ERROR')
#
#
#     def cancel(self, order):
#         if order['side'] == 'B':
#             for i in self.buy:
#                 if order['orderid'] == i['orderid'] and order['exchange'] == i['exchange']:
#                     del order[i]
#
#         if order['side'] == 'S':
#             for i in self.sell:
#                 if order['orderid'] == i['orderid'] and order['exchange'] == i['exchange']:
#                     del order[i]
#
#         else:
#             print('ERROR')
#
#     def modify(self, order):
#         if order['side'] == 'B':
#             for i in self.buy:
#                 if order['orderid'] == i['orderid'] and order['exchange'] == i['exchange'] and order['price'] != i['price'] or order['quantity'] != i['quantity']:
#                     # replace order['price'], replace order['quantity']
#                     i['price'] = order['price']
#                     i['quantity'] = order['quantity']
#                 break
#
#         if order['side'] == 'S':
#             for i in self.sell:
#                 if order['orderid'] == i['orderid'] and order['exchange'] == i['exchange'] and order['price'] != i['price'] or order['quantity'] != i['quantity']:
#                     # replace order['price'], replace order['quantity']
#                     i['price'] = order['price']
#                     i['quantity'] = order['quantity']
#                 break
#
#         else:
#             print('ERROR')
#
#     def top_of_book(self, order):
#         # return the best bid and offers
#         # use sorted() to reorganize the book by key 'price', one of the books is reversed
#         self.sell = sorted(self.sell, order['price'], reverse=True)
#         self.buy = sorted(self.buy, order['price'])
#         # print the first item in each list
#         print(self.sell[0], self.buy[0])


work_with_server()
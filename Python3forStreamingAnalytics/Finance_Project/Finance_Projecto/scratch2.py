from orderbook import Orderbook
from strategy import Strategy
from ordermanager import OrderManager
from client import ClientConnection


# create orderbook object
# call add method
# pass test_1 to add method
# you should get back DOB as expected output


test_1 = {
    "Symbol": "ADBE",
    "OrderID": "001",
    "Action": "A",
    "Exchange": "1",
    "Quantity": "189000",
    "News": "0",
    "Side": "B",
    "Description": "Adobe",
    "Price": "113.36"
}

test_2 = {
    "Symbol": "ADBE",
    "OrderID": "002",
    "Action": "A",
    "Exchange": "1",
    "Quantity": "329000",
    "News": "50",
    "Side": "S",
    "Description": "Adobe",
    "Price": "118.41"
}


order_book_1 = Orderbook()
order_book_1.add(test_1)
# print(Orderbook.all)
order_book_1.add(test_2)
#print(Orderbook.all)

assert len(order_book_1.book['ADBE']['B']) == 1
assert len(order_book_1.book['ADBE']['S']) == 1

test_3 = {
    "Symbol": "ADBE",
    "OrderID": "002",
    "Action": "M",
    "Exchange": "1",
    "Quantity": "362000",
    "News": "0",
    "Side": "S",
    "Description": "Adobe",
    "Price": "119.76"
}

before_modify = order_book_1.book.copy
order_book_1.modify(test_3)
#print(order_book_1.book)
assert before_modify != order_book_1.book

test_4 = {
    "Symbol": "ADBE",
    "OrderID": "004",
    "Action": "A",
    "Exchange": "1",
    "Quantity": "189000",
    "News": "0",
    "Side": "B",
    "Description": "Adobe",
    "Price": "113.36"
}

test_5 = {
    "Symbol": "ADBE",
    "OrderID": "005",
    "Action": "A",
    "Exchange": "1",
    "Quantity": "329000",
    "News": "50",
    "Side": "S",
    "Description": "Adobe",
    "Price": "118.41"
}

test_6 = {
    "Symbol": "ADBE",
    "OrderID": "006",
    "Action": "A",
    "Exchange": "1",
    "Quantity": "129000",
    "News": "100",
    "Side": "S",
    "Description": "Adobe",
    "Price": "110.41"
}

strategy_1 = Strategy()
strategy_1.store_signal(test_4)
#print(strategy_1.signal_table)
strategy_1.store_signal(test_5)
#print(strategy_1.signal_table)
strategy_1.store_signal(test_6)
#print(strategy_1.signal_table)
strategy_1.store_signal(test_4)
#print(strategy_1.signal_table)

test_7 = {
    "Symbol": "ADBE",
    "OrderID": "007",
    "Action": "A",
    "Exchange": "1",
    "Quantity": "329000",
    "News": "50",
    "Side": "S",
    "Description": "Adobe",
    "Price": "118.41"
}
test_8 = {
    "Symbol": "ADBE",
    "OrderID": "008",
    "Action": "A",
    "Exchange": "1",
    "Quantity": "329000",
    "News": "0",
    "Side": "S",
    "Description": "Adobe",
    "Price": "119.41"
}
order_book_1.add(test_8)
#print(len(Orderbook.all['ADBE']['S']))
strategy_2 = Strategy()
strategy_2.store_price(test_7, order_book_1.book)
test_9 = {
    "Symbol": "ADBE",
    "OrderID": "009",
    "Action": "A",
    "Exchange": "1",
    "Quantity": "329000",
    "News": "0",
    "Side": "B",
    "Description": "Adobe",
    "Price": "115.41"
}
test_10 = {
    "Symbol": "ADBE",
    "OrderID": "010",
    "Action": "A",
    "Exchange": "1",
    "Quantity": "329000",
    "News": "100",
    "Side": "B",
    "Description": "Adobe",
    "Price": "116.41"
}
order_book_1.add(test_9)
strategy_2.store_price(test_10, order_book_1.book)
#print(Orderbook.all)
#print(len(Orderbook.all['ADBE']['B']))
#print(strategy_2.previous_orders_lowest)
#print(strategy_2.previous_orders_highest)
test_11 = {
    "Symbol": "ADBE",
    "OrderID": "011",
    "Action": "A",
    "Exchange": "3",
    "Quantity": "250000",
    "News": "0",
    "Side": "S",
    "Description": "Adobe",
    "Price": "116.50"
}
test_12 = {
    "Symbol": "ADBE",
    "OrderID": "012",
    "Action": "A",
    "Exchange": "1",
    "Quantity": "329000",
    "News": "100",
    "Side": "B",
    "Description": "Adobe",
    "Price": "116.41"
}
test_13 = {
    "Symbol": "ADBE",
    "OrderID": "013",
    "Action": "A",
    "Exchange": "1",
    "Quantity": "429000",
    "News": "0",
    "Side": "B",
    "Description": "Adobe",
    "Price": "120.41"
}

order_book_1.add(test_11)
order_book_1.add(test_12)
strategy_2.store_signal(test_12)
strategy_2.store_price(test_12, order_book_1.book)
#print(Orderbook.all)
assert len(order_book_1.book['ADBE']['B']) == 3
assert len(order_book_1.book['ADBE']['S']) == 3
assert (strategy_2.previous_orders_highest['ADBE']) == '116.41'
assert (strategy_2.previous_orders_lowest['ADBE']) == '116.50'
execution_order_1 = OrderManager()
execution_order_1.trade_after_news(test_13, strategy_2)
#OrderManager_2 = OrderManager()
#print(execution_order_1.execute_order_100)
#print(execution_order_1.hedge_order_100)

# test that news = 50 works for execute_order()

#print(Orderbook.all)
#print(len(Orderbook.all['ADBE']['B']))
#print(len(Orderbook.all['ADBE']['S']))

test_14 = {
    "Symbol": "ADBE",
    "OrderID": "014",
    "Action": "A",
    "Exchange": "3",
    "Quantity": "329000",
    "News": "50",
    "Side": "B",
    "Description": "Adobe",
    "Price": "116.42"
}
test_15 = {
    "Symbol": "ADBE",
    "OrderID": "015",
    "Action": "A",
    "Exchange": "3",
    "Quantity": "150000",
    "News": "0",
    "Side": "S",
    "Description": "Adobe",
    "Price": "113.10"
}
strategy_3 = Strategy()
order_book_1.add(test_14)
strategy_3.store_signal(test_14)
strategy_3.store_price(test_14, order_book_1.book)
order_book_1.add(test_15)
execution_order_1.trade_after_news(test_15, strategy_3)
#OrderManager_2 = OrderManager()
assert execution_order_1.execute_order_50['Side'] == 'B'
assert execution_order_1.execute_order_50['Price'] == '113.10'
assert execution_order_1.execute_order_50['Quantity'] == '150000'
#print(type(execution_order_1.hedge_order_50))
assert execution_order_1.hedge_order_50['Side'] == 'S'
assert execution_order_1.hedge_order_50['Price'] == '116.42'
assert execution_order_1.hedge_order_50['Quantity'] == '150000'
#print(type(execution_order_1.self.hedge_order_50))

#print(Orderbook.all)
#print(len(Orderbook.all['ADBE']['B']))
#print(len(Orderbook.all['ADBE']['S']))

# Adding test_16 a modify for test_14, running it through all the methods
# modify, store_price, trade_after_news, store_signal

test_16 = {
    "Symbol": "ADBE",
    "OrderID": "014",
    "Action": "M",
    "Exchange": "3",
    "Quantity": "219000",
    "News": "0",
    "Side": "B",
    "Description": "Adobe",
    "Price": "114.43"
}

order_book_1.modify(test_16)
strategy_3.store_price(test_16, order_book_1.book)
#print(strategy_3.previous_orders_lowest )
#print(strategy_3.previous_orders_highest )
execution_order_1.trade_after_news(test_16, strategy_3)
#print(execution_order_1.execute_order_50)
#print(execution_order_1.hedge_order_50)
strategy_3.store_signal(test_16)
assert strategy_3.signal_table['ADBE'] == '0'

##reseting order_15 to a higher price
test_17 = {
    "Symbol": "ADBE",
    "OrderID": "015",
    "Action": "M",
    "Exchange": "3",
    "Quantity": "150000",
    "News": "0",
    "Side": "S",
    "Description": "Adobe",
    "Price": "118.10"
}
order_book_1.modify(test_17)
###Testing:
# submit an order with news, 100
# submit a differnet stock,  add AAL
# submit an order to be executed against, high bid
# book is 4x4, best bid offer is 116.42/116.50

# print(strategy_3.previous_orders_lowest )
# print(strategy_3.previous_orders_highest )
# print(order_book_1.book)
# print(len(order_book_1.book['ADBE']['B']))
# print(len(order_book_1.book['ADBE']['S']))

test_17 = {
    "Symbol": "ADBE",
    "OrderID": "017",
    "Action": "A",
    "Exchange": "1",
    "Quantity": "555555",
    "News": "100",
    "Side": "B",
    "Description": "Adobe",
    "Price": "116.45"
}
order_book_1.add(test_17)
# print(len(order_book_1.book['ADBE']['B']))
# print(len(order_book_1.book['ADBE']['S']))
strategy_3.store_price(test_17, order_book_1.book)
# print(strategy_3.previous_orders_lowest )
# print(strategy_3.previous_orders_highest )
execution_order_1.trade_after_news(test_17, strategy_3)
#print(execution_order_1.execute_order_50)
#print(execution_order_1.hedge_order_50)
strategy_3.store_signal(test_17)
assert strategy_3.signal_table['ADBE'] == '100'

test_18 = {
    "Symbol": "AAL",
    "OrderID": "018",
    "Action": "A",
    "Exchange": "3",
    "Quantity": "300000",
    "News": "0",
    "Side": "S",
    "Description": "Adobe",
    "Price": "50.10"
}

order_book_1.add(test_18)
# print(len(order_book_1.book['AAL']['B']))
# print(len(order_book_1.book['AAL']['S']))
#strategy_3.store_price(test_18, order_book_1.book)
#print(strategy_3.previous_orders_lowest )
#print(strategy_3.previous_orders_highest )
execution_order_1.trade_after_news(test_18, strategy_3)
# print(execution_order_1.execute_order_100)
# print(execution_order_1.hedge_order_100)
strategy_3.store_signal(test_18)
assert strategy_3.signal_table['AAL'] == '0'
#print(strategy_3.signal_table)


test_19 = {
    "Symbol": "ADBE",
    "OrderID": "019",
    "Action": "A",
    "Exchange": "1",
    "Quantity": "180000",
    "News": "0",
    "Side": "B",
    "Description": "Adobe",
    "Price": "118.14"
}
order_book_1.add(test_19)
# print(len(order_book_1.book['ADBE']['B']))
# print(len(order_book_1.book['ADBE']['S']))
strategy_3.store_price(test_19, order_book_1.book)
# print(strategy_3.previous_orders_lowest )
# print(strategy_3.previous_orders_highest )
execution_order_1.trade_after_news(test_19, strategy_3)
#print(execution_order_1.execute_order_100)
#print(execution_order_1.hedge_order_100)
strategy_3.store_signal(test_19)
assert strategy_3.signal_table['ADBE'] == '0'

### Testing Send an AAL order with news 100
### Send an AAL order to execute against  high bid to sell

# print(strategy_3.previous_orders_lowest )
# print(strategy_3.previous_orders_highest )
# print(order_book_1.book)
# print(len(order_book_1.book['AAL']['B']))
# print(len(order_book_1.book['AAL']['S']))

# AAL book is 0X1, no best bid/offer

test_20 = {
    "Symbol": "AAL",
    "OrderID": "020",
    "Action": "A",
    "Exchange": "2",
    "Quantity": "150000",
    "News": "100",
    "Side": "B",
    "Description": "Adobe",
    "Price": "49.50"
}
order_book_1.add(test_20)
# print(len(order_book_1.book['AAL']['B']))
# print(len(order_book_1.book['AAL']['S']))
strategy_3.store_price(test_20, order_book_1.book)
# print(strategy_3.previous_orders_lowest )
# print(strategy_3.previous_orders_highest )
execution_order_1.trade_after_news(test_20, strategy_3)
# print(execution_order_1.execute_order_100)
# print(execution_order_1.hedge_order_100)
strategy_3.store_signal(test_20)
assert strategy_3.signal_table['AAL'] == '100'

test_21 = {
    "Symbol": "AAL",
    "OrderID": "020",
    "Action": "M",
    "Exchange": "2",
    "Quantity": "305000",
    "News": "0",
    "Side": "B",
    "Description": "Adobe",
    "Price": "53.28"
}
order_book_1.modify(test_21)
# print(len(order_book_1.book['AAL']['B']))
# print(len(order_book_1.book['AAL']['S']))
strategy_3.store_price(test_21, order_book_1.book)
# print(strategy_3.previous_orders_lowest )
# print(strategy_3.previous_orders_highest )
execution_order_1.trade_after_news(test_21, strategy_3)
# print(execution_order_1.execute_order_100)
# print(execution_order_1.hedge_order_100)
strategy_3.store_signal(test_21)
assert strategy_3.signal_table['AAL'] == '0'


### Testing
# Send an ADBE order with news 100
# Send an AAL order with news 100
# Send an ADBE order to execute against...high bid to sell
# Send an AAL order to execute against...high bid to sell


# print(strategy_3.previous_orders_lowest )
# print(strategy_3.previous_orders_highest )
# print(order_book_1.book)
# print(len(order_book_1.book['ADBE']['B']))
# print(len(order_book_1.book['ADBE']['S']))
# AAL book is 1X1, 49.5/50.10
# ADBE book is 6X4, 116.45/50

test_22 = {
    "Symbol": "ADBE",
    "OrderID": "019",
    "Action": "M",
    "Exchange": "3",
    "Quantity": "275000",
    "News": "100",
    "Side": "B",
    "Description": "Adobe",
    "Price": "116.39"
}
order_book_1.modify(test_22)
# print(len(order_book_1.book['ADBE']['B']))
# print(len(order_book_1.book['ADBE']['S']))
strategy_3.store_price(test_22, order_book_1.book)
# print(strategy_3.previous_orders_lowest )
# print(strategy_3.previous_orders_highest )
execution_order_1.trade_after_news(test_22, strategy_3)
# print(execution_order_1.execute_order_100)
# print(execution_order_1.hedge_order_100)
strategy_3.store_signal(test_22)
assert strategy_3.signal_table['ADBE'] == '100'

test_23 = {
    "Symbol": "AAL",
    "OrderID": "020",
    "Action": "M",
    "Exchange": "2",
    "Quantity": "187000",
    "News": "100",
    "Side": "B",
    "Description": "American Airlines",
    "Price": "49.66"
}
order_book_1.modify(test_23)
# print(len(order_book_1.book['AAL']['B']))
# print(len(order_book_1.book['AAL']['S']))
strategy_3.store_price(test_23, order_book_1.book)
# print(strategy_3.previous_orders_lowest )
# print(strategy_3.previous_orders_highest )
execution_order_1.trade_after_news(test_23, strategy_3)
# print(execution_order_1.execute_order_100)
# print(execution_order_1.hedge_order_100)
strategy_3.store_signal(test_23)
assert strategy_3.signal_table['AAL'] == '100'

test_24 = {
    "Symbol": "ADBE",
    "OrderID": "024",
    "Action": "A",
    "Exchange": "1",
    "Quantity": "278000",
    "News": "0",
    "Side": "B",
    "Description": "Adobe",
    "Price": "119.19"
}
order_book_1.add(test_24)
# print(len(order_book_1.book['ADBE']['B']))
# print(len(order_book_1.book['ADBE']['S']))
strategy_3.store_price(test_24, order_book_1.book)
# print(strategy_3.previous_orders_lowest )
# print(strategy_3.previous_orders_highest )
execution_order_1.trade_after_news(test_24, strategy_3)
# print(execution_order_1.execute_order_100)
# print(execution_order_1.hedge_order_100)
strategy_3.store_signal(test_24)
assert strategy_3.signal_table['ADBE'] == '0'

test_25 = {
    "Symbol": "AAL",
    "OrderID": "025",
    "Action": "A",
    "Exchange": "2",
    "Quantity": "222000",
    "News": "0",
    "Side": "B",
    "Description": "American Airlines",
    "Price": "54.87"
}
order_book_1.add(test_25)
# print(len(order_book_1.book['AAL']['B']))
# print(len(order_book_1.book['AAL']['S']))
strategy_3.store_price(test_25, order_book_1.book)
# print(strategy_3.previous_orders_lowest )
# print(strategy_3.previous_orders_highest )
execution_order_1.trade_after_news(test_25, strategy_3)
# print(execution_order_1.execute_order_100)
# print(execution_order_1.hedge_order_100)
strategy_3.store_signal(test_25)
assert strategy_3.signal_table['AAL'] == '0'
#returns high bid back into the book
test_26 = {
    "Symbol": "ADBE",
    "OrderID": "024",
    "Action": "A",
    "Exchange": "1",
    "Quantity": "278000",
    "News": "0",
    "Side": "B",
    "Description": "Adobe",
    "Price": "112.19"
}
order_book_1.modify(test_26)
# returns high bid back into the book
test_27 = {
    "Symbol": "AAL",
    "OrderID": "025",
    "Action": "M",
    "Exchange": "2",
    "Quantity": "222000",
    "News": "0",
    "Side": "B",
    "Description": "American Airlines",
    "Price": "48.47"
}

order_book_1.modify(test_27)

#### Want to test, sending an add order w/ no news, for a new symbol
### Does it store any price or news values

test_28 = {
    "Symbol": "HD",
    "OrderID": "028",
    "Action": "A",
    "Exchange": "1",
    "Quantity": "282000",
    "News": "50",
    "Side": "S",
    "Description": "Home Depot",
    "Price": "63.00"
}
test_29 = {
    "Symbol": "HD",
    "OrderID": "029",
    "Action": "A",
    "Exchange": "1",
    "Quantity": "282000",
    "News": "50",
    "Side": "B",
    "Description": "Home Depot",
    "Price": "62.00"
}
client_1 = ClientConnection(order_book_1, execution_order_1, strategy_3)
client_1.tcp_client.connect((client_1.host_ip, client_1.server_port))
order_book_1.add(test_28)
order_book_1.add(test_29)
symbol = test_29['Symbol']
side = test_29['Side']
execution_order_1.execute_order_50.clear()
execution_order_1.hedge_order_50.clear()
if len(order_book_1.book[symbol]['B']) > 0 and len(order_book_1.book[symbol]['S'])> 0:
    #print("bids and offers in the book")
    strategy_3.store_price(test_29, order_book_1.book)
    #print(strategy_3.previous_orders_lowest, strategy_3.previous_orders_highest)
    execution_order_1.trade_after_news(test_29, strategy_3)
    #print(execution_order_1.execute_order_50)
    #print(execution_order_1.hedge_order_50)
 #   client_1.send(test_29)
else:
    print('no trade')

strategy_3.store_signal(test_29)
#print(strategy_3.signal_table['HD'])

test_30 = {
    "Symbol": "HD",
    "OrderID": "030",
    "Action": "A",
    "Exchange": "3",
    "Quantity": "347500",
    "News": "0",
    "Side": "S",
    "Description": "Home Depot",
    "Price": "59.00"
}
client_1 = ClientConnection(order_book_1, execution_order_1, strategy_3)
client_1.tcp_client.connect((client_1.host_ip, client_1.server_port))
order_book_1.add(test_30)

symbol = test_30['Symbol']
#side = test_29['Side']
#execution_order_1.execute_order_50.clear()
#execution_order_1.hedge_order_50.clear()
if len(order_book_1.book[symbol]['B']) > 0 and len(order_book_1.book[symbol]['S'])> 0:
    print("bids and offers in the book")
    strategy_3.store_price(test_30, order_book_1.book)
    print(strategy_3.previous_orders_lowest, strategy_3.previous_orders_highest)
    execution_order_1.trade_after_news(test_30, strategy_3)
    print(execution_order_1.execute_order_50)
    print(execution_order_1.hedge_order_50)
  #  client_1.send(test_30)
else:
    print('no trade')

strategy_3.store_signal(test_30)
print(strategy_3.signal_table['HD'])


print('*****************************************')

test_31 = {
    "Symbol": "CSCO",
    "OrderID": "031",
    "Action": "A",
    "Exchange": "3",
    "Quantity": "347500",
    "News": "0",
    "Side": "S",
    "Description": "Cisco",
    "Price": "180.00"
}
client_1 = ClientConnection(order_book_1, execution_order_1, strategy_3)
client_1.tcp_client.connect((client_1.host_ip, client_1.server_port))
order_book_1.add(test_31)
#print(order_book_1.book[test_31['Symbol']])
test_32 = {
    "Symbol": "CSCO",
    "OrderID": "032",
    "Action": "A",
    "Exchange": "1",
    "Quantity": "175500",
    "News": "0",
    "Side": "B",
    "Description": "Cisco",
    "Price": "179.00"
}
order_book_1.add(test_32)
print(order_book_1.book[test_32['Symbol']])
if len(order_book_1.book[symbol]['B']) > 0 and len(order_book_1.book[symbol]['S'])> 0:
    print("bids and offers in the book")
    strategy_3.store_price(test_32, order_book_1.book)
    print('best bids/offers', strategy_3.previous_orders_lowest, strategy_3.previous_orders_highest)
    outcome=execution_order_1.trade_after_news(test_32, strategy_3)

#testing changing the price of an order

test_33 = {
    "Symbol": "CSCO",
    "OrderID": "032",
    "Action": "A",
    "Exchange": "1",
    "Quantity": "175500",
    "News": "0",
    "Side": "B",
    "Description": "Cisco",
    "Price": "179.05"
}
# order_book_1.clear_crossed_book(test_33, strategy_3)
test_33['Price'] == str(float(test_33['Price']) + 10)
print(str(float(test_33['Price']) + 10))
print(test_33['Price'])
print("test")
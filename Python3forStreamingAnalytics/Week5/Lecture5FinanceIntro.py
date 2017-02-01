# send strings over the network. how do you send an object(class/function)?
# need to convert to something that can be sent
# use a dictionary built in python __dict() whihc converts a =A() into a dictionary
# converts to a string and send it over the network
# when it is recvd, need to rebuild the string into an object

# marshalling is giving you a class, not a dictionary. then unmarshall
# disadvantage is size, also not very portable
# Pickle, solves some of the problems, but its slow

# JSON,
import json
#import literal
import ast

class orderbook:
    def __init__(self):
        self.length=20
        self.bestOffer=10
        self.bestBid=11

a = orderbook()
s = a.__dict__
print(s)

#ast.literal_eval(s)

#Marshalling/Pickle

import marshal
# marshal cannot serialize classes, just dictionaries/lists
import pickle

s = marshal.dumps(a.__dict__)
print(s)

b = marshal.loads(s) # returns a dictionary
print(b)

#pickle
s = pickle.dumps(a) # dumps converts object into a string
print(s)

b = pickle.loads(s) # loads converts string to dictionary/object
print(b) # type is a class

# jJSON

import json

a = orderbook()
s = json.dumps(a.__dict__)
print(s)

b=json.loads(s)
print(b)

# Financial systems

#UDP/TCP, UDP is fast but unreliable, the information doesn't stay in order

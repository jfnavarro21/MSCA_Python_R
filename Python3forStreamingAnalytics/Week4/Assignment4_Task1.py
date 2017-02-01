# Task 1: A little big of networking
# Create a TCP server

import socketserver # diff in p2.7
import numpy as np
from time import sleep
import socket
import statistics
import threading

class Handler_TCPServer(socketserver.BaseRequestHandler):
    def handle(self):
        try:
            mu, sigma = 1, 0.1
            s = np.random.normal(mu, sigma, 10)
            for i in s:
                self.request.sendall((str(i) + ' ').encode())
                sleep(1)
        except:
            pass

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999
    tcp_server = socketserver.TCPServer((HOST, PORT), Handler_TCPServer)
    tcp_server.serve_forever()

# In command prompt enter    telnet 127.0.0.1 9999
# Output from Client(command prompt)
#    1.00094400388 0.895617696392 1.09301557998 1.10805728882 0.955695804086
#    0.986706074736 1.06383527808 0928869628808 1.02471673176
#    Connection to host lost.








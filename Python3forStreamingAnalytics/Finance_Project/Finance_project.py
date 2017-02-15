##  make client, json dumps/loads. client contains the model, execute orders against ones in the book
#client, connect 9995, for loop (true), read data (recv) JSON loads, take string convert to object.  sendall dumps


# Task 0: Learn how to connect to rcc

import socket
import json

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
            if len(data)==5:
                break
    # closes the connection and prints the list
    finally:
        tcp_client.close()
        print(data)

# calls work_with_server function
work_with_server()
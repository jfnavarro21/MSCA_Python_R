# Task 2: Create a TCP client

import statistics as st
import socket
# set host and port, create data as an empty list
host_ip, server_port = "127.0.0.1", 9999
data =[]

# function to create a client
def work_with_server():
    global data
    global res_mean
    global res_stdev
    # creates tcp_client as a socket object
    tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # connects using host and port
        tcp_client.connect((host_ip, server_port))
        while True:
            # stores recieved data in variable received
            received = tcp_client.recv(1024)
            # will break loop if data stops
            if not received:
                break
            # appends received as a float into the list data
            data.append(float(received))

    # closes the connection and prints the list
    finally:
        tcp_client.close()
        print(data)

# calls work_with_server function, print the mean and standard deviation of the list data
work_with_server()
print(st.mean(data))
print(st.stdev(data))


#Output:

# C:\Users\JohntheGreat\Anaconda3\python.exe C:/Users/JohntheGreat/Documents/MSCA/Python3forStreamingAnalytics/Week4/Assignment4_Task2.py
# [1.01641677, 0.915754791165, 0.759171955394, 0.949588610492, 0.939346036072, 1.12396555513, 1.08119365413, 0.900009853287, 0.965018654557, 1.05002770126]
# 0.9700493581487
# 0.10450894585239735
#
# Process finished with exit code 0


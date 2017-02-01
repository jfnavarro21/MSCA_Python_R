# Task 3: Create threaded TCP clients

import threading
import statistics as st
import socket
# set the tuple for host and port
host_ip, server_port = "127.0.0.1", 9999
# create empty lists for res_mean, res_stdev and thread_list
res_mean=[]
res_stdev=[]
thread_list=[]
# create subclass TcpClient of parent class threading.Thread
class TcpClient(threading.Thread):
    def __init__(self, offset):
        threading.Thread.__init__(self)
        self.offset=offset  # int between 0 and 5

    # This is my function from task #2
    def work_with_server(self):
       #create empty list,  set tcp_client as socket object
       data = []
       global res_mean
       global res_stdev
       tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

       # This will store the recieved data in variable received
       try:
           tcp_client.connect((host_ip, server_port))
           while True:
               received = tcp_client.recv(1024)
               #it will break when the information stops
               if not received:
                   break
               # this appends received as a float into data list
               data.append(float(received))

       finally:
           # takes the mean of data and appends into res_mean
           res_mean.append(st.mean(data))
           # takes the standard deviation of data and appends into res_stdev
           res_stdev.append(st.stdev(data))
           # ends the connection
           tcp_client.close()
           print(data)

       return data


    def run(self):
        self.work_with_server()

# Set number of threads to 5
thread_number = 5

# calls the function for each thread, appends into thread_list
for i in range(0,thread_number):
    thread_list.append(TcpClient(i))

# starts the threads
for i in range(0, thread_number):
    thread_list[i].start()

# makes the threads wait
for i in range(0, thread_number):
    thread_list[i].join()

# shows that res_mean has 5 means from each thread
print(res_mean)
# print the mean of res_mean and the mean of res_stdev
print(st.mean(res_mean))
print(st.mean(res_stdev))

# Output:
# C:\Users\JohntheGreat\Anaconda3\python.exe C:/Users/JohntheGreat/Documents/MSCA/Python3forStreamingAnalytics/Week4/Assignment4_Task3.py
#
# [0.9962661781696, 0.9860156937055999, 0.9893152328904, 0.9647682937555, 1.0038831954592]
# 0.98804971879606
# 0.10806280301072893
#
# Process finished with exit code 0
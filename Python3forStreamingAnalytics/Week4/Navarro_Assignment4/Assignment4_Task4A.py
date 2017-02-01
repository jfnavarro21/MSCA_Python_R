 # Task 4: Introdcution to web scraping

import socket
# will be used to get the byte data from the site stackoverflow.com
request = b"GET / HTTP/1.1\nHost: stackoverflow.com\n\n"
# create a socket object: s
s =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#connects the socket to the site
s.connect(("stackoverflow.com", 80))
# sends the request for the data
s.send(request)
# set tally count to 0
tally = 0

# while loop, stores the data received into result
while True:
    result = s.recv(512)
    # use count function on hyperlinks and aggregates each time into tally
    tally += result.count(b'http')
    # will break the loop
    if len(result) < 1:
         break
    # returns the tally count each time, final number is the final number of hyperlinks on the page
    print(tally)

# Outcome:
# final line is 89


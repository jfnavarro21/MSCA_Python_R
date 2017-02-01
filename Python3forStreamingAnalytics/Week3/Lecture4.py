#locks
#critical section
# if you dont have lock, code will be hanging until lock is released
#slides 27-29 session 3

#needs 2 resources, T1 get A, T2 is waiting for A, T3 got B, but they
#need the other ones, and they got stuck w the wrong ones. deadlock

#locks are very limited, dont use in real programming, consumes CPU for nothing

#semaphore is like a lock, but you have a number of keys you can take
# semaphore(2) 2 keys T1 gets 1 key , T2 gets another key, T3 cannot get
#any bc the resource is two

#Daemon is a process, that you can set free from the terminal
#slide 36, set free, the thread will work




#Inter Process communication
#Threads share data, processes do not
#but you can use a pipe to share data
#how do processes share? Socket, pipe, namedpipe, files, share memory, signal(interruption)
#pipe is unidirectional, sockets bi directional
#socket is slow, shared memory is fast, but socket has a lot of applications
#loopback, talks to the same machine, local host
#shared memory stays at OS layer. Software, operating systerm, drivers, network

#OSI model, 7 layers
#telnet connects to TCP server,
#TCP protocol initiates communication w A and B witha  fixed path
 # always up

 #UDP communicate without being connected. datagram
 # SMTP is the port (server to send email25 or 993)
 #FTP is another port 22 SSH, different port - diff services
 # 80 http (web) this port communicates with a server. entrance is a socket
 #telnet 127.0.0.1 4444 loopback
 #or use telnet localhost 4444


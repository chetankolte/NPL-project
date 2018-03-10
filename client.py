import socket

s=socket.socket()
host=socket.gethostname()
port=6667

s.connect((host,port))
print s.recv(1024)
b=raw_input("Your Name : ")
s.send(b)
em=raw_input("Your Email : ")
s.send(em)
print s.recv(1024)
a=int(input("Option : "))
print('Thank You for your vote :)')
print('You chose',a)
a=str(a)
s.send(a)
s.close

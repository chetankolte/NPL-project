import socket

s=socket.socket()
host=socket.gethostname()
port=6667
s.bind((host,port))

s.listen(5)
while True:
	c, addr=s.accept()
	print 'Got connection from', addr
	c.send('Thank You for connecting')
	name=c.recv(20)
	print name
	email=c.recv(40)
	print email
	c.send('Which is your favourite subject? \n1) NPL\n2) MCC\n3) DDB')
	response=c.recv(1)
	print response
	c.close()
	with open('responses.txt','a') as f:
     		f.write(name)
		f.write(' , ')
		f.write(email)
		f.write(' : ')
		f.write(response)
		f.write(' ,\n')
		response=int(response)
		if response==1:
			with open('countNPL.txt','r') as m:
				h=m.readline(10)
				oponecount=int(h)+1
				m.close()
			with open('countNPL.txt','w') as g:
				oponecount=str(oponecount)
				g.write(oponecount)
				g.close()
		elif response==2:
			with open('countMCC.txt','r') as n:
				j=n.readline(10)
				optwocount=int(j)+1
				n.close()
			with open('countMCC.txt','w') as i:
				optwocount=str(optwocount)
				i.write(optwocount)
				i.close()
		else:
			with open('countDDB.txt','r') as o:
				l=o.readline(10)
				opthreecount=int(l)+1
				o.close()
			with open('countDDB.txt','w') as k:
				opthreecount=str(opthreecount)
				k.write(opthreecount)
				k.close()
	file_oponecount=open('countNPL.txt','r')
	file_optwocount=open('countMCC.txt','r')
	file_opthreecount=open('countDDB.txt','r')
	print 'Number of NPL lovers: ',file_oponecount.read()
	print 'Number of MCC lovers: ',file_optwocount.read()
	print 'Number of DDB lovers: ',file_opthreecount.read()

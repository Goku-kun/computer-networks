import socket
import  select
import sys

def getACK(ack,Client_socket,i_s,number):
	while not ack:
		msg ="packet :"+str(number)
		Client_socket.send(msg.encode("utf-8"))
		r = select.select(i_s,[],[],5)
		if r[0]:
			Client_socket.recv(1024).decode("utf-8")
			ack = True;
			print("GOT ack packet " + str(number))
			number += 1
	return True,number
			


server_socket = socket.socket()
server_socket.bind(('',12345))
server_socket.listen(1)
Client_socket , address = server_socket.accept()
print(address)
number = 1
ack = False
i_s = [Client_socket,sys.stdin]

while True:
	ack,number = getACK(False,Client_socket,i_s,number)
	
	

 

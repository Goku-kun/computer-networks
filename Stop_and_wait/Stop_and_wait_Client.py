import socket
import sys
import select

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect(('',12345))

while True:
    
    while True:
	Input_Stream = [client_socket,sys.stdin]
   	r,w,e= select.select(Input_Stream,[],[])
        for soc in r:
		if soc == client_socket:
		    msg = client_socket.recv(1024).decode('utf-8')
		    print(msg)
		if soc == sys.stdin:
		    msg = raw_input()
		    client_socket.send(msg.encode('utf-8'))
		if msg == 'bye':
		    input_stream.remove(client_socket)
    if client_socket in input_stream:
	break
client_socket.close()

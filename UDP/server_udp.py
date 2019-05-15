import socket

mysocket=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
mysocket.bind(("",12345))

client, (ip,port)=mysocket.recvfrom(2048)
print("Msg from UDP Client :",client)

mysocket.sendto("Hello, I am UDP Server",(ip,port))

mysocket.close()



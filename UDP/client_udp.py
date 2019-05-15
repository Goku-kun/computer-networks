import socket

mysocket=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
mysocket.connect(("",12345))

mysocket.sendto("This is client",("",12345))

data=mysocket.recvfrom(2048)
print("Msg from server :",data)


mysocket.close()



import socket

mysocket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysocket.connect(("",12345))
print("Connection established")

data=mysocket.recv(2048)
print("Msg from server :",data)

mysocket.send("This is client")

mysocket.close()



import socket

mysocket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysocket.bind(("",12345))
mysocket.listen(5)

client, (ip,port)=mysocket.accept()
print("Client IP: ",ip, " Port: ", port)

client.send("I am server")
data=client.recv(2048)
print("Msg from client :",data)

mysocket.close()



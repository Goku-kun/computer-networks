import socket


# Calculate checksum
def checksum(msg):
  s = 0
  for i in range(0, len(msg), 2):
    w = ord(msg[i]) + (ord(msg[i+1]) << 8 )
    s = s + w
    s = (s>>16) + (s & 0xffff);
    s = s + (s >> 16);
    s = ~s & 0xffff
    return str(s)


# Input
message = raw_input("Enter the message:")
chksm = checksum(message)


# Socket
skt = socket.socket()
port = 12345
skt.bind(('', port))
print("socket binded to %s" %(port))
skt.listen(5)
print("socket is listening")
while True:
   c, addr = skt.accept()
   print('Got connection from ', addr)
   print(message + ' | ' + chksm)
   c.send(message + ' | ' + chksm)
   c.close()

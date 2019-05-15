import socket


# compare the checksums
def check_data(data):
    if data[1].strip()==checksum(data[0].strip()):
        return True
    else:
        return False


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


# Socket
skt = socket.socket()
port = 12345
skt.connect(('10.30.7.121', port))
data = skt.recv(1024)
print('Message recieved:' + data.strip())
chksm = data.split("|")
if check_data(chksm):
    print('Message checked!' + '\nMessage: ' + chksm[0])
else:
    print('Check failed!')
skt.close()

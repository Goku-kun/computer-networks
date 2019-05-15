import socket

mysocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mysocket.connect(('', 5554))


def decodeData(data, key):
    l_key = len(key)
    re = int(data, 2) % int(key, 2)
    remainder = (bin(re))
    if len(remainder[2:]) != 3:
        x = len(remainder[2:])
        remain = '0' * (len(key) - 1 - x) + remainder[2:]
    return remain
  
  
while True: 
    data = mysocket.recv(1024) 
    remain=data.split('|')
    if not data: 
        break
    msg=remain[0]
    new =(''.join(format(ord(x), 'b') for x in msg)) 
    key = "1000"
    new2=new+remain[1]
    print("Data received from Server : ",new2)
    print("CRC generator key: ",key)
    ans = decodeData(new2, key)
    temp = "0" * (len(key) - 1) 
    if ans == temp: 
        mysocket.send("THANK you Data ->"+msg + " Received No error FOUND")
    else: 
        mysocket.send("Error in data") 

mysocket.close() 


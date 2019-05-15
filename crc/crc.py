import socket

mysocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mysocket.bind(('', 5554))
mysocket.listen(5)

def encodeData(data, key):
    l_key = len(key)
    appended_data = data + '0'*(l_key-1)
    re = int(appended_data, 2) % int(key, 2)
    remainder=(bin(re))
    if len(remainder[2:]) != 3:
        x = len(remainder[2:])
        remain = '0' * (len(key) - 1 - x) + remainder[2:]
    return remain

user_input = raw_input("Enter data you want to send->")
data =(''.join(format(ord(x), 'b') for x in user_input)) 
print("Binary form of data to be send : ",data)
key = "1000"
print("CRC generator : 1000")
print("Data send : " (data+remain))
ans=encodeData(data,key)
datanew=user_input+'|'+ans
c,addr=mysocket.accept()
c.send(datanew)
  
c.close() 



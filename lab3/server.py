import socket
import os
s=socket.socket()
print('socket is now created')
s.bind(('localhost',9999))
s.listen(3)
print('waiting for connections')
while True:
    c,addr=s.accept()
    name=c.recv(1024).decode()
    print("connections with",addr,name)
    
    
    
    c.send(bytes('welcome to skyline bro','utf-8'))
    
    #starting for sending file
    
    file=open("cat.webp","rb")
    file_size=os.path.getsize("cat.webp")
    
    c.send("rec_image.webp".encode())
    c.send(str(file_size).encode())
    
    data=file.read()
    
    c.sendall(data)
    c.send(b"<END>")
    file.close()
    
    
    c.close()  
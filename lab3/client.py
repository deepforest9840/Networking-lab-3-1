import socket
from tqdm import tqdm


c=socket.socket()
c.connect(('localhost',9999))
name=" client "
c.send(bytes(name,'utf-8'))

msg=c.recv(1024).decode()
    
print(msg)

file_name=c.recv(1024).decode()

print(file_name)

file_size=c.recv(1024).decode()

print(file_size)

file=open(file_name,"wb")

file_bytes=b""
done=False
progress=tqdm.tqdm(unit="B",unit_scale=True,unit_divisor=1000,total=int(file_size))

while not done:
    data=c.recv(1024)
    if file_bytes[-5:]==b"<END>":
        done=True
        
    else:
        file_bytes+=data
    progress.update(1024)


file.write(file_bytes)
file.close()





import socket

def main():
    client=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_addr=(("localhost",9993))
    domain="cse.du.ac.bd."
    client.sendto(domain.encode(),server_addr)
    msg,_=client.recvfrom(1024)
    print(msg.decode())
    

if __name__ == "__main__":
    main()

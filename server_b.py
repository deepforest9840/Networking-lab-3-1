import  socket
import time
import random

usa='r'
pasa='1'
bala=120000

usb='sakib'
pasb='123'
balb=50000

d={}
serv_sock=socket.socket()
def connection():

    hostn = socket.gethostname()
    host = socket.gethostbyname(hostn)
    port = 4598

    print(host)

    serv_sock.bind(('', port))
    serv_sock.listen(5)
    c, addr = serv_sock.accept()

    print("Connected to: " + str(addr))
    return c

def error_handling():
    total=0
    error=0
    start_time = time.time() * 1000  # Get the start time in milliseconds

    while True:
        random_number = random.randint(1, 10)
        
        if total == 100:
            c.send(str(total).encode())
            break

        if random_number <= 0.0:
            c.send(("error").encode())
            error += 1
        else:
            total += 1
            c.send(("yes ").encode())

    end_time = time.time() * 1000  # Get the end time in milliseconds
    elapsed_time = end_time - start_time

    print( f'time is {elapsed_time} ')
    return elapsed_time



def servertransiction(bala):
    while True:
        opt = c.recv(1024).decode()
        print('choice ', opt)

        if int(opt) == 1:
            count=0
            error_set = set()
            while True:
                count=count+1
                if (count==100):
                    break
                print("Holder wants to know balance")
                a=error_handling()
                error_set.add(int(a))
                c.send(("Your current balance is : " + str(bala)).encode())
            a = max(error_set)
            print(f'error rate is {a}')

        elif int(opt) == 3:
            am = int(c.recv(1024).decode())
            bala = bala + am
            c.send(("After deposing current balance is: " + str(bala)).encode())

        else:
            am = int(c.recv(1024).decode())
            print(am)

            if am <= 0:
                continue

            id = c.recv(1024).decode()

            if d.get(id) is not None:
                print('Error')
                c.send(('555').encode())

            else:
                print("Wtihdrawn amnt: ", am)

                if bala < am:
                    c.send(('401').encode())
                    continue
                else:
                    d[id] = {usa, am}

                    ra = random.randint(0, 50)
                    print(ra)

                    if ra > 50:
                        c.send(('401').encode())
                        continue
                    bala = bala - am
                    c.send(("Withdraw successful!After withdraw your balance is: " + str(bala)).encode())
                    print(d)


def serverdriver(c,bala):
    while True:
        user = c.recv(1024).decode()
        if not user:
            break

        if user == usa:
            pas = c.recv(1024).decode()
            if pas == pasa:
                c.send('40'.encode())

                servertransiction(bala)

            else:
                print("Invalid Password")
                c.send(('404').encode())
                c.close()
        else:
            print('Invalid User')
            c.send(('404').encode())
            c.close()



c=connection()

serverdriver(c,bala)














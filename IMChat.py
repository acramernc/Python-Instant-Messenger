import socket, threading, time

print("Welcome to GCC IM\n")
hostName = socket.gethostname()
myIP = socket.gethostbyname(hostName)
print("Your ip is ", myIP)
port = 25565




def send():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        print("Trying to connect")
        s.connect((otherIP, port))
        time.sleep(.2)
        print("Connection Successful")
        name = input("Please enter your name:")
        kill = False
        while True:
            time.sleep(.2)
            msg = input(name + ": ")
            if msg.lower() == "bye": kill = True
            msg = name + ": " + msg
            msg = msg.encode("utf-8")
            s.sendall(msg)
            if kill: break


def rcv():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as r:
        r.bind(('', port))
        r.listen()
        conn, addr = r.accept()
        with conn:
            print('Connected by', addr)
            while True:
                #data = ""
                data = conn.recv(1024)
                if not data: break
                rmsg = data.decode('utf-8')
                print(rmsg)
            print("The other client has disconnected")


rThread = threading.Thread(target=rcv)
sThread = threading.Thread(target=send)

rThread.start()

otherIP = input("Please enter the target IPv4 address")

sThread.start()



import socket, threading

print("Welcome to GCC IM\n")
otherIP = input("Please enter the target IPv4 address")
port = 25565
alive = True


def send():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((otherIP, port))
        name = input("Please enter your name:")
        while True:
            msg = input(name + ": ")
            msg = name + ": " + msg
            msg = msg.encode("utf-8")
            s.sendall(msg)
            if not alive: break


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
                print(data.decode('utf-8'))


rThread = threading.Thread(target=rcv)
sThread = threading.Thread(target=send)

rThread.start()
sThread.start()

while True:
    alive = rThread.is_alive()

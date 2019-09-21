import socket, threading, re

HOST = ''
PORT = 25565
BYE = re.compile("bye", re.I)

hostname = socket.gethostname()
myIP = socket.gethostbyname(hostname)

print("Welcome to GCC IM!")
print("Your local IP address is " + myIP)
otherIP = input("Please enter the other user's IP address: ")

def receive():
    receiving_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    receiving_socket.bind((HOST,PORT))
    receiving_socket.listen(1)

    conn, addr = receiving_socket.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(4096)
            if len(data):
                rcv_msg = data.decode('utf-8')
                if BYE.search(rcv_msg):
                    print("\n" + rcv_msg)
                    break
                else:
                    print("\n" + rcv_msg)

    print("\nThe other client has ended this conversation.")

def send():
    sending_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        sending_socket.connect((otherIP, PORT))
    except:
        print("\nUnable to connect to that IP address.")

    print("Connection successful!")
    name = input("Please enter your name: ")

    while True:
        msg = input(name + ": ")
        if msg:
            if BYE.search(msg):
                msg = name + ": " + msg
                msg = msg.encode('utf-8')
                sending_socket.sendall(msg)
                break
            else:
                msg = name + ": " + msg
                msg = msg.encode('utf-8')
                sending_socket.sendall(msg)


sending_thread = threading.Thread(target=send, name="sthread")
receiving_thread = threading.Thread(target=receive, name="rthread")

receiving_thread.start()
sending_thread.start()

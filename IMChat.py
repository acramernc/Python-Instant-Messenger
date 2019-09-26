#Group Adam Cramer and Brendan Ortmann

import socket, threading, time, sys

print("Welcome to GCC IM\n")
hostName = socket.gethostname()
myIP = socket.gethostbyname(hostName)
print("Your ip is ", myIP)
port = 25565
alive = True

#BYE = re.compile("bye", re.I)



def send():
    global alive
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            print("Trying to connect on " + str(otherIP) + ":" + str(port) + "...")
            s.connect((otherIP, port))
        except (socket.timeout, socket.gaierror):
            print("\nUnable to connect to that IP address.")
            alive = False
            sys.exit(0)
        #print("Trying to connect")
        #s.connect((otherIP, port))
        time.sleep(.2)
        print("Connection Successful")
        name = input("Please enter your name:")
        #kill = False
        while True:
            time.sleep(.2)
            msg = input(name + ": ")
            if msg.lower() == "bye": alive = False
            msg = name + ": " + msg
            msg = msg.encode("utf-8")
            s.sendall(msg)
            if not alive: break
        return
#            if msg:
 #               if BYE.search(msg):
  #                  msg = name + ": " + msg
   #                 msg = msg.encode('utf-8')
    #                s.sendall(msg)
     #               break
      #          else:
       #             msg = name + ": " + msg
        #            msg = msg.encode('utf-8')
         #           s.sendall(msg)


def rcv():
    global alive
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as r:
        r.bind(('', port))
        r.listen()
        conn, addr = r.accept()
        with conn:
            print('\nConnected by', addr)
            while True:
                #data = ""
                data = conn.recv(1024)
                if not data: break
                rmsg = data.decode('utf-8')
                print("\n" + rmsg)
                if not alive: break
            print("The other client has disconnected")
            alive = False

def dummy():
    while alive:
        time.sleep(.2)

dThread = threading.Thread(target=dummy)
rThread = threading.Thread(target=rcv, daemon = True)
sThread = threading.Thread(target=send, daemon = True)

dThread.start()
rThread.start()

otherIP = input("Please enter the target IPv4 address")

sThread.start()


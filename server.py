import socket as sk
import threading
import sys

clients = []
clientsaddr = []

if len(sys.argv) != 2:
    print("correct usage server.py <port>")
    sys.exit()

host = ""
port = int(sys.argv[1])

socket = sk.socket(sk.AF_INET, sk.SOCK_STREAM)

socket.bind((host, port))
socket.listen()

def broadcast(message, connection):
    for conn1 in clients:
                if conn1 != connection:
                    conn1.send(message)
                else:
                    pass


def mainloop(connection, ip_address):
    while True:
        try:
            message = connection.recv(2048)
            print(message.decode())
        except Exception as e:
            connection.close()
            clients.remove(connection)
            print("[-]{c} disconnected!".format(c = ip_address))
            broadcast("[-]{c} disconnected!".format(c = ip_address).encode(), connection)
            break
        else:
            broadcast(message, connection)
                
while True:
    connection, ip_address = socket.accept()
    print("[+]{a} connected!".format(a = ip_address))
    clients.append(connection)
    clientsaddr.append(ip_address)
    t = threading.Thread(target=mainloop, args=(connection, ip_address,))
    t.daemon = True
    t.start()
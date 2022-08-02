from pydoc import cli
import socket as sk
import threading
import sys

clients = []
clientsaddr = []

if len(sys.argv) != 2:
    print("corect usege server.py <port>")
    sys.exit()

host = ""
port = int(sys.argv[1])

s = sk.socket(sk.AF_INET, sk.SOCK_STREAM)

s.bind((host, port))
s.listen()

def mainloop(conn, addr):
    while True:
        try:
            m = conn.recv(2048)
            print(m.decode())
        except Exception as e:
            conn.close()
            print("[-]{c} disconnected!".format(c = addr))
            break
        else:
            for conn in clients:
                if clientsaddr != addr:
                    conn.send(m)

while True:
    conn, addr = s.accept()
    print("[+]{a} connected!".format(a = addr))
    clients.append(conn)
    clientsaddr.append(addr)
    t = threading.Thread(target=mainloop, args=(conn, addr,))
    t.daemon = True
    t.start()



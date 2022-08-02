import socket as sk
import threading
import sys

if len(sys.argv) != 3:
    print("corect useage client.py <port> <address>")
    sys.exit()

host = sys.argv[2]
port = int(sys.argv[1])

s = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
s.connect((host, port))

print('''
/\/\/\/\/\/\/\/\/\/\/\/\/\/
         CHAT-O
\/\/\/\/\/\/\/\/\/\/\/\/\/\\
''')
name = input("enter your name >")

def res():
    while True:
        m = s.recv(2048).decode()
        print(m)


def send():
    while True:
        ms = input()
        ms = "{n}: {m}".format(n = name, m = ms)
        s.send(ms.encode())

tr = threading.Thread(target=res)
tr.start()

ts = threading.Thread(target=send)
ts.start()
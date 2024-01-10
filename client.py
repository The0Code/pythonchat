import socket as sk
import threading
import sys

#if len(sys.argv) != 3:
#    print("correct usage client.py <port> <address>")
#    sys.exit()



host = input("address>")
port = int(input("port>"))

s = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
s.connect((host, port))

print('''
/\/\/\/\/\/\/\/\/\/\/\/\/\\
|         CHAT-O                 |
\/\/\/\/\/\/\/\/\/\/\/\/\/
''')
name = input("enter your name >")
s.send("{j} loged in".format(j = name).encode())

def res():
    while True:
        try:
            m = s.recv(2048).decode()
            print(m)
        except:
            s.send("{a} > disconnected".format(a = name).encode)


def send():
    while True:
        try:
            ms = input()
            ms = "{n}: {m}".format(n = name, m = ms)
            s.send(ms.encode())
        except:
            s.send("{a} > disconnected".format(a = name).encode)

tr = threading.Thread(target=res)
tr.start()

ts = threading.Thread(target=send)
ts.start()
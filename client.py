import socket as sk
import threading

print('''
 ________________________
/                        \\
|         CHAT-O         |
\\________________________/
''')

host = input("address>")
port = int(input("port>"))

socket = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
socket.connect((host, port))


name = input("enter your name >")
socket.send("{j} loged in".format(j = name).encode())

def receive():
    while True:
        try:
            message = socket.recv(2048).decode()
            print(message)
        except:
            socket.send("{a} > disconnected".format(a = name).encode())


def send():
    while True:
        try:
            message = input()
            message = "{n}: {message}".format(n = name, message = message)
            socket.send(message.encode())
        except:
            socket.send("{a} > disconnected".format(a = name).encode())

receivingthread = threading.Thread(target=receive)
receivingthread.start()

sendingthread = threading.Thread(target=send)
sendingthread.start()
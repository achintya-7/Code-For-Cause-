import socket
import time
port = 3000
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #creates a socket object  
# socket.socket(family, type)
# AF_INET : family or ipv4 ip address 
# SOCK_DGRAM UDP, SOCK_STREAM : TCP

# some ip address that server will listen when message comes
hostname = '127.145.21.122'

n = input("name: ")

server.bind((hostname, port)) #bind the socket with the host machine and on port 3000
chunk = 65555 # recieve at most these amount of data at once
while True:
    data, clientAdd = server.recvfrom(chunk)
    message = data.decode('ascii') #data travels in binary in bytes
    print(f"{n} : {message}")
    message_send = input("message: ")
    data = message_send.encode('ascii') #send data to the ipadress that sent me the data
    server.sendto(data, clientAdd)
    time.sleep(3)
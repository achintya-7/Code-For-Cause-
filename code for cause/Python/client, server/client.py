import socket
port = 3000

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #creates a socket object  
# instead of explicity binding, we will let OS do it
# OS will bind for us

hostname = "127.145.201.122"
chunk = 65555

n = input("name: ")
while True:
    server.connect((hostname, port))
    message = input(f"{n}: ")
    data = message.encode('ascii')
    server.send(data)
    data = server.recv(chunk)
    text = data.decode('ascii')
    print(f"message : {text}")
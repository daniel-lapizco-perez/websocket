import time, socket, sys

new_socket = socket.socket()
host_name = socket.gethostname()
socket_ip = socket.gethostbyname(host_name)

port = 8080

new_socket.bind((host_name, port))
print("binding successfull!")
print("This is your IP: ", socket_ip)

name = input('Enter name: ')

new_socket.listen(1)

conn, addr = new_socket.accept()

print("Received connection from ", addr[0])
print('Connection Established, connected from: ', addr[0])

client = (conn.recv(1024)).decode()
print(client + ' has connected')

conn.send(name.encode())
while True:
    message = input('Me: ')
    conn.send(message.encode())
    message = conn.recv(1024)
    message = message.decode()
    print(client, ":", message)
import socket
import json

# create a object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# define the port on which server is running
port = 80
# host = '0.0.0.0'
# host = '192.168.1.42' # raspberrypi
host = '192.168.1.35'

# connect to the server
s.connect((host, port))

while True:
    message = str(input("enter your message: "))

    # send to server
    data = json.dumps(message)
    s.send(data.encode())

    # receive data from server
    print(s.recv(4096).decode())

# close the connection
s.close()

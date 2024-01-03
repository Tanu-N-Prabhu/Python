# an example script to connect to google by scoket
import socket
import sys

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket sucessfully created")
except socket.error as err:
    print("socket error" + err)

# default port for socket
port = 80

try:
    host_ip = socket.gethostbyname('www.google.com')
except socket.gaierror:
    print("there was an error resolving the host")
    sys.exit()

# connect to the server
s.connect((host_ip, port))

print("the socket was connected sucessfully to google \
    on port == %s" % (host_ip))

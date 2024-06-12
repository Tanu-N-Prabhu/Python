import socket

# server socket
serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port = 80
# binding to start server
# host = '0.0.0.0'
host = '192.168.1.35'
serv.bind((host, port))
serv.listen(5)

print("Server started and listing for client connections on port %s" % port)

# true for indefinite
while True:
    conn, addr = serv.accept()
    from_client = None

    while True:
        # byte stream 
        data = conn.recv(4096)
        if not data:
            break
        from_client = data.decode()

        response = "welcome " + from_client
        conn.send(response.encode())
        print(from_client)

    conn.close()

    print('client disconnected')

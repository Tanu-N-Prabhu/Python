import socket


def is_port_open(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(5)
    try:
        s.connect((host, port))
        s.shutdown(2)
        return True
    except:
        return False


def scan_ports(host):
    open_ports = []
    for port in range(1, 65535):
        if is_port_open(host, port):
            open_ports.append(port)
    return open_ports


host = input("Enter host to scan: ")
open_ports = scan_ports(host)
print("Open ports:", open_ports)

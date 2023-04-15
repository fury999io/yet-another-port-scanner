import socket
target = input("Enter the target IP address: ")
port_range = input("Enter the port range (start-end): ")
start_port, end_port = map(int, port_range.split('-'))
for port in range(start_port, end_port+1):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((target, port))
    if result == 0:
        print(f"Port {port} is open")
    sock.close()

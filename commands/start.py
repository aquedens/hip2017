import socket
import sys
import json

# Create a UDS socket
sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = '/var/www/html/command_socket'
print('connecting to {}'.format(server_address))
try:
    sock.connect(server_address)
except socket.error as msg:
    print(msg)
    sys.exit(1)

try:
    command = {'command': 'start'}
    encoded_command = json.dumps(command).encode('utf-8')
    
    sock.sendall(encoded_command)
finally:
    print('closing socket')
    sock.close()

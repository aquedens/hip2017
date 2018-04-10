import socket
import sys
import os
import json
from time import sleep
import pigpio

server_address = '/var/www/html/command_socket'

# Make sure the socket does not already exist
try:
    os.unlink(server_address)
except OSError:
    if os.path.exists(server_address):
        raise

# Create a UDS socket
sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

# Bind the socket to the address
print('starting up on {}'.format(server_address))
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    #print('waiting for a connection')
    connection, client_address = sock.accept()
    try:
        #print('connection from', client_address)

        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(1024)
            if data:
                print('received {!r}'.format(data))
                decodedData = json.loads(data.decode('utf-8'))
                command = decodedData['command']
                
                if command == 'left':
                    print('go left')
                elif command == 'right':
                    print('go right')
                elif command == 'forward':
                    print('go forward')
                elif command == 'backward':
                    print('go backward')
                elif command == 'speed':
                    speed = decodedData['value']
                    print('set speed to %s' % speed)
                else:
                    print('invalid command')
                #connection.sendall(data)
            else:
                #print('no data from', client_address)
                break

    finally:
        # Clean up the connection
        connection.close()

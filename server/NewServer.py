import socket
import sys
import os
import json
from time import sleep
import pigpio

DIR = 20     # Direction GPIO Pin
STEP = 21    # Step GPIO Pin
SWITCH = 16  # GPIO pin of switch

# Connect to pigpiod daemon
pi = pigpio.pi()

# Set up pins as an output
pi.set_mode(DIR, pigpio.OUTPUT)
pi.set_mode(STEP, pigpio.OUTPUT)

# Set up input switch
pi.set_mode(SWITCH, pigpio.INPUT)
pi.set_pull_up_down(SWITCH, pigpio.PUD_UP)

MODE = (14, 15, 18)   # Microstep Resolution GPIO Pins
RESOLUTION = {'Full': (0, 0, 0),
              'Half': (1, 0, 0),
              '1/4': (0, 1, 0),
              '1/8': (1, 1, 0),
              '1/16': (0, 0, 1),
              '1/32': (1, 0, 1)}
for i in range(3):
    pi.write(MODE[i], RESOLUTION['Full'][i])

# Set duty cycle and frequency
pi.set_PWM_dutycycle(STEP, 128)  # PWM 1/2 On 1/2 Off
pi.set_PWM_frequency(STEP, 0)  # 500 pulses per second

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

speeds = [320, 400, 500, 800, 1000, 1600, 2000, 4000, 8000]
speed_index = 0

try:
    while True:
        # Wait for a connection
        #print('waiting for a connection')
        connection, client_address = sock.accept()
        try:
            while True:
                data = connection.recv(1024)
                if data:
                    print('received {!r}'.format(data))
                    decodedData = json.loads(data.decode('utf-8'))
                    command = decodedData['command']
                    
                    if command == 'start':
                        print('start motors')
                        pi.set_PWM_frequency(STEP, speeds[0]) 
                    elif command == 'faster':
                        print('go faster')
                        if speed_index < len(speeds):
                            speed_index = speed_index + 1
                        pi.set_PWM_frequency(STEP, speeds[speed_index]) 
                    elif command == 'slower':
                        print('go slower')
                        if speed_index > 0:
                            speed_index = speed_index - 1
                        pi.set_PWM_frequency(STEP, speeds[speed_index]) 
                    elif command == 'left':
                        print('go left')
                    elif command == 'right':
                        print('go right')
                    elif command == 'reverse':
                        print('reverse')
                        #Set DIR bit the other way
                    else:
                        print('invalid command')

                    #connection.sendall(data)
                else:
                    #print('no data from', client_address)
                    break
        except KeyboardInterrupt:
            print ("\nCtrl-C pressed.  Stopping PIGPIO and exiting...")
            connection.close()
            break
except KeyboardInterrupt:
    print ("\nCtrl-C pressed.  Stopping PIGPIO and exiting...")
finally:
    # Clean up the connection
    pi.set_PWM_dutycycle(STEP, 0)  # PWM off
    pi.stop()

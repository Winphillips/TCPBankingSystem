import struct
import binascii
import sys
import socket

# Create Socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect Socket to the server's IP and port #
client_socket.connect(('localhost', 4753))

while True:
    # MENU
    command = input('Enter command (deposit <amount>, withdraw <amount>, balance, quit): ')

    # Send commands to the server
    client_socket.send(command.encode())

    # Receive server response and print it to the terminal
    response = client_socket.recv(1024)
    print(response.decode())

    # Close if 'quit'; close server for ease of testing, obviously would be removed if real program.
    if command == 'quit' or command =='close server':
        break

# Close the socket and exit the program
client_socket.close()
print("Closed...")
sys.exit()

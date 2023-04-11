import struct
import binascii
import sys
import socket

# Initialize balance to $100
balance = 100

# Create a socket and bind it to a port to listen for incoming connections
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 4753))
server_socket.listen(1)
print('Server listening...')

while True:
    # When a client connects, receive the request from the client
    conn, addr = server_socket.accept()
    print(f'Connected by {addr}')

    while True:
        request = conn.recv(1024)
        if not request:
            break
        
        print('Received request:', request)

        # OPERAATIONS
        request = request.decode()
        # DEPOSIT
        if request.startswith('deposit'):
            amount_str = request.split()[1]
            if not amount_str.isdigit():
                response = 'Invalid deposit amount'
            else:
                amount = int(amount_str)
                if amount <= 0:
                    response = 'Invalid deposit amount'
                else:
                    balance += amount
                    response = f'Deposited ${amount}. New balance: ${balance}'
        # WITHDRAW
        elif request.startswith('withdraw'):
            amount_str = request.split()[1]
            if not amount_str.isdigit():
                response = 'Invalid withdrawal amount'
            else:
                amount = int(amount_str)
                if amount <= 0:
                    response = 'Invalid withdrawal amount'
                elif amount > balance:
                    response = 'Insufficient funds'
                else:
                    balance -= amount
                    response = f'Withdrawn ${amount}. New balance: ${balance}'
        # BALANCE
        elif request == 'balance':
            response = f'Balance: ${balance}'
        # QUIT
        elif request == 'quit':
            break
        #Just for ease of testing to close program to prevent restarting everytime
        elif request == 'close server':
            conn.close()
            response = 'Connection closed...'
            server_socket.close()
            response = 'Server closed...'
        # EDGE CASES
        else:
            response = 'Invalid request'

        # Send the response to the client
        conn.send(response.encode())
        print('Sent response:', response)

    # Close the connection
    print(f'Connection closed by {addr}')
    conn.close()

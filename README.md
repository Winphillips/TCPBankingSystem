# SimpleTCPBankingSystem

A basic implementation of a client-server banking system using TCP sockets in Python.

## Overview

This repository contains a simple banking system implemented using TCP sockets in Python. It consists of two main files: `server.py` and `client.py`. The `server.py` file contains the server-side implementation, while the `client.py` file contains the client-side implementation.

## Functionality

The server listens for incoming connections on a specified port and handles client requests for depositing funds, withdrawing funds, checking balance, and quitting the program. The client communicates with the server by sending commands and receiving responses, allowing users to interact with the banking system via a text-based menu in the terminal.

## Usage

1. Clone the repository to your local machine using `git clone`.
2. Run the `server.py` file on the server-side to start the server.
3. Run the `client.py` file on the client-side to start the client.
4. Enter commands in the client-side terminal to interact with the banking system (e.g., `deposit <amount>`, `withdraw <amount>`, `balance`, `quit`).
5. The server will process the commands and send responses back to the client.
6. To close the program, enter `quit` or `close server` command in the client-side terminal.

## Example
```
Here's an example of how the client interacts with the banking system:

Enter command (deposit <amount>, withdraw <amount>, balance, quit): deposit 50
Received response: Deposited $50. New balance: $150

Enter command (deposit <amount>, withdraw <amount>, balance, quit): balance
Received response: Balance: $150

Enter command (deposit <amount>, withdraw <amount>, balance, quit): withdraw 30
Received response: Withdrawn $30. New balance: $120

Enter command (deposit <amount>, withdraw <amount>, balance, quit): quit
Received response: Connection closed...
```

## Notes

- The `struct`, `binascii`, and `sys` libraries are imported for supporting binary data packing, ASCII conversion, and program termination functionalities, respectively.
- The `socket` library is imported for creating, binding, and connecting sockets for network communication.
- This is a basic example of a banking system and can be used as a starting point for further development or learning about TCP socket communication in Python.

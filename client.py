#!/usr/bin/env python
""" docker_vscoderun - Client
    Connect to the server on the port specified by CONNECT_PORT. On Success,
    sends the filename given by the command line argument to the server to be
    opened there in VSCode.
"""

import os
import sys
import socket

SERVER = '10.0.0.145'   # TCP Server
CONNECT_PORT = 5001     # TCP Listen port
MSG_SIZE = 1024         # TCP Msg Size

print(os.path.dirname(os.path.realpath(__file__)))
exit()

if __name__ == '__main__':
    # Validate single command line arg
    if len(sys.argv) != 2:
        print('Usage: client.py FILENAME')
        exit()
    filename = sys.argv[1]

    # Establish socket connection
    print('Connecting to ' + SERVER + ':' + str(CONNECT_PORT))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((SERVER, CONNECT_PORT))
    print('Connected Successfully.\n')

    # Hanlde user requests
    try:
        sock.send(filename.encode())
    except Exception as e:
        print(e)

    # Cleanup
    sock.close()

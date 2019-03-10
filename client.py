#!/usr/bin/env python
""" docker_vscoderun - Client
    Connect to the server on the port specified by CONNECT_PORT. On Success,
    sends the filename given by the command line argument to the server to be
    opened there in the editor specified by server.py:OPEN_WITH.
"""

import sys
import socket

SERVER = '10.0.0.145'   # TCP Server
CONNECT_PORT = 5001     # TCP Listen port
MSG_SIZE = 1024         # TCP Msg Size

if __name__ == '__main__':
    # Validate single command line arg
    if len(sys.argv) != 2:
        print('Usage: client.py FILENAME')
        exit()
    filename = sys.argv[1]

    # Establish socket connection
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((SERVER, CONNECT_PORT))
    # print('Connected to ' + SERVER + ':' + str(CONNECT_PORT))

    # Hanlde user requests
    try:
        sock.send(filename.encode())
    except Exception as e:
        print(e)

    # Cleanup
    sock.close()

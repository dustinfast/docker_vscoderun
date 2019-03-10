#!/usr/bin/env python
""" docker_vscoderun - Server
    Listens on the port specified by LISTEN_PORT for client requests. On
    request receives, opens the file given in the request with the application
    specified by OPEN_WITH.
"""

import socket

HOST = '10.0.0.145'      # TCP Listen host
LISTEN_PORT = 5001      # TCP Listen port
MSG_SIZE = 1024         # TCP Msg Size
OPEN_WITH = 'code'      # VSCode command.

# Specifies addresses connections are allowed form. If empty, allows any.
# TODO: ALLOW_CONNS_FROM = []


if __name__ == '__main__':
    # Init listener
    sock = socket.socket()
    sock.bind((HOST, LISTEN_PORT))
    sock.listen(1)

    print('Listening on %s:%d...' % (HOST, LISTEN_PORT))

    # Block until request is received
    conn, client = sock.accept()

    # Process the request
    print('Received request from ' + str(client[0]))
    try:
        file_name = conn.recv(MSG_SIZE).decode()
        print('Opening "%s" with "%s"...' % (file_name, OPEN_WITH))

        conn.close()
    except Exception as e:
        print('ERROR:' + e)

    # Do cleanup
    sock.close()

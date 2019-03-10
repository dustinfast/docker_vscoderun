#!/usr/bin/env python
""" docker_vscoderun - Server
    Listens on the port specified by LISTEN_PORT for client requests. On
    request receives, opens the file given in the request with the application
    specified by EDITOR.
"""

import os
import socket

# Customizable constants
HOST = '10.0.0.145'                 # Docker host IP (do NOT use localhost)
HOST_PATH = 'c:\\dev\\'             # Host volume directory (no trailing /)
CONTAINER_PATH = '/repos'           # Container volume mount point
EDITOR = 'code'                     # Editor command. Ex: 'code' or 'notepad'
ALLOW_CONNS_FROM = ['10.0.0.145']   # Allowed IPs. If blank, allows all

# Other constants
LISTEN_PORT = 5001                  # TCP Listen port
MSG_SIZE = 1024                     # TCP Msg Size

if __name__ == '__main__':
    # Init listener
    try:
        sock = socket.socket()
        sock.bind((HOST, LISTEN_PORT))
        sock.listen(1)
    except OSError as e:
        print('docker_vscoderun failed to bind.')
        exit()

    print('docker_vscoderun listening on %s:%d...' % (HOST, LISTEN_PORT))

    # Accept incoming connections indefinetely
    while True:
        # Block until a request is received
        conn, client = sock.accept()
        client_ip = str(client[0])
        
        # Process or ignore the request, depending on client address
        if not ALLOW_CONNS_FROM or client_ip in ALLOW_CONNS_FROM:
            fname = conn.recv(MSG_SIZE).decode()
            fnamef = HOST_PATH + fname
            # print("Opening %s with %s from %s." % (fnamef, EDITOR, client_ip))

            # Ensure file is in container volume's mounted location
            if not fname.startswith(CONTAINER_PATH):
                # print('\tERROR: File is not located in container volume.')
                pass
            else:
                try:
                    os.system(EDITOR + ' ' + fnamef)
                except Exception as e:
                    print(e)
        else:
            # print('Ignored request from %s.' % client_ip)
            pass

        conn.close()

    # Do cleanup
    sock.close()

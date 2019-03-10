# docker_vscoderun

A simple convenience client/server application to open a file in Visual Studio Code on a host from inside a docker container.

The file must be in a location mounted on the host (i.e. with `docker build -v HOST_PATH:CONTAINER_PATH`).

This application may be easily modified to open the file in any editor. Simply modify the `OPEN_WITH` constant in `server.py`.

## Usage

Run the server on the host, and the client in the container. Then, from a terminal within the container, use `code FILENAME` to open the file in the host environment using Visual Studio Code.

## Security
For security reasons, you should modify the `ALLOW_CONNS_FROM` constant in `server.py` to include only the IP address of your container. Otherwise, the application will except connections from any IP address.

## Dependencies

* Python
* Visual Studio Code

Note: Visual Studio Code should not be installed in the container. If it is, rename `code.bash` to something that does not conflict with the vscode executable.

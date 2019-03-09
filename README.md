# docker_vscoderun

A simple convenience client/server application to open a file in visual studio code on a host from inside a docker container.

The file must be in a location mounted on the host (i.e. with `docker build -v HOST_PATH:CONTAINER_PATH`).

## Usage

Run the server on the host, and the client in the container. Then, from a terminal within the container, use `code FILENAME` to open the file in the host environment using visual studio code.

## Dependencies

* Python
* Visual Studio Code

Note: Visual Studio Code should not be installed in the container. If it is, rename `code.bash` to something that does not conflict with the vscode executable.

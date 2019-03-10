# docker_vscoderun

A convenience client/server application to open a file in Visual Studio Code (or your favorite editor) on your host from inside a Linux container's bash prompt.

Note: The file to be opened must be in a location mounted in the container from the host. I.e. with `docker build -v HOST_PATH:CONTAINER_PATH`.

## Usage

First, clone this repo into your HOST_PATH directory, then 
modify the "Customizable constants" in `server.py` according to your host environment and preffered editor... I like Visual Studio Code. Then run the server on your host with `python server.py`.

From your container's terminal, create an alias for the `code` command with `alias code='/repos/docker_vscoderun/code` (you may want to add this line to your ~/.bashrc to avoid having to do it again in the future).

You can now use `code FILENAME` to open any file in CONTAINER_PATH inside the editor on your host.

Tested functional with Windows 10 host and Ubuntu 14.04 container.

## Dependencies

* Python (on host and container)
* Visual Studio Code (on host)

Note: Visual Studio Code should not be installed in the container. If it is, name the `code` alias created in *Usage* to something that does not conflict with the vscode executable `/usr/bin/code`.

import socket
import os


def is_connected():

    IPaddress = socket.gethostbyname(socket.gethostname())
    print(IPaddress)
    return IPaddress != "127.0.0.1"


if __name__ == "__main__":
    if not is_connected():
        os.system("wifi-connect -o 8001")

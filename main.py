import os
from urllib.request import urlopen


def internet_on():
    try:
        response = urlopen('https://www.google.com/', timeout=5)
        return True
    except Exception:
        return False


if __name__ == "__main__":
    while True:
        try:
            if not internet_on():
                os.system("sudo wifi-connect -o 8001")
        except Exception:
            break
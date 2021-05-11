import os
import subprocess
from urllib.request import urlopen
from time import sleep
from gpiozero import Button

button = Button(26)


def internet_on():
    try:
        response = urlopen('https://www.google.com/', timeout=5)
        return True
    except Exception:
        return False


ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


def run_bash_script(path: str) -> subprocess.Popen:
    return subprocess.Popen(["sudo","/bin/sh", f"{ROOT_DIR}{path}"])


if __name__ == "__main__":

    proper_connection = False


    def proper_connection_to_true():
        global proper_connection
        print("Click button")
        proper_connection = True


    button.when_pressed = proper_connection_to_true

    run_bash_script("/shell_scripts/prepare.sh")
    print("Finished prepare")
    sleep(120)
    while not proper_connection:
        sleep(10)
        proper_connection = run_bash_script("/network/check_connected_device.sh").stdout == ""

    print("Close hotspot")
    run_bash_script("/shell_scripts/end_hotspot.sh")

    try:
        if internet_on():
            proper_connection = True
        else:
            sleep(10)

    except Exception:
        print("Error")
        exit(1)

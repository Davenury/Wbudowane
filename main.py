import os
import subprocess
from urllib.request import urlopen
from time import sleep
from gpiozero import Button
from jitsi_connection import generate_link, open_page, get_driver
from mail_service import send_message
from network.connect_to_wifi import refresh_connection
from multiprocessing import Process

button = Button(26)
callThread = None


def internet_on():
    try:
        response = urlopen('https://www.google.com/', timeout=5)
        return True
    except Exception:
        return False


ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


def run_bash_script(path: str) -> subprocess.Popen:
    return subprocess.Popen(["sudo", "/bin/sh", f"{ROOT_DIR}{path}"])


def button_action():
    global callThread

    if callThread is not None:
        callThread.kill()

    link = generate_link()
    send_message(link)
    print(f"Start meeting at {link}")

    def func():
        command = f"python3 -c '''import jitsi_connection;jitsi_connection.open_page('{link}')'''"
        os.system(f'''su - pi -c "{command}"''')

    callThread = Process(target=func)
    callThread.start()


if __name__ == "__main__":

    # while True:

    proper_connection = False


    def proper_connection_to_true():
        global proper_connection
        print("Click button")
        proper_connection = True


    button.when_pressed = proper_connection_to_true

    run_bash_script("/shell_scripts/prepare.sh")
    print("Finished prepare")
    counter = 120 / 5
    while not proper_connection:
        print(f"Still in loop: {proper_connection}")
        sleep(5)
        if counter > 0:
            counter -= 1
        elif not proper_connection:
            result = run_bash_script("/network/check_connected_device.sh").stdout
            proper_connection = result is None

    print("Close hotspot")
    run_bash_script("/shell_scripts/end_hotspot.sh")

    refresh_connection()
    sleep(10)
    button.when_pressed = button_action
    print("Changed button action")
    try:
        while internet_on():
            sleep(10)
        else:
            print("Not proper wifi or connection with internet lost")

    except Exception:
        print("Error")
        exit(1)

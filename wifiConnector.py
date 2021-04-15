import os
from configurationsGetter import get_configuration


def connect_to_wifi():
    config = get_configuration()
    interface = 'wlan0'
    name = config.get("ssid")
    password = config.get("password")
    os.system('iwconfig ' + interface + ' essid ' + name + ' key ' + password)

import os
from network.configurationsGetter import get_configuration

path_file = "/etc/wpa_supplicant/wpa_supplicant.conf"



def refresh_connection():
    command_restart_wifi_configuration = "sudo wpa_cli -i wlan0 reconfigure"
    os.system(command_restart_wifi_configuration)
    os.system("ping -c10 8.8.4.4")
def update_wifi():
    file = open(path_file, "w")
    values = get_configuration()
    file.write(
        f"""ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
        update_config=1
        country=GB
        
        network={{
            ssid="{values['ssid']}"
            psk="{values['password']}"
        }}
        """)
    file.close()
    refresh_connection()

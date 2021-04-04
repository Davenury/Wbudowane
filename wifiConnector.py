from wifi import Cell, Scheme
from configurationsGetter import get_configurations

ssid, email, password = get_configurations()

if __name__ == "__main__":
    cell = Cell.all('wlan0')[0]
    scheme = Scheme.for_cell('wlan0', ssid, cell, password)
    scheme.save()
    scheme.activate()

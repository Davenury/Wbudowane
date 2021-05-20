#!/bin/sh

sudo iwlist wlan0 scan | grep SSID | cut -f 2 -d ':' > wifi.txt
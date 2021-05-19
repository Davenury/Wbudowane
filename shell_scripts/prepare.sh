#!/bin/sh

#Prepare virtual interface
sudo iw phy phy0 interface add hotspot type __ap
sudo ifconfig hotspot 192.168.28.1

# Install packages needed for taking photos with python-opencv
sudo apt-get -y install libatlas-base-dev
sudo apt-get -y install dnsmasq

# Run flask app
export FLASK_APP=home/pi/Wbudowane/app.py
sudo -E python3 -m flask run --host=192.168.28.1 &
echo $! > process.txt

# Run hotspot
sudo hostapd home/pi/Wbudowane/shell_scripts/hostapd.conf
echo $! >> process.txt

# Run dhcp server
sudo udhcpd -f
echo $! >> process.txt

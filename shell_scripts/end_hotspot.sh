#!/bin/sh


cat process.txt | while read line
do
  sudo kill $line
done

sudo ifconfig wlan0 up
sudo ifconfig hotspot down
rm -f wifi.txt
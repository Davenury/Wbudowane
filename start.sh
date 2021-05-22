#! /bin/sh

pwd > /home/pi/where.txt
cd /home/pi/Wbudowane/ && (python3 ./jitsi_connection.py > /home/pi/log.txt 2>&1)
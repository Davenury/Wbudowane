
#Prepare virtual interface
sudo iw phy phy0 interface add hotspot type __ap
sudo ifconfig hotspot 192.168.28.1

# Install packages needed for taking photos with python-opencv
sudo apt-get install libatlas-base-dev

# Run hotspot
sudo hostapd hostapd.conf &
echo $! > process.txt

# Run dhcp server
sudo udhcpd -f &
echo $! >> process.txt
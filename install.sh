#!/bin/bash

# Installieren von den Notwendigen Softwaretools
sudo apt install -y gphoto2 libgphoto2*

# Einrichten der Services
sudo cp liveview.service /usr/lib/systemd/system/liveview.service
systemctl enable liveview.service
echo "lvstop='systemctl stop liveview.service'" >> .bashrc
echo "lvstart='systemctl start liveview.service'" >> .bashrc
#!/bin/bash

###########################################################
# Installations Skript für den Fernaulöser im Joy-Pi Koffer
# Author: Lorant Gulyas
# Version: 0.6
# Datum: 15.5.2024
############################################################

# Installieren von den Notwendigen Softwaretools
sudo apt update
sudo apt install -y gphoto2 libgphoto2* python3
sudo apt-get -y install python3-rpi.gpio
sudo mkdir /etc/gphoto2

# Kopieren aller Sckripts und Services in die korrekten Ordner
#Services
sudo cp motion.service /etc/systemd/system/motion.service
sudo chmod 644 /etc/systemd/system/motion.service
sudo cp liveview.service /etc/systemd/system/liveview.service
sudo chmod 644 /etc/systemd/system/liveview.service
sudo cp matrix.service /etc/systemd/system/matrix.service
sudo chmod 644 /etc/systemd/system/matrix.service
#Skripte
sudo cp bewegung.py /etc/gphoto2/bewegung.py
sudo cp tasten.py /etc/gphoto2/tasten.py
sudo cp liveView.sh /etc/gphoto2/liveview.sh
# Aktivieren der Services für den Autostart
sudo systemctl enable motion.service
sudo systemctl enable matrix.service
# sudo systemctl enable liveview.service

#Restart des Daemons
sudo systemctl daemon-reload
# Starten der Services
sudo systemctl start motion.service
sudo systemctl start matrix.service
sudo systemctl start liveview.service

echo "lvstop='systemctl stop liveview.service'" >> ../.bashrc
echo "lvstart='systemctl start liveview.service'" >> ../.bashrc
L5qEzQPL5b

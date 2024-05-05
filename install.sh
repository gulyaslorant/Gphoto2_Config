#!/bin/bash

# Installieren von den Notwendigen Softwaretools
sudo apt install -y gphoto2 libgphoto2*

# Kopieren aller Sckripts und Services in die korrekten Ordner
#Services
sudo cp motion.service /etc/systemd/system/motion.service
sudo chmod 644 /etc/systemd/system/motion.service
sudo cp liveview.service /etc/ystemd/system/liveview.service
sudo chmod 644 /etc/systemd/system/liveview.service
sudo cp bewegung.service /etc/systemd/system/bewegung.service
sudo chmod 644 /etc/systemd/system/bewegung.service
#Skripte
sudo cp bewegung.py /etc/gphoto2/bewegung.py
sudo cp tasten.py /etc/gphoto2/tasten.py
sudo cp liveView.sh /etc/gphoto2/liveview.sh# sudo systemctl enable liveview.service
# Aktivieren der Services für den Autostart
sudo systemctl enable motion.service
sudo systemctl enable bewegung.service
sudo systemctl enable liveview.service
#Restart des Daemons
sudo systemctl daemon-reload
# Starten der Services
sudo systemctl start motion.service
sudo systemctl start bewegung.service
sudo systemctl start liveview.service

echo "lvstop='systemctl stop liveview.service'" >> ../.bashrc
echo "lvstart='systemctl start liveview.service'" >> ../.bashrc

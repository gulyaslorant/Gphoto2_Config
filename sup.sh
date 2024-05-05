#!/bin/bash

# Kopieren aller Sckripts und Services in die korrekten Ordner
#Services
sudo cp motion.service /usr/lib/systemd/system/motion.service
sudo cp liveview.service /usr/lib/systemd/system/liveview.service
sudo cp bewegung.service /usr/lib/systemd/system/bewegung.service
#Skripte
sudo cp bewegung.py /etc/gphoto2/bewegung.py
sudo cp tasten.py /etc/gphoto2/tasten.py
sudo cp liveView.sh /etc/gphoto2/liveview.sh



# sudo systemctl enable liveview.service
sudo systemctl daemon-reload



echo "lvstop='systemctl stop liveview.service'" >> ../.bashrc
echo "lvstart='systemctl start liveview.service'" >> ../.bashrc

#!/bin/bash

# Update der Servicedatei & Befehlskürzel
sudo cp liveview.service /usr/lib/systemd/system/liveview.service
# sudo systemctl enable liveview.service
sudo systemctl daemon-reload

echo "lvstop='systemctl stop liveview.service'" >> .bashrc
echo "lvstart='systemctl start liveview.service'" >> .bashrc

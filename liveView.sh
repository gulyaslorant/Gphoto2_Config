#!/bin/bash

gphoto2 --set-config viewfinder=1
gphoto2 --capture-movie --stdout | mplayer -cache 128 -
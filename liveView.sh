#!/bin/bash

# gphoto2 --set-config viewfinder=1
# gphoto2 --capture-movie --stdout | mplayer -cache 128 -
gphoto2 --capture-movie --stdout | ffmpeg -i -vcodec rawvideo -pix_fmt yuv420p -threads 0 -f v4l2 -
# ExecStart=/usr/bin/sudo /bin/bash -lc 'gphoto2 --stdout --capture-movie | ffmpeg -i - -vcodec rawvideo -pix_fmt yuv420p -threads 0 -f v4l2 /dev/video0'
# ffmpeg -i -

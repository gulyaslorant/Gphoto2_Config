#!/usr/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time             #Importieren der Bibliotheken
import subprocess

motion_pin = 16  #Den Pin des Bewegungssensors einer Variable zuweisen.

GPIO.setmode(GPIO.BOARD) #Die GPIO Boardkonfiguration benutzen.
GPIO.setup(motion_pin, GPIO.IN)  #Der Pin der Deklarierten Variable wird als Input gesetzt.

try:                        # Beginn einer Schleife
    while True:
        # Der Wert 0 wurde nicht Berücksichtigt, weil keine Notwendigkeit besteht, einen Wert zu übermitteln, wenn keine Bewegung erkannt wurde.
       if(GPIO.input(motion_pin) == 1):
           result = subprocess.run(["sudo", "systemctl", "is-active", "--quiet", "liveview.service"])
           service_active = (result.returncode == 0)
           if service_active:
           # Stop liveview.service if it is running
               subprocess.run(["sudo", "systemctl", "stop", "liveview.service"])
           # Run the gphoto2 command
           subprocess.run(["gphoto2", "--capture-image"])
           # Service erneut starten, falls es vorher gelaufen ist.
           if service_active:
           # Start liveview.service again
               subprocess.run(["sudo", "systemctl", "start", "liveview.service"])  # Wenn der Sensor Input = 0 ist
              # Wird der print Befehl ausgeführt
       elif(GPIO.input(motion_pin) == 2): # Wenn der Sensor Input = 1 ist
              print ("Keine Bewegung ...")# Wird der print Befehl ausgeführt
       time.sleep(0.1) # 0,1 Sekunde Warten
except KeyboardInterrupt:
    GPIO.cleanup()     # Gibt GPIO Ports wieder frei.

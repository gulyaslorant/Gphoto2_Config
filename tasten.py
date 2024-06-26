#!/usr/bin/python

import RPi.GPIO as GPIO
import time
import subprocess
import os


class ButtonMatrix():

    def __init__(self):

        GPIO.setmode(GPIO.BOARD)

        # Die IDs der Buttons werden festgelegt
        self.buttonIDs = [[4,3,2,1],[8,7,6,5],[12,11,10,9],[16,15,14,13]]
        # GPIO Pins für die Zeilen werden deklariert.
        self.rowPins = [13,15,29,31]
        # GPIO Pins für die Spalte werden deklariert.
        self.columnPins = [33,35,37,22]

        # Definiere Vier Inputs mit pull up Widerständen.
        for i in range(len(self.rowPins)):
            GPIO.setup(self.rowPins[i], GPIO.IN, pull_up_down = GPIO.PUD_UP)

        # Definiere Vier Outputs und setze sie auf high.
        for j in range(len(self.columnPins)):
            GPIO.setup(self.columnPins[j], GPIO.OUT)
            GPIO.output(self.columnPins[j], 1)

    def activateButton(self, rowPin, colPin):
        # Erhalte die Button Nummer
        btnIndex = self.buttonIDs[rowPin][colPin]
# --------------------------------------------------------------
# --------------------------------------------------------------
# Knopf 1 ---------------------------------------------------
        if btnIndex == 1:
            # Check if liveview.service is active
            result = subprocess.run(["sudo", "systemctl", "is-active", "--quiet", "liveview.service"])
            service_active = (result.returncode == 0)
            if service_active:
                # Stop liveview.service if it is running
                subprocess.run(["sudo", "systemctl", "stop", "liveview.service"])
            # Run the gphoto2 command
            subprocess.run(["gphoto2", "--list-cameras"])
            # Service Erneut starten, falls er vorher gelaufen ist.
            if service_active:
                # Start liveview.service again
                subprocess.run(["sudo", "systemctl", "start", "liveview.service"])
 # Knopf 2 ----------------------------------------------
        if btnIndex == 2:
            # Check if liveview.service is active
            result = subprocess.run(["sudo", "systemctl", "is-active", "--quiet", "liveview.service"])
            service_active = (result.returncode == 0)

            if service_active:
            # Stop liveview.service if it is running
                subprocess.run(["sudo", "systemctl", "stop", "liveview.service"])
            # Run the gphoto2 command
            subprocess.run(["gphoto2", "--auto-detect"])
            # Service erneut starten, falls es vorher gelaufen ist.
            if service_active:
            # Start liveview.service again
                subprocess.run(["sudo", "systemctl", "start", "liveview.service"])
# Knopf 3 --------------------------------------------------
        if btnIndex == 3:
            if os.system('systemctl is-active --quiet liveview') == 0:
                subprocess.run(["systemctl","stop", "liveview"])
            else:
                subprocess.run(["systemctl","start", "liveview"])
# Knopf 4 ----------------------------------------------
        if btnIndex == 4:
            # Check if liveview.service is active
            result = subprocess.run(["sudo", "systemctl", "is-active", "--quiet", "liveview.service"])
            service_active = (result.returncode == 0)
            if service_active:
            # Stop liveview.service if it is running
                subprocess.run(["sudo", "systemctl", "stop", "liveview.service"])
            # Run the gphoto2 command
            subprocess.run(["gphoto2", "--config-list"])
            # Service erneut starten, falls es vorher gelaufen ist.
            if service_active:
            # Start liveview.service again
                subprocess.run(["sudo", "systemctl", "start", "liveview.service"])
# Knopf 5 ----------------------------------------------
        if btnIndex == 5:
        # Check if liveview.service is active
            result = subprocess.run(["sudo", "systemctl", "is-active", "--quiet", "liveview.service"])
            service_active = (result.returncode == 0)
            if service_active:
                # Stop liveview.service if it is running
                subprocess.run(["sudo", "systemctl", "stop", "liveview.service"])
                # Run the gphoto2 command
            subprocess.run(["gphoto2", "--set-config", "shutterspeed=1/60"])
                # Service erneut starten, falls es vorher gelaufen ist.
            if service_active:
             # Start liveview.service again
                subprocess.run(["sudo", "systemctl", "start", "liveview.service"])
# Knopf 6 ----------------------------------------------------------
        if btnIndex == 6:
        # Check if liveview.service is active
            result = subprocess.run(["sudo", "systemctl", "is-active", "--quiet", "liveview.service"])
            service_active = (result.returncode == 0)
            if service_active:
                # Stop liveview.service if it is running
                subprocess.run(["sudo", "systemctl", "stop", "liveview.service"])
                # Run the gphoto2 command
            subprocess.run(["gphoto2", "--set-config", "shutterspeed=1/125"])
                # Service erneut starten, falls es vorher gelaufen ist.
            if service_active:
             # Start liveview.service again
                subprocess.run(["sudo", "systemctl", "start", "liveview.service"])
# Knopf 7 ----------------------------------------------------------
        if btnIndex == 7:
            # Check if liveview.service is active
            result = subprocess.run(["sudo", "systemctl", "is-active", "--quiet", "liveview.service"])
            service_active = (result.returncode == 0)
            if service_active:
                # Stop liveview.service if it is running
                subprocess.run(["sudo", "systemctl", "stop", "liveview.service"])
            # Run the gphoto2 command
            subprocess.run(["gphoto2", "--set-config", "shutterspeed=1/500"])
                # Service erneut starten, falls es vorher gelaufen ist.
            if service_active:
                # Start liveview.service again
                subprocess.run(["sudo", "systemctl", "start", "liveview.service"])
# Knopf 8 ----------------------------------------------------------
        if btnIndex == 8:
        # Check if liveview.service is active
            result = subprocess.run(["sudo", "systemctl", "is-active", "--quiet", "liveview.service"])
            service_active = (result.returncode == 0)
            if service_active:
            # Stop liveview.service if it is running
                subprocess.run(["sudo", "systemctl", "stop", "liveview.service"])
            # Run the gphoto2 command
            subprocess.run(["gphoto2", "--set-config", "shutterspeed=1/1000"])
            # Service erneut starten, falls es vorher gelaufen ist.
            if service_active:
                # Start liveview.service again
                subprocess.run(["sudo", "systemctl", "start", "liveview.service"])
# Knopf 9 ----------------------------------------------------------
            if btnIndex == 9:
            # Check if liveview.service is active
                result = subprocess.run(["sudo", "systemctl", "is-active", "--quiet", "liveview.service"])
                service_active = (result.returncode == 0)
                if service_active:
                # Stop liveview.service if it is running
                    subprocess.run(["sudo", "systemctl", "stop", "liveview.service"])
                # Run the gphoto2 command
                subprocess.run(["gphoto2", "--set-config", "iso=200"])
                # Service erneut starten, falls es vorher gelaufen ist.
                if service_active:
                    # Start liveview.service again
                    subprocess.run(["sudo", "systemctl", "start", "liveview.service"])
# Knopf 10 ----------------------------------------------------------
            if btnIndex == 10:
            # Check if liveview.service is active
                result = subprocess.run(["sudo", "systemctl", "is-active", "--quiet", "liveview.service"])
                service_active = (result.returncode == 0)
                if service_active:
                # Stop liveview.service if it is running
                    subprocess.run(["sudo", "systemctl", "stop", "liveview.service"])
                # Run the gphoto2 command
                subprocess.run(["gphoto2", "--set-config", "iso=400"])
                    # Service erneut starten, falls es vorher gelaufen ist.
                if service_active:
                # Start liveview.service again
                    subprocess.run(["sudo", "systemctl", "start", "liveview.service"])
# Knopf 11 --------------------------------------------------------------
            if btnIndex == 11:
            # Check if liveview.service is active
                result = subprocess.run(["sudo", "systemctl", "is-active", "--quiet", "liveview.service"])
                service_active = (result.returncode == 0)
                if service_active:
                # Stop liveview.service if it is running
                    subprocess.run(["sudo", "systemctl", "stop", "liveview.service"])
                    # Run the gphoto2 command
                subprocess.run(["gphoto2", "--set-config", "iso=1250"])
                # Service erneut starten, falls es vorher gelaufen ist.
                if service_active:
                # Start liveview.service again
                    subprocess.run(["sudo", "systemctl", "start", "liveview.service"])
# Knopf 12 --------------------------------------------------------------
            if btnIndex == 12:
            # Check if liveview.service is active
                result = subprocess.run(["sudo", "systemctl", "is-active", "--quiet", "liveview.service"])
                service_active = (result.returncode == 0)
                if service_active:
                # Stop liveview.service if it is running
                    subprocess.run(["sudo", "systemctl", "stop", "liveview.service"])
                # Run the gphoto2 command
                subprocess.run(["gphoto2", "--set-config", "iso=3200"])
                # Service erneut starten, falls es vorher gelaufen ist.
                if service_active:
                # Start liveview.service again
                    subprocess.run(["sudo", "systemctl", "start", "liveview.service"])
# Knopf 13 --------------------------------------------------------------
            if btnIndex == 13:
                # Check if liveview.service is active
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
                    subprocess.run(["sudo", "systemctl", "start", "liveview.service"])
        #if btnIndex == 14:
        #    subprocess.run(["gphoto2", "--capture-image-and-download --filename="~/Pictures/Bild001.%C"])
# Knopf 15 --------------------------------------------------------------
            if btnIndex == 15:
            # Check if liveview.service is active
                result = subprocess.run(["sudo", "systemctl", "is-active", "--quiet", "liveview.service"])
                service_active = (result.returncode == 0)
                if service_active:
                # Stop liveview.service if it is running
                    subprocess.run(["sudo", "systemctl", "stop", "liveview.service"])
                # Run the gphoto2 command
                subprocess.run(["gphoto2", "--capture-image-and-download"])
                    # Service erneut starten, falls es vorher gelaufen ist.
                if service_active:
                # Start liveview.service again
                    subprocess.run(["sudo", "systemctl", "start", "liveview.service"])
# Knopf 16 --------------------------------------------------------------
            if btnIndex == 16:
            # Check if liveview.service is active
                result = subprocess.run(["sudo", "systemctl", "is-active", "--quiet", "liveview.service"])
                service_active = (result.returncode == 0)
                if service_active:
                # Stop liveview.service if it is running
                    subprocess.run(["sudo", "systemctl", "stop", "liveview.service"])
                # Run the gphoto2 command
                subprocess.run(["gphoto2", "--list-files"])
                # Service erneut starten, falls es vorher gelaufen ist.
                if service_active:
                # Start liveview.service again
                    subprocess.run(["sudo", "systemctl", "start", "liveview.service"])
        # Verhindert mehrere Knopfdrücke in zu kurzer zeit
        time.sleep(.3)

    def buttonHeldDown(self,pin):
        if(GPIO.input(self.rowPins[pin]) == 0):
            return True
        return False

def main():

    # Initialisierung der Button Matrix
    buttons = ButtonMatrix()

    try:
        while(True):
            for j in range(len(buttons.columnPins)):
                # Jeder Output Pin wird auf low gesetzt.
                GPIO.output(buttons.columnPins[j],0)
                for i in range(len(buttons.rowPins)):
                    if GPIO.input(buttons.rowPins[i]) == 0:
                        buttons.activateButton(i,j)
                        # Nichts tun solange der Button gedrückt gehalten wird.
                        while(buttons.buttonHeldDown(i)):
                            pass
                GPIO.output(buttons.columnPins[j],1)
    except KeyboardInterrupt:
        GPIO.cleanup()

if __name__ == "__main__":
    main()

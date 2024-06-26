# Konfigurationsdateien für Gphoto2

## Folgende Dateien sind im Paket enthalten

- bewegung.py
- controls.py
- install.sh
- liveview.service
- liveView.sh
- matrix.service
- motion.serice
- sup.sh
- tasten.py

## Initialisierung aller Services

Hierzu muss die Intall.sh Datei mit +x Rechten genehmigt werden, um ausgeführt werden zu können.

Hierzu folgenden Befehl in dem Gphoto2_config Ordner ausführen

`sudo chmod +x install.sh`

Danach das Script ausführen, um die notwendigen Tools zu installieren, das bedeutet Gphot2 sowie die notwendigen Libs. Zusätzlich werden die Services angelegt, und eingerichtet, dass sie mit dem Hochfahren starten

## Liveview Einstellungen

liveview Service ist die Servicedatei, welche in den Service Ordner kopiert werden muss

hierzu folgenden Befehl ausführen:

`cp liveview.service /etc/systemd/system/liveview.service`

## Folgende Dateien sind auf den Joy-Pi abgestimmt

- tasten.py
- bewegung.py

Beide werden als Service gestartet, damit sie im Hintergrund direkt aufgerufen werden können. Später werden die Dateien in eine zusammengefasst, damit alle Steuerungen in einer Datei zusammengefasst werden.

### matrix.service steuert die Knöpfe der 16 Buttons, welche mit Funktionen hinterlegt sind.

## In der Obersten Reihe sind die Grundlegenden Funktionen.

1. Auflistung der Verfügbaren Kameras
2. Initialisierung der angeschlossenen Kamera
3. Start/Stop der Live View Funktion
4. Liste aller Einstellmöglichkeiten

## In der 2. Reihe von oben hat man die Möglichkeit die Belichtungszeiten anzupassen

1. 1/60
2. 1/125
3. 1/500
4. 1/1000

## Vorletzte Reihe bietet die Möglichkeiten für Iso Einstellungen

1. Iso 125
2. Iso 400
3. Iso 1250
4. Iso 3200

## In der letzten Reihe hat man Aufnahmemöglichkeiten

1. Aufnahme auf die Speicherkart
2. Aufnahme auf das Gerät
3. -
4. Liste aller Dateien auf dem Gerät

### In der Motion.py Datei wird der Bewegungssensor angesteuert.

Hiermit soll sicher gestellt werden, dass die Kamera auch auslöst, wenn eine Handbewegung registriert wird.

### Updaten der Skripte

- sup.sh

Mit folgenden Befehl das passende Skript ausführbar machen

`sudo chmod +x sup.sh`

Danach das Skript einfach ausführen, um alle notwendigen Dateien zu kopieren und Services zu aktualisieren.

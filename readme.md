# Konfigurationsdateien für Gphoto2

## Folgende Dateien sind im Paket enthalten

- liveview.service
- liveview.sh

liveview Service ist die Servicedatei, welche in den Service Ordner kopiert werden muss

hierzu folgenden Befehl ausführen:

`cp liveview.service /etc/systemd/system/liveview.service`

## Folgende Dateien sind auf den Joy-Pi abgestimmt

- button_matrix.py
- motion.py

Beide werden als Service gestartet, damit sie im Hintergrund direkt aufgerufen werden können. Später werden die Dateien in eine zusammengefasst, damit alle Steuerungen in einer Datei zusammengefasst werden.

### Button_matrix steuert die Knöpfe der 16 Buttons, welche mit Funktionen hinterlegt sind.

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

# Raspberry Pi Pico W Audio-Modul Projekt

In diesem Projekt wird ein PCM5100A Audio-Modul an den Raspberry Pi Pico W angeschlossen, um Soundausgabe mit `.wav` und `.pcm`-Dateien zu ermöglichen. Der Code wurde mit MicroPython in Thonny entwickelt.

## Projektübersicht

Nach dem Erlernen der Python-Grundlagen und der Arbeit mit einem Starterset für den Raspberry Pi Pico W, habe ich dieses Projekt entwickelt, um ein Audio-Modul anzuschließen und zu steuern. Ziel war es, Audiodaten über I2S (Inter-IC Sound) zu übertragen und die Wiedergabe von Audio-Dateien auf dem Pico W zu ermöglichen.

## Was du benötigst

- Raspberry Pi Pico W
- PCM5100A Audio-Modul
- 5 Männlich-Weiblich Jumper-Kabel
- 2 x 8 Ohm, 2W Lautsprecher
- MicroPython und Thonny IDE

## Anleitung zum Anschließen des Audio-Moduls

### Pinbelegung für das PCM5100A Audio-Modul:
- **BCK (Pin 15)**: Bit Clock (Takt für die Datenübertragung)
- **LCK (Pin 16)**: Word Select (Kanalauswahl – links/rechts)
- **DIN (Pin 17)**: Serial Data (Datenübertragung)

### Schritte zum Setup:
1. Verbinde das PCM5100A Audio-Modul mit dem Raspberry Pi Pico W gemäß der oben genannten Pinbelegung.
2. Installiere die erforderlichen MicroPython-Bibliotheken über Thonny:
   - Öffne Thonny und gehe zu „Tools“ > „Manage packages“.
   - Suche nach den notwendigen Bibliotheken und installiere sie.
3. Lade die bereitgestellten Python-Skripte (`wavcode.py` und `pcmcode.py`) hoch, um die Audiodaten abzuspielen.
4. Komprimiere `.wav`-Dateien, um sie im Pico W mit begrenztem Speicherplatz (max. 2 MB) zu nutzen.

## Nützliche Links

Weitere nützliche Ressourcen und Tools findest du in der mitgelieferten PDF- oder DOCX-Datei.

## Fazit

Dieses Projekt hilft dir, die grundlegenden Prinzipien der Audioübertragung über I2S zu verstehen und den Raspberry Pi Pico W mit einem Audio-Modul zu verbinden. Mit MicroPython und Thonny kannst du einfach mit dem Pico W experimentieren und lernen.

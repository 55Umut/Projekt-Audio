# 🎧 Umut | Raspberry Pi Pico W Audio-Projekt

<div align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=32&duration=3000&pause=1000&color=2F81F7&center=true&vCenter=true&width=600&lines=Willkommen+beim+Audio-Projekt;MicroPython+%2B+Raspberry+Pi+Pico+W;Sound+via+I2S;Lernen+durch+Projekte" alt="Typing SVG" />
</div>

<div align="center">
  <a href="https://github.com/55Umut/Projekt-Audio">
    <img src="https://img.shields.io/badge/🔊%20Projekt-Audio%20mit%20Pico%20W-brightgreen?style=for-the-badge" alt="Projekt Audio" />
  </a>
</div>

---

## 📘 Projektübersicht

In diesem Projekt wird ein **PCM5100A Audio-Modul** an den **Raspberry Pi Pico W** angeschlossen, um Soundausgabe mit `.wav`- und `.pcm`-Dateien zu ermöglichen.  
Der Code wurde in **MicroPython** mit der **Thonny IDE** geschrieben.

🎯 **Ziel**: Audio über I2S-Schnittstelle abspielen und ein praktisches Embedded-Projekt mit Soundausgabe umsetzen.

---

## 🧰 Was du benötigst

- 🧠 Raspberry Pi Pico W
- 🔊 PCM5100A Audio-Modul
- 🔌 5 Jumper-Kabel (Männlich-Weiblich)
- 🔈 2 Lautsprecher (8 Ohm, 2W)
- 💻 Thonny IDE & MicroPython-Firmware

---

## 🛠️ Anleitung zum Anschließen des Audio-Moduls

### 📌 Pinbelegung für das PCM5100A Audio-Modul:

| Modul Pin | Pico W Pin | Funktion          |
|-----------|------------|-------------------|
| BCK       | GP15       | Bit Clock         |
| LCK       | GP16       | Word Select       |
| DIN       | GP17       | Serial Data       |

---

### 🧪 Setup-Schritte:

1. **Hardware anschließen**: Verbinde das Modul laut obiger Tabelle mit dem Pico W.
2. **Firmware**: Flash MicroPython auf den Pico W (z. B. via Thonny).
3. **Thonny öffnen** → „Tools > Manage Packages“ → benötigte Pakete installieren.
4. **Python-Skripte hochladen**:  
   - `wavcode.py`  
   - `pcmcode.py`
5. **Audiodateien vorbereiten**: `.wav`-Dateien auf max. **2 MB** komprimieren.

---

## 📁 Projektstruktur

```bash
Projekt-Audio/
├── wavcode.py            # Audio-Ausgabe mit .wav-Dateien
├── pcmcode.py            # Audio-Ausgabe mit .pcm-Dateien
├── AudioTestFiles/       # Beispiel-Dateien
├── Ressourcen/           # PDF/DOCX-Dokumentation
└── README.md             # Dieses Dokument


## 👨‍💻 Beispielcode

```python
import wavcode

wavcode.play("sound.wav") 

## 🧠 Lernziele

- ✅ Grundlagen der Audioübertragung über I2S verstehen  
- ✅ Arbeiten mit Hardwaremodulen und GPIOs  
- ✅ Sound-Dateien in Embedded-Systemen abspielen  
- 🟡 GUI oder Weboberfläche für Dateiauswahl entwickeln  
- 🟡 Audio-Kompression / Encoder-Skripte schreiben  

---

## 📚 Nützliche Ressourcen

- 📂 Siehe den Ordner `Ressourcen/` (PDF & DOCX)  
- 🌐 [Raspberry Pi Pico W Docs](https://www.raspberrypi.com/documentation/microcontrollers/)  
- 📹 YouTube Tutorials zum Thema „Pico W Audio“  

---

## 🔮 Zukünftige Erweiterungen

- Lautstärkeregler via Potentiometer  
- OLED-Display mit Titelanzeige  
- WLAN Webinterface zur Dateiauswahl  

---

## 🧩 Technologien & Tools

<div align="center">
  <img src="https://img.shields.io/badge/MicroPython-black?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Raspberry%20Pi%20Pico%20W-green?style=for-the-badge&logo=raspberry-pi&logoColor=white" />
  <img src="https://img.shields.io/badge/Thonny-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/I2S-Audio-red?style=for-the-badge" />
</div>

---

## 📫 Kontakt

- GitHub: [@55Umut](https://github.com/55Umut)  
- LinkedIn: in Arbeit  
- E-Mail: auf Anfrage  

<div align="center">
  <img src="https://komarev.com/ghpvc/?username=55Umut&color=blue" alt="Profile Views" />
  <br><br>
  <b>Danke fürs Reinschauen 🎧</b><br>
  <i>Feedback & Pull Requests sind jederzeit willkommen!</i>
</div>

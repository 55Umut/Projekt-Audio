from machine import Pin, I2S
import time
import gc

# Führe Garbage Collection durch
gc.collect()

# Definiere die Pins für die I2S-Kommunikation (angepasst)
bck = Pin(15)  # Bit Clock Pin (BCK) -> Pin 15
ws = Pin(16)   # Word Select Pin (LCK) -> Pin 16
sd = Pin(17)   # Serial Data Pin (DIN) -> Pin 17

# I2S-Konfiguration
SAMPLE_RATE = 44100  # Standard-Abtastrate für PCM-Daten
BITS = 16           # 16-Bit PCM-Daten
BUFFER_LENGTH_IN_BYTES = 40000  # Erhöhe den Puffer


# Initialisiere die I2S-Schnittstelle für Mono-Ausgabe
audio_out = I2S(0,
                sck=bck,
                ws=ws,
                sd=sd,
                mode=I2S.TX,
                bits=BITS,
                format=I2S.MONO,  # Mono-Ausgabe (falls gewünscht)
                rate=SAMPLE_RATE,
                ibuf=BUFFER_LENGTH_IN_BYTES)

# Funktion zum Einlesen der PCM-Daten in Chunks
def read_pcm_file_in_chunks(filename, chunk_size):
    with open(filename, 'rb') as f:
        while True:
            chunk = f.read(chunk_size)  
            if not chunk:
                break  
            yield chunk  

# Lese und spiele die PCM-Daten aus der Datei 'ezp.pcm' ab
chunk_size = 1024  # Größe der Chunks 

print("Spiele PCM-Datei ab...")

# Lese die Datei in Chunks und gebe sie über I2S aus
for chunk in read_pcm_file_in_chunks('ezp.pcm', chunk_size):
    audio_out.write(bytearray(chunk))  # Schreibe den aktuellen Chunk an den I2S-Ausgang

# Deinitialisiere die I2S-Schnittstelle nach der Wiedergabe
audio_out.deinit()

print("Fertig!")

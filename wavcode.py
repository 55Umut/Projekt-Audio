from machine import Pin, I2S
import time
import gc
import struct
import os

# Führe Garbage Collection durch
gc.collect()

# Definiere die Pins für die I2S-Kommunikation
bck = Pin(15)  # Bit Clock Pin (BCK) -> Pin 15
ws = Pin(16)   # Word Select Pin (LCK) -> Pin 16
sd = Pin(17)   # Serial Data Pin (DIN) -> Pin 17

# I2S-Konfiguration
BUFFER_LENGTH_IN_BYTES = 40000

# Funktion zum Lesen des WAV-Headers
def read_wav_header(file):
    riff, size, fformat = struct.unpack('<4sI4s', file.read(12))
    if riff != b'RIFF' or fformat != b'WAVE':
        raise ValueError("Ungültiges WAV-Format")

    chunk_header = file.read(8)
    subchunk_id, subchunk_size = struct.unpack('<4sI', chunk_header)

    if subchunk_id == b'fmt ':
        fmt = struct.unpack('<HHIIHH', file.read(16))
        audio_format, channels, sample_rate, _, _, bits_per_sample = fmt

        # Überprüfe die Anzahl der Bits pro Sample
        if bits_per_sample not in [8, 16, 24, 32]:
            raise ValueError(f"Ungültige Anzahl der Bits pro Sample: {bits_per_sample}. Erwartet: 8, 16, 24 oder 32.")

        # Ausgabe zur Diagnose
        print(f"Header Info: Sample Rate: {sample_rate}, Channels: {channels}, Bits per Sample: {bits_per_sample}")
        
        return sample_rate, channels, bits_per_sample
    else:
        raise ValueError("Ungültiger WAV-Header")

# Funktion zum Einlesen der WAV-Daten in Chunks
def read_wav_file_in_chunks(filename, chunk_size):
    try:
        file_size = os.stat(filename)[6]
        print(f"Dateigröße: {file_size} Bytes")
        
        with open(filename, 'rb') as f:
            sample_rate, channels, bits_per_sample = read_wav_header(f)
            
            audio_format = I2S.STEREO if channels == 2 else I2S.MONO
            
            # Verwende 16 Bit für die I2S-Konfiguration, auch wenn die Datei 8-Bit ist
            i2s_bits = 16 if bits_per_sample == 8 else bits_per_sample
            audio_out = I2S(0, sck=bck, ws=ws, sd=sd, mode=I2S.TX,
                            bits=i2s_bits, format=audio_format,
                            rate=sample_rate, ibuf=BUFFER_LENGTH_IN_BYTES)
            
            f.seek(44)  # Standard WAV-Header-Länge
            
            chunks_read = 0
            while True:
                chunk = f.read(chunk_size)
                if not chunk:
                    break
                if bits_per_sample == 8:
                    # Konvertiere 8-Bit zu 16-Bit
                    chunk = b''.join(bytes([0, b]) for b in chunk)
                chunks_read += 1
                if chunks_read % 100 == 0:
                    print(f"Chunks gelesen: {chunks_read}")
                yield audio_out, chunk
            
            audio_out.deinit()
    except Exception as e:
        print(f"Fehler beim Lesen der WAV-Datei: {e}")

# Lese und spiele die WAV-Datei ab
chunk_size = 2048  # Größe der Chunks

print("Spiele WAV-Datei ab...")

try:
    # Lese die Datei in Chunks und gebe sie über I2S aus
    for audio_out, chunk in read_wav_file_in_chunks('trimed2.wav', chunk_size):
        audio_out.write(chunk)
    print("Wiedergabe erfolgreich beendet.")
except Exception as e:
    print(f"Fehler während der Wiedergabe: {e}")

print("Fertig!")

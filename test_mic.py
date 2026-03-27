# test_mic.py
import sounddevice as sd
import scipy.io.wavfile as wav
import numpy as np

# Copiado del config.py
DEVICE_INDEX = 16 
SAMPLE_RATE = 16000
DURATION = 3

def test_recording():
    print(f"🎤 Probando grabación (3 segundos) en el dispositivo {DEVICE_INDEX}...")
    try:
        audio = sd.rec(
            int(DURATION * SAMPLE_RATE),
            samplerate=SAMPLE_RATE,
            channels=1,
            dtype='int16',
            device=DEVICE_INDEX
        )
        sd.wait()
        print("✅ Grabación completada.")
        
        filename = "test_recording.wav"
        wav.write(filename, SAMPLE_RATE, audio)
        print(f"📂 Archivo guardado como '{filename}'.")
        print(f"▶️ Reproduciendo ahora...")
        
        # Intentar reproducir usando sounddevice
        sd.play(audio, SAMPLE_RATE)
        sd.wait()
        print("✅ Prueba finalizada. Si escuchaste tu voz, ¡el micro está listo!")
        
    except Exception as e:
        print(f"❌ Error durante la prueba: {e}")

if __name__ == "__main__":
    test_recording()

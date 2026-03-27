# services/stt.py
from faster_whisper import WhisperModel
import sounddevice as sd
import numpy as np
import sys
import os

# Path hack para importar config sin problemas
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import WHISPER_MODEL, SAMPLE_RATE, RECORD_SECONDS, DEVICE_INDEX

class STTService:
    def __init__(self):
        # Usamos la ruta local donde estás descargando los archivos con wget
        model_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "models", "tiny")
        print(f"🎙️ Cargando Faster-Whisper desde carpeta local: {model_path}...")
        self.model = WhisperModel(model_path, compute_type="int8", local_files_only=True)

    def record_audio(self):
        print("🎤 Grabando...")
        audio = sd.rec(
            int(RECORD_SECONDS * SAMPLE_RATE),
            samplerate=SAMPLE_RATE,
            channels=1,
            dtype='int16',
            device=DEVICE_INDEX
        )
        sd.wait()
        return audio.flatten()

    def transcribe(self, audio):
        # 1. Convertir int16 a float32 y normalizar a [-1, 1]
        audio_fp32 = audio.astype(np.float32) / 32768.0
        
        # 2. Normalización de amplitud (Mic Boost por software)
        # Esto ayuda si el micrófono se escucha muy bajo.
        max_amplitude = np.max(np.abs(audio_fp32))
        if max_amplitude > 0:
            audio_fp32 = audio_fp32 / max_amplitude
            
        print(f"📊 Audio amplificado (máx: {max_amplitude:.4f} -> 1.0)")
        
        segments, _ = self.model.transcribe(audio_fp32, language="es")
        return " ".join([seg.text for seg in segments])

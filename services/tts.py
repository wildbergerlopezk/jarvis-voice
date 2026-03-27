# services/tts.py
import subprocess
import tempfile
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import PIPER_MODEL_PATH, PIPER_BINARY

class TTSService:
    def __init__(self):
        # Aseguramos que la ruta al modelo y al binario sean absolutas
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.model_path = os.path.join(base_dir, PIPER_MODEL_PATH) if not os.path.isabs(PIPER_MODEL_PATH) else PIPER_MODEL_PATH
        self.binary_path = os.path.join(base_dir, PIPER_BINARY) if not os.path.isabs(PIPER_BINARY) else PIPER_BINARY
        print(f"🔊 Piper listo con modelo: {self.model_path}")

    def speak(self, text):
        if not text:
            return
            
        temp_wav = "/tmp/jarvis_speech.wav"
        try:
            # 1. Generar audio con Piper
            subprocess.run(
                [
                    self.binary_path,
                    "--model", self.model_path,
                    "--output_file", temp_wav
                ],
                input=text.encode(),
                check=True,
                stderr=subprocess.PIPE
            )

            # 2. Reproducir con aplay
            subprocess.run(["aplay", temp_wav], check=True)
            
            # Limpiar
            if os.path.exists(temp_wav):
                os.remove(temp_wav)
        except Exception as e:
            print(f"❌ Error en TTS: {e}")
            print(f"🤖 Jarvis dice (pero no ha podido sonar): {text}")

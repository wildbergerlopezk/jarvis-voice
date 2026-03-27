# config.py
import subprocess
import sounddevice as sd

# IMPORTANTE: Cambia el DEVICE_INDEX ejecutando utils/audio_utils.py primero.
# Habitualmente el micrófono será el índice con '(input)' y más canales.
DEVICE_INDEX = 16

WHISPER_MODEL = "tiny" # Usamos 'tiny' primero para que descargue rápido (75MB) y probar que todo funciona.
SAMPLE_RATE = 16000
RECORD_SECONDS = 3

# Usamos tinyllama porque es el más rápido para tu CPU
OLLAMA_MODEL = "tinyllama:latest"

# Ruta del binario de Piper extraído
PIPER_BINARY = "./piper/piper"

# Ruta del modelo de Piper. Lo bajaremos localmente para que funcione siempre.
PIPER_MODEL_PATH = "es_ES-davefx-medium.onnx"

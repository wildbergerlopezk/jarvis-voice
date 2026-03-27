# services/stt.py
import speech_recognition as sr

def transcribe_audio(audio_data):
    """
    Convierte audio a texto usando Whisper.
    Requiere que esté instalado: pip install speechrecognition pydub whisper
    """
    recognizer = sr.Recognizer()
    
    try:
        text = recognizer.recognize_whisper(audio_data, model="large-v3")
        return text
    except Exception as e:
        print("❌ Error en STT:", str(e))
        return "Error al convertir voz a texto"

# services/tts.py
import os
from pydub import AudioSegment
from gtts import gTTS  # Alternativa si no tienes Coqui

def speak(text):
    """
    Convierte texto a voz en español.
    Usa gTTS (Google Text-to-Speech) como alternativa sencilla.
    Para voz natural, usa Coqui XTTS con modelo de voz local.
    """
    
    try:
        # Opción 1: Usar Google TTS (sencillo)
        tts = gTTS(text=text, lang='es')
        audio_file = "tts_output.mp3"
        tts.save(audio_file)
        
        # Reproducir
        from playsound import playsound
        playsound(audio_file)
        
        print(f"🔊 Dicho: {text}")
    except Exception as e:
        print("❌ Error en TTS:", str(e))

# agent/utils.py
import threading
import time
import queue
from pydub import AudioSegment
import speech_recognition as sr

class JarvisContext:
    def __init__(self):
        self.is_active = False
        self.audio_queue = queue.Queue()
        self.listen_thread = None
    
    def activate(self, wake_word_detected=True):
        """
        Activa el modo de escucha. Una vez activado, no necesitas decir 'jarvis' más.
        El sistema escuchará continuamente por el micrófono.
        """
        if not self.is_active:
            print("✅ Jarvis está listo para escuchar. Dile cualquier cosa ahora.")
            self.is_active = True
            # Inicia hilo de escucha en segundo plano (para que no bloquee el script)
            self.listen_thread = threading.Thread(target=self._listen_forever, daemon=True)
            self.listen_thread.start()
    
    def _listen_forever(self):
        """
        Escucha continuamente por el micrófono mientras esté activo.
        Cada vez detecta voz → convierte a texto y envía al agente principal.
        """
        import speech_recognition as sr
        recognizer = sr.Recognizer()

        while self.is_active:
            try:
                with sr.Microphone() as source:
                    print("🎙️ Escuchando... (dile algo)")
                    audio = recognizer.record(source, duration=3)  # Escucha por 3 segundos
                    
                    # Convertir a texto usando Whisper (requiere que esté instalado)
                    text = recognizer.recognize_whisper(audio, model="large-v3")
                    print(f"🔊 Texto detectado: {text}")
                    
                    # Enviar al agente principal para procesar
                    self.audio_queue.put(text)
            except Exception as e:
                print("❌ Error de micrófono:", str(e))
                time.sleep(1)

# Ejemplo de uso en el loop principal (en conversation_loop.py o en brain.py)
jarvis_context = JarvisContext()

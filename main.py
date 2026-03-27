# main.py
from services.stt import STTService
from services.tts import TTSService
from services.llm import LLMService
import sys
import os

def main():
    print("🚀 Iniciando Jarvis (Fase 1)...")
    
    try:
        stt = STTService()
        tts = TTSService()
        llm = LLMService()
    except Exception as e:
        print(f"❌ Error al inicializar servicios: {e}")
        return

    print("\n🎤 Jarvis listo. Hablar ahora (grabación de 3s)...")

    while True:
        try:
            # 1. Grabar y Transcribir
            audio = stt.record_audio()
            text = stt.transcribe(audio)

            if not text.strip():
                continue

            print(f"🧑: {text}")

            # 2. Generar respuesta con Ollama
            print("🧠 Pensando...")
            response = llm.generate(text)
            print(f"🤖: {response}")

            # 3. Hablar la respuesta
            tts.speak(response)
            
            print("\n🎙️ Esperando siguiente comando...")

        except KeyboardInterrupt:
            print("\n👋 Saliendo de Jarvis. ¡Hasta pronto!")
            break
        except Exception as e:
            print(f"⚠️ Error inesperado: {e}")
            continue

if __name__ == "__main__":
    main()

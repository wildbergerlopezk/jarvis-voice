# utils/audio_utils.py
import sounddevice as sd

def list_devices():
    """
    Lista todos los dispositivos de audio disponibles.
    Busca el índice del micrófono que quieres usar.
    """
    print("\n--- Dispositivos de Audio Detectados ---")
    print(sd.query_devices())
    print("-" * 40)
    print("TIP: Busca el índice del dispositivo que tenga 'input' y canales > 0.")

if __name__ == "__main__":
    list_devices()
